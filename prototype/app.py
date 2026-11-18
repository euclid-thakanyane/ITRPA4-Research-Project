"""
ITRPA4 prototype: Twitter-based influenza outbreak risk explorer.

Loads the best statistical model and the best machine learning model saved by itrpa_experiments.ipynb and lets the user
  1. pick a state and time step from the held-out test split,
  2. upload or type keyword counts,
  3. compare all models (evaluated test results), and
  4. explore a live X (Twitter) signal dashboard (ILLUSTRATION ONLY, not part of the evaluated results).

Run:  streamlit run app.py
"""
import json, os, re
from datetime import timedelta
import numpy as np
import pandas as pd
import scipy.sparse as sp
import joblib
import streamlit as st
import matplotlib.pyplot as plt

import itrpa_models  # noqa: F401  (needed so joblib can unpickle custom classes / functions)
from itrpa_models import CountGLMClassifier, BayesLogRegPosterior

HERE = os.path.dirname(os.path.abspath(__file__))
ART = os.path.join(HERE, "artifacts")
FIGS = os.path.join(HERE, "..", "figures")
LIVE_POSTS = os.path.join(HERE, "sample_live_posts.json")
LIVE_COUNTS = os.path.join(HERE, "live_daily_counts.json")
LIVE_OVERLAP = os.path.join(HERE, "live_keyword_overlap.json")

st.set_page_config(page_title="ITRPA4 Flu Outbreak Risk Prototype", layout="wide")

# ----------------------------------------------------------------------------------------------------------- loading
@st.cache_resource
def load_artifacts():
    meta = json.load(open(os.path.join(ART, "meta.json")))
    m_stat = joblib.load(os.path.join(ART, "best_stat_model.joblib"))
    m_ml = joblib.load(os.path.join(ART, "best_ml_model.joblib"))
    X_te = sp.csr_matrix(sp.load_npz(os.path.join(ART, "X_test.npz")))  # csr_matrix keeps 2-D row slices
    te_meta = pd.read_csv(os.path.join(ART, "test_meta.csv"))
    preds = pd.read_csv(os.path.join(ART, "test_predictions.csv"))
    res = pd.read_csv(os.path.join(ART, "test_results.csv"), index_col=0)
    rt = pd.read_csv(os.path.join(ART, "runtime.csv"), index_col=0)
    cal = pd.read_csv(os.path.join(ART, "calibration_posthoc.csv"))
    return meta, m_stat, m_ml, X_te, te_meta, preds, res, rt, cal

meta, M_STAT, M_ML, X_TE, TE_META, PREDS, RES, RT, CAL = load_artifacts()

@st.cache_resource
def load_improved():
    """Improved temporal model (section 14 of the notebook). Optional: the app still runs without these files."""
    f = os.path.join(ART, "improved_meta.json")
    if not os.path.exists(f):
        return None
    out = dict(meta=json.load(open(f)), preds=pd.read_csv(os.path.join(ART, "improved_test_predictions.csv")))
    for k in ("improve_summary", "improve_bootstrap_ci", "improve_significance", "improve_operating_points"):
        fp = os.path.join(ART, k + ".csv")
        out[k] = pd.read_csv(fp) if os.path.exists(fp) else None
    return out

IMP = load_improved()
FEATS, KEYWORDS, N_AUX, STATES = meta["feature_names"], meta["keywords"], meta["n_aux"], meta["states"]
NAME_STAT, NAME_ML = meta["best_stat"], meta["best_ml"]
THR = meta["thresholds"]
STATE_IDX = {s: i for i, s in enumerate(STATES)}
KW_SET = {k: N_AUX + i for i, k in enumerate(KEYWORDS)}

# ----------------------------------------------------------------------------------------------------------- scoring
def predict(model, X, state):
    """Outbreak probability for rows of X (csr). `state` is used only by the count-GLM models."""
    if isinstance(model, CountGLMClassifier):
        return model.predict_proba(X, np.full(X.shape[0], STATE_IDX[state]))[:, 1]
    return model.predict_proba(X)[:, 1]

def contributions(model, x, state):
    """Per-feature contribution to the prediction for one row x (1 x p csr). Returns (Series, method label)."""
    if isinstance(model, BayesLogRegPosterior):
        z = model.transform(x).ravel()
        return pd.Series(z * model.coef_mean, index=model.feature_names), "posterior-mean coefficient x standardised log1p value (log-odds)"
    if isinstance(model, CountGLMClassifier):
        return None, "count model: uses only total keyword volume and state (no per-keyword contributions)"
    steps = getattr(model, "steps", None)
    clf = steps[-1][1] if steps else model
    cls = type(clf).__name__
    if cls == "LogisticRegression":
        xt = model[:-1].transform(x) if steps and len(steps) > 1 else x
        xt = xt.toarray().ravel() if sp.issparse(xt) else np.asarray(xt).ravel()
        return pd.Series(xt * clf.coef_.ravel(), index=FEATS), "coefficient x preprocessed value (log-odds)"
    if cls == "LGBMClassifier" and not steps:
        c = clf.predict(x.toarray(), pred_contrib=True)[0, :-1]
        return pd.Series(c, index=FEATS), "exact TreeSHAP (LightGBM native, log-odds)"
    if cls == "XGBClassifier" and not steps:
        import xgboost as xgb
        c = clf.get_booster().predict(xgb.DMatrix(x.toarray()), pred_contribs=True)[0, :-1]
        return pd.Series(c, index=FEATS), "exact TreeSHAP (XGBoost native, log-odds)"
    # generic occlusion: drop in probability when one non-zero feature is set to 0
    base = predict(model, x, state)[0]
    nz = x.indices
    rows = sp.vstack([x] * len(nz)).tolil()
    for r, j in enumerate(nz):
        rows[r, j] = 0
    p = predict(model, rows.tocsr(), state) if len(nz) else np.array([])
    return pd.Series(base - p, index=[FEATS[j] for j in nz]), "occlusion: probability drop when the feature is set to 0"

def show_contrib(model, name, x, state, k=15):
    c, how = contributions(model, x, state)
    st.caption(f"{name}: {how}")
    if c is None or len(c) == 0 or np.allclose(c.values, 0):
        st.info("No per-keyword contributions to show for this input.")
        return
    aux = c[[i for i in c.index if str(i).startswith("aux_")]]
    if len(aux): st.caption(f"Sum of contributions from the 20 undocumented aux columns: {aux.sum():+.4f} (not shown below)")
    c = c[[i for i in c.index if not str(i).startswith("aux_")]]
    if len(c) == 0 or np.allclose(c.values, 0):
        st.info("No keyword contributions for this input (only aux columns contribute)."); return
    top = c[c != 0].abs().sort_values(ascending=False).head(k).index
    s = c[top][::-1]
    fig, ax = plt.subplots(figsize=(5, 0.32 * len(s) + 1))
    ax.barh(s.index, s.values, color=["#c05746" if v > 0 else "#2a6f97" for v in s.values])
    ax.axvline(0, color="k", lw=0.8); ax.set_xlabel("keyword contribution (red raises risk)")
    st.pyplot(fig, clear_figure=True)

def score_panel(x, state, label=""):
    c1, c2 = st.columns(2)
    for col, model, name in ((c1, M_STAT, NAME_STAT), (c2, M_ML, NAME_ML)):
        p = float(predict(model, x, state)[0])
        with col:
            st.metric(f"{name} ({'statistical' if model is M_STAT else 'machine learning'})", f"{p:.3f}",
                      help=f"Decision threshold tuned on training OOF predictions = {THR[name]:.3f}")
            st.write("Predicted class:", "**OUTBREAK**" if p >= THR[name] else "no outbreak", f"(threshold {THR[name]:.3f})")
            show_contrib(model, name, x, state)

def vector_from_counts(counts: dict, aux_mode: str):
    """Build a 1 x 545 csr from {keyword: count}. Aux columns: training median or zero."""
    v = np.zeros(len(FEATS))
    if aux_mode == "training median":
        v[:N_AUX] = meta.get("aux_train_median", [0] * N_AUX)
    for k, c in counts.items():
        if k in KW_SET:
            v[KW_SET[k]] += float(c)
    return sp.csr_matrix(v)

AUX_HELP = ("Columns 0-19 of the dataset are undocumented auxiliary features (monotone, cumulative-looking profiles). For "
            "manual or live input they are unknown, so they are either filled with the training median or set to zero.")

# ----------------------------------------------------------------------------------------------------------- layout
st.title("Twitter-based influenza outbreak risk: prototype")
st.markdown(f"Models from the ITRPA4 experiments: best statistical = **{NAME_STAT}**, best machine learning = **{NAME_ML}** "
            "(baseline models from the original comparison; the recommended calibrated ensemble in the test-set lookup was selected on the validation block only). Data: Zhao (2015), UCI, doi:10.24432/C5CP7V.")
tab1, tab2, tab3, tab4 = st.tabs(["Test-set lookup", "Upload / enter keyword counts", "Model comparison", "Live X signal dashboard (illustration)"])

# ---- Tab 1
with tab1:
    c1, c2 = st.columns([1, 2])
    with c1:
        state = st.selectbox("State", STATES, index=STATES.index("new york") if "new york" in STATES else 0)
        ts = TE_META.loc[TE_META.state == state, "t"].values
        t = st.slider("Test time step (index in the 1,580-step series; the test split starts at %d)" % meta["train_steps"],
                      int(ts.min()), int(ts.max()), int(ts.min()) + int(np.argmax(TE_META.loc[TE_META.state == state, "y"].values)) if TE_META.loc[TE_META.state == state, "y"].any() else int(ts.min()))
        row = int(np.where((TE_META.state == state) & (TE_META.t == t))[0][0])
        x = X_TE[row]
        st.write("True label:", "**OUTBREAK**" if TE_META.y[row] == 1 else "no outbreak")
        kw_counts = pd.Series(x.toarray().ravel()[N_AUX:], index=KEYWORDS)
        st.write("Non-zero keywords in this observation:", int((kw_counts > 0).sum()), "of", len(KEYWORDS))
        st.dataframe(kw_counts[kw_counts > 0].sort_values(ascending=False).head(15).rename("count"))
    with c2:
        score_panel(x, state)
        if IMP is not None:
            im = IMP["meta"]; ip = IMP["preds"]
            r_ = ip[(ip.state == state) & (ip.t == t)].iloc[0]
            st.markdown("---")
            st.metric(f"{im['name']} (recommended; lagged and rolling Twitter features, calibrated)", f"{r_.p_improved:.3f}",
                      help="Uses each state's keyword history up to this time step, so it is only available for the test-set lookup.")
            st.write(" | ".join(f"{op}: threshold {thr:.4f} -> {'**OUTBREAK**' if r_.p_improved >= thr else 'no outbreak'}"
                                for op, thr in im["operating_points"].items()))
            st.caption("Thresholds were chosen on the training-period validation block (steps 657-1094), never on the test split.")
    st.subheader(f"Predicted risk over the test period: {state}")
    d = PREDS[PREDS.state == state].sort_values("t")
    fig, ax = plt.subplots(figsize=(11, 3))
    ax.fill_between(d.t, 0, d.y, step="mid", color="#f3c9c1", label="true outbreak")
    ax.plot(d.t, d.p_stat, color="#2a6f97", label=NAME_STAT); ax.plot(d.t, d.p_ml, color="#c05746", label=NAME_ML)
    if IMP is not None:
        di = IMP["preds"][IMP["preds"].state == state].sort_values("t")
        ax.plot(di.t, di.p_improved, color="#6a4c93", lw=1.8, label=IMP["meta"]["name"] + " (calibrated)")
    ax.axvline(t, color="k", ls=":"); ax.set_ylim(0, 1.02); ax.set_xlabel("time step"); ax.set_ylabel("P(outbreak)"); ax.legend(fontsize=8)
    st.pyplot(fig, clear_figure=True)

# ---- Tab 2
with tab2:
    st.markdown("Enter keyword counts for **one state-week** in the dataset's vocabulary. Unknown words are ignored.")
    state2 = st.selectbox("State (used by count models only)", STATES, key="s2")
    aux_mode = st.radio("Auxiliary columns 0-19", ["training median", "zero"], horizontal=True, help=AUX_HELP)
    mode = st.radio("Input", ["Type counts", "Upload CSV"], horizontal=True)
    counts = {}
    if mode == "Type counts":
        txt = st.text_area("Counts as keyword=count, separated by commas or new lines", "flu=40, fever=6, sick=12, cough=5, influenza=3")
        for part in re.split(r"[,\n]+", txt):
            if "=" in part:
                k, v = part.split("=", 1)
                try: counts[k.strip().lower()] = float(v)
                except ValueError: st.warning(f"Could not read count in '{part.strip()}'")
    else:
        up = st.file_uploader("CSV: either columns keyword,count or one row with keyword names as columns", type="csv")
        if up is not None:
            df = pd.read_csv(up)
            if {"keyword", "count"} <= set(df.columns.str.lower()):
                df.columns = df.columns.str.lower(); counts = dict(zip(df.keyword.str.lower(), df["count"]))
            else:
                counts = {str(k).lower(): float(v) for k, v in df.iloc[0].items() if pd.notna(v)}
    known = {k: v for k, v in counts.items() if k in KW_SET}; unknown = [k for k in counts if k not in KW_SET]
    st.write(f"Recognised keywords: {len(known)}" + (f" | ignored (not in vocabulary): {', '.join(unknown)}" if unknown else ""))
    if known:
        score_panel(vector_from_counts(known, aux_mode), state2)

# ---- Tab 3
with tab3:
    st.subheader("Held-out test-set results (from the notebook)")
    cols = [c for c in ["family", "pr_auc", "roc_auc", "f1", "precision", "recall", "mcc", "balanced_acc", "brier", "threshold"] if c in RES.columns]
    st.dataframe(RES[cols].style.format({c: "{:.4f}" for c in cols if c != "family"}), width="stretch")
    c1, c2 = st.columns(2)
    with c1:
        fig, ax = plt.subplots(figsize=(6, 4))
        r = RES.sort_values("pr_auc")
        ax.barh(r.index, r.pr_auc, color=["#2a6f97" if f == "Statistical" else "#c05746" for f in r.family]); ax.set_xlabel("Test PR-AUC"); ax.set_xlim(0, 1)
        st.pyplot(fig, clear_figure=True)
    with c2:
        st.markdown("**Compute time (seconds)**"); st.dataframe(RT.round(3), width="stretch")
    st.markdown("**Post-hoc calibration (Brier score, lower is better)**")
    st.dataframe(CAL.pivot(index="model", columns="method", values="brier").round(5))
    if IMP is not None:
        st.subheader("Improved models and statistical validation (notebook section 14)")
        st.caption("All choices were made on a validation block from the end of the training period. Intervals: circular block bootstrap "
                   "(28-step blocks, 2,000 replicates, all states resampled together).")
        num = lambda df: {c: "{:.6f}" for c in df.columns if pd.api.types.is_float_dtype(df[c])}
        for k, ttl in (("improve_summary", "Validation and test results"), ("improve_bootstrap_ci", "95% block-bootstrap confidence intervals"),
                       ("improve_significance", "Paired significance tests"), ("improve_operating_points", "Operating points (chosen on validation)")):
            if IMP.get(k) is not None:
                with st.expander(ttl, expanded=(k == "improve_summary")):
                    st.dataframe(IMP[k].style.format(num(IMP[k]), na_rep=""), width="stretch")
    if os.path.isdir(FIGS):
        figs = sorted(f for f in os.listdir(FIGS) if f.endswith(".png"))
        pick = st.selectbox("Chapter 4 figure", figs, index=next((i for i, f in enumerate(figs) if "calibration_curves" in f), 0)) if figs else None
        if pick: st.image(os.path.join(FIGS, pick))

# ---- Tab 4: live dashboard
TOKEN = re.compile(r"#?([a-z0-9']+)")
def tokenize(text):
    """Lower-case word tokens; a leading '#' is stripped so hashtags (#flu) count as the keyword."""
    return TOKEN.findall(str(text).lower().replace("\u2019", "'"))

def keyword_counts(texts):
    c = {}
    for tx in texts:
        for tok in tokenize(tx):
            if tok in KW_SET: c[tok] = c.get(tok, 0) + 1
    return c

@st.cache_data
def load_live():
    out = {"posts": None, "counts": None, "overlap": None, "meta": {}, "errors": []}
    if os.path.exists(LIVE_POSTS):
        try:
            d = json.load(open(LIVE_POSTS))
            posts = d.get("posts", []) if isinstance(d, dict) else d
            out["meta"] = {k: v for k, v in d.items() if k != "posts"} if isinstance(d, dict) else {}
            if posts:
                df = pd.DataFrame(posts)
                df["created_at"] = pd.to_datetime(df.get("created_at"), utc=True, errors="coerce", format="ISO8601").dt.tz_convert("Africa/Johannesburg")
                df["date"] = df.created_at.dt.date
                df["query"] = df.get("query", pd.Series(["(unknown)"] * len(df))).fillna("(unknown)")
                df["matched_keywords"] = df.text.apply(lambda s: sorted({t for t in tokenize(s) if t in KW_SET}))
                out["posts"] = df
        except Exception as e:
            out["errors"].append(f"sample_live_posts.json could not be read: {e}")
    if os.path.exists(LIVE_COUNTS):
        try:
            d = json.load(open(LIVE_COUNTS))
            rows, summaries = [], []
            def rec_row(r, series, group):
                start = r.get("start") or r.get("day") or r.get("date")
                cnt = r.get("tweet_count", r.get("count"))
                return dict(group=group, series=series, start=start, count=cnt,
                            partial_day=bool(r.get("partial_day", False)),
                            lower_bound=(r.get("complete") is False))
            def walk(node, key, group):
                """Find every object holding a 'daily' list of buckets, at any depth (the file layout may change)."""
                if isinstance(node, dict):
                    if isinstance(node.get("daily"), list):
                        name = key if key not in (None, "queries") else node.get("query", "series")
                        rows.extend(rec_row(r, str(name), group) for r in node["daily"] if isinstance(r, dict))
                    for k, v in node.items():
                        if k != "daily": walk(v, k, group if group else k)
                elif isinstance(node, list):
                    if node and all(isinstance(r, dict) and ("tweet_count" in r or "count" in r) and ("start" in r or "date" in r or "day" in r) for r in node) and key != "daily":
                        rows.extend(rec_row(r, r.get("query", str(key)), group or str(key)) for r in node)
                    elif node and all(isinstance(r, dict) for r in node) and "summary" in str(key):
                        summaries.append((key, node))
            walk(d, None, None)
            if rows:
                cdf = pd.DataFrame(rows)
                cdf["start"] = pd.to_datetime(cdf.start, utc=True, errors="coerce", format="ISO8601")
                cdf["date"] = cdf.start.dt.date   # buckets are UTC days as returned by the API
                cdf["count"] = pd.to_numeric(cdf["count"], errors="coerce")
                out["counts"] = cdf.dropna(subset=["start", "count"]).drop_duplicates(["group", "series", "start"])
            out["counts_summaries"] = summaries
            out["counts_meta"] = {k: v for k, v in d.items() if isinstance(v, (str, int, float)) or k in ("limits", "window")} if isinstance(d, dict) else {}
        except Exception as e:
            out["errors"].append(f"live_daily_counts.json could not be read: {e}")
    if os.path.exists(LIVE_OVERLAP):
        try: out["overlap"] = json.load(open(LIVE_OVERLAP))
        except Exception as e: out["errors"].append(f"live_keyword_overlap.json could not be read: {e}")
    return out

with tab4:
    st.error("**Illustration only.** This dashboard uses a small sample of recent public X posts. It is **not** part of the "
             "evaluated dissertation results, which come only from the UCI dataset (Zhao, 2015). The live posts have no CDC "
             "outbreak labels, come from keyword searches rather than a geolocated state stream, and are on a different scale "
             "from the 2011-2015 training data. The model scores below show how the pipeline would run on live text. They are **not** outbreak forecasts.")
    L = load_live()
    for e in L["errors"]: st.warning(e)
    posts, cdf = L["posts"], L["counts"]
    if L["meta"].get("_placeholder"):
        st.info("sample_live_posts.json is the empty placeholder. Add real posts to enable this tab.")
    if posts is None and cdf is None:
        st.info("No live data files found (sample_live_posts.json, live_daily_counts.json). Put them next to app.py to enable this dashboard.")
    else:
        if L["meta"].get("source"): st.caption("Source: " + str(L["meta"]["source"]))
        # date range across both sources
        dates = []
        if posts is not None and posts.date.notna().any(): dates += [posts.date.min(), posts.date.max()]
        if cdf is not None and len(cdf): dates += [cdf.date.min(), cdf.date.max()]
        if not dates:
            st.warning("The live files contain no parseable dates."); st.stop()
        dmin, dmax = min(dates), max(dates)
        c1, c2, c3 = st.columns([2, 1, 1])
        rng = c1.date_input("Date range", (dmin, dmax), min_value=dmin, max_value=dmax)
        d0, d1 = (rng if isinstance(rng, (list, tuple)) and len(rng) == 2 else (dmin, dmax))
        view = c2.radio("View", ["Daily", "Weekly"], horizontal=True)
        aux_live = c3.radio("Aux columns", ["training median", "zero"], help=AUX_HELP)
        state_live = st.selectbox("State assumed for count models", STATES, index=STATES.index("new york") if "new york" in STATES else 0,
                                  help="Live posts are not geolocated. This only affects count-GLM models.")

        def period(dser):
            ds = pd.to_datetime(pd.Series(dser))
            return (ds.dt.to_period("W-SUN").dt.start_time.dt.date if view == "Weekly" else ds.dt.date).values

        # --- 1. volume trend
        st.subheader("1. Post volume trend (X counts / paginated search)")
        if cdf is not None and len(cdf):
            cm = L.get("counts_meta", {})
            with st.expander("Notes on the counts data (coverage and limits)"):
                st.json(cm)
            c = cdf[(cdf.date >= d0) & (cdf.date <= d1)].copy()
            g1, g2 = st.columns([1, 2])
            groups = sorted(c.group.dropna().unique())
            gsel = g1.multiselect("Source group", groups, default=groups)
            excl = g1.checkbox("Exclude partial-day buckets", value=True)
            lb = g1.checkbox("Include lower-bound days (incomplete pagination)", value=True,
                             help="Some days only have a lower bound because not every result page was retrieved. Missing days are left as gaps; no values are filled in.")
            if gsel: c = c[c.group.isin(gsel)]
            if excl: c = c[~c.partial_day]
            if not lb: c = c[~c.lower_bound]
            c["period"] = period(c.date)
            pv = c.groupby(["period", "series"])["count"].sum(min_count=1).unstack("series").sort_index()
            default_q = [q for q in pv.columns if q in ("flu", "influenza", "fever", "flu_season", "flu_shot", "sore_throat")] or list(pv.columns)[:6]
            qsel = g2.multiselect("Series", list(pv.columns), default=default_q)
            if qsel and len(pv):
                fig, ax = plt.subplots(figsize=(11, 3.8))
                for qn in qsel: ax.plot(pd.to_datetime(pv.index), pv[qn], "o-", ms=3, label=qn)
                ax.set_ylabel(f"posts per {'week (Mon-Sun)' if view == 'Weekly' else 'day (UTC)'}"); ax.legend(fontsize=7, ncol=3)
                if view == "Weekly": ax.set_title("Weekly totals: incomplete weeks and missing days make totals lower bounds", fontsize=9)
                fig.autofmt_xdate(); st.pyplot(fig, clear_figure=True)
                st.dataframe(pv[qsel].round(0), width="stretch")
                nlb = int(c[c.series.isin(qsel)].lower_bound.sum())
                if nlb: st.caption(f"{nlb} of the plotted daily buckets are lower bounds (incomplete pagination).")
            for key, summ in L.get("counts_summaries", []):
                with st.expander(f"Summary table from the data file: {key}"):
                    st.dataframe(pd.DataFrame(summ), width="stretch")
        else:
            st.info("live_daily_counts.json not found or has no daily buckets. Volume trend unavailable.")

        if posts is not None:
            p = posts[(posts.date >= d0) & (posts.date <= d1)].copy()
            if len(p):
                pc = p.assign(period=period(p.date)).groupby("period").size()
                fig, ax = plt.subplots(figsize=(11, 2.4)); ax.bar(pd.to_datetime(pc.index), pc.values, width=5 if view == "Weekly" else 0.8, color="#9aa5b1")
                ax.set_ylabel("sampled posts"); ax.set_title(f"Sampled posts per {'week' if view == 'Weekly' else 'day'} (the sample, not total volume)", fontsize=9)
                fig.autofmt_xdate(); st.pyplot(fig, clear_figure=True)
            st.write(f"Posts in range: **{len(p)}** of {len(posts)} | with at least one dataset keyword: **{int((p.matched_keywords.str.len() > 0).sum())}**")
            # --- 2. keyword overlap
            st.subheader("2. Dataset keywords matched in live posts")
            kc = pd.Series(keyword_counts(p.text)).sort_values(ascending=False) if len(p) else pd.Series(dtype=float)
            topn = st.slider("Top N keywords", 5, 50, 20)
            if len(kc):
                st.write(f"{len(kc)} of {len(KEYWORDS)} dataset keywords appear in the selected posts.")
                s = kc.head(topn)[::-1]
                fig, ax = plt.subplots(figsize=(9, 0.22 * len(s) + 1)); ax.barh(s.index, s.values, color="#2a6f97"); ax.set_xlabel("occurrences")
                st.pyplot(fig, clear_figure=True)
            if L["overlap"] and isinstance(L["overlap"], dict):
                with st.expander("Pre-computed overlap summary (live_keyword_overlap.json, full sample)"):
                    st.json({k: v for k, v in L["overlap"].items() if not isinstance(v, list)})
            # --- 3. keyword-vector scores
            st.subheader("3. Keyword-count vector scored by both models")
            st.caption("Posts in each period are tokenised and counted against the 525 dataset keywords, then summed into one keyword-count vector per period and scored. "
                       "The sample holds tens of posts per period, while a state-week in the training data held many more tweets, so absolute probabilities are not meaningful.")
            p["period"] = period(p.date)
            rows = []
            for per, g in p.groupby("period"):
                v = vector_from_counts(keyword_counts(g.text), aux_live)
                rows.append(dict(period=per, posts=len(g), keyword_tokens=int(v[:, N_AUX:].sum()),
                                 **{NAME_STAT: float(predict(M_STAT, v, state_live)[0]), NAME_ML: float(predict(M_ML, v, state_live)[0])}))
            sc = pd.DataFrame(rows)
            if len(sc):
                fig, ax = plt.subplots(figsize=(11, 3.5))
                ax.plot(pd.to_datetime(sc.period), sc[NAME_STAT], "o-", color="#2a6f97", label=NAME_STAT)
                ax.plot(pd.to_datetime(sc.period), sc[NAME_ML], "o-", color="#c05746", label=NAME_ML)
                ax.set_ylim(0, 1.02); ax.set_ylabel("model score"); ax.legend(fontsize=8)
                ax.set_title(f"{view} keyword-vector score trend (illustration)", fontsize=9)
                st.pyplot(fig, clear_figure=True)
                st.dataframe(sc.style.format({NAME_STAT: "{:.4f}", NAME_ML: "{:.4f}"}), width="stretch")
            st.markdown("**Whole selected range as one vector**")
            if len(p):
                score_panel(vector_from_counts(keyword_counts(p.text), aux_live), state_live)
            # --- 4. post table
            st.subheader("4. Browse posts")
            f1, f2, f3 = st.columns([2, 2, 2])
            txt = f1.text_input("Text contains")
            qs = f2.multiselect("Query", sorted(p["query"].unique()))
            kws = f3.multiselect("Matched dataset keyword", list(kc.index[:200]))
            t = p
            if txt: t = t[t.text.str.contains(txt, case=False, regex=False)]
            if qs: t = t[t["query"].isin(qs)]
            if kws: t = t[t.matched_keywords.apply(lambda m: any(k in m for k in kws))]
            show = t[["created_at", "query", "text", "matched_keywords"] + (["url"] if "url" in t.columns else [])].sort_values("created_at", ascending=False)
            show = show.assign(created_at=show.created_at.dt.strftime("%Y-%m-%d %H:%M SAST"), matched_keywords=show.matched_keywords.str.join(", "))
            st.write(f"{len(show)} posts")
            st.dataframe(show, width="stretch", height=400)
        else:
            st.info("sample_live_posts.json not found or empty. Keyword overlap, scores and the post table are unavailable.")
