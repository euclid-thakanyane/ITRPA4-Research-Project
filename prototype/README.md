# ITRPA4 Prototype: Twitter-based Influenza Outbreak Risk Explorer

A Streamlit app built on the models trained in `../itrpa_experiments.ipynb` for the mini dissertation
*Predicting Epidemic Outbreaks from Sparse Twitter Data: Statistical vs. Machine Learning Approaches*.

## Run it

```bash
cd prototype
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py                                     # opens http://localhost:8501
```

The saved models in `artifacts/` were produced by the notebook. To regenerate them, run the notebook from the project root
(it writes `prototype/artifacts/` and `prototype/itrpa_models.py`). Use the same major versions of scikit-learn, LightGBM
and XGBoost as `requirements.txt` so the pickled models load.

## What it does

| Tab | Purpose |
|---|---|
| **Test-set lookup** | Pick a state and a time step from the held-out UCI test split. Shows the true label, the outbreak probability from the **best statistical model** and the **best ML model** (chosen by test PR-AUC in the notebook), the predicted class at the threshold tuned on training data, the top contributing keywords, and the risk curve for that state over the test period. |
| **Improved model (test-set lookup and model comparison)** | If `artifacts/improved_meta.json` exists (written by notebook section 14), the test-set lookup also shows the calibrated probability from the recommended improved model (lagged and rolling Twitter features), its class at the three operating points chosen on the training-period validation block (best F1, best MCC, early warning), and its risk curve. The model comparison tab adds the validation/test table, block-bootstrap confidence intervals and paired significance tests. Temporal features need each state's keyword history, so this model is not used for manually entered counts or the live dashboard. |
| **Upload / enter keyword counts** | Type `keyword=count` pairs or upload a CSV (`keyword,count` columns, or one row with keyword names as headers). Words outside the 525-keyword vocabulary are listed and ignored. |
| **Model comparison** | The full test-set metric table (PR-AUC, ROC-AUC, F1, precision, recall, MCC, balanced accuracy, Brier score), compute times, post-hoc calibration results, and a viewer for the Chapter 4 figures in `../figures/`. |
| **Live X signal dashboard (illustration)** | See below. |

### How contributions are computed
* Logistic regression: coefficient × preprocessed feature value (log-odds scale).
* Bayesian horseshoe LR: posterior-mean coefficient × standardised log1p value.
* LightGBM / XGBoost: exact TreeSHAP from the libraries' native `pred_contrib(s)`.
* Random Forest / MLP: occlusion, i.e. the drop in probability when each non-zero feature is set to 0.
* Poisson / Negative-Binomial count models use only total keyword volume and state, so they have no per-keyword contributions.

The dataset matrix has 545 columns, but only 525 keywords are documented. Columns 0–19 (`aux_00`–`aux_19`) are undocumented,
monotone, cumulative-looking features. Their summed contribution is shown separately, and they are hidden from the keyword
bar charts. For manual or live input their values are unknown, so you choose whether to fill them with the **training median**
or **zero**. This choice changes the scores.

## Live X signal dashboard (illustration only)

**Not part of the evaluated dissertation results.** It shows how the trained pipeline could be pointed at current social-media text.

Input files sit next to `app.py`. Each one is optional, and the tab degrades gracefully if a file is missing or empty:

| File | Expected content |
|---|---|
| `sample_live_posts.json` | `{"source": ..., "posts": [{"created_at", "text", "query", "url"?}, ...]}` (a bare list of posts also works) |
| `live_daily_counts.json` | Any JSON where daily series appear as objects with a `"daily"` list of buckets `{"start"/"day"/"date", "tweet_count"/"count", "partial_day"?, "complete"?}`, at any depth. Each series is named by its key and grouped by its top-level key (for example `official_7_day`, `outbreak_signals_30_day_from_paginated_search`). Buckets with `complete: false` are flagged as lower bounds. Lists whose key contains "summary" are shown as tables. |
| `live_keyword_overlap.json` | Pre-computed overlap summary (shown in an expander) |

Features:
1. **Date-range filter** and a **Daily / Weekly** view (weeks run Monday to Sunday; the first and last weeks may be incomplete).
   It handles any range, for example the 30-day window.
2. **Post-volume trend** per series, with filters for source group and series, an option to drop partial-day buckets, and an option to include or exclude lower-bound days.
   Days with no data are left as gaps and never filled in. Buckets are UTC days as the API returns them. A second chart shows how many **sampled posts** fall in each day or week.
3. **Dataset keywords matched** in the selected posts, as a top-N bar chart.
4. **Keyword-count vector scoring:** posts are lower-cased and tokenised (`[a-z0-9']+`, with a leading `#` stripped so `#flu` counts as `flu`),
   counted against the 525 dataset keywords, and summed into **one keyword-count vector per day or per week**. Each vector is scored by both saved models,
   giving a daily or weekly score trend. The whole selected range is also scored as a single vector, with keyword contributions.
5. **Browsable post table** with filters for text, query and matched keyword. Times are shown in SAST.

Why the scores are not forecasts:
* The live posts have no CDC outbreak labels, so nothing can be evaluated.
* They come from keyword searches (which already select flu talk), not a geolocated state stream like the training data.
* Volume is on a different scale: a few dozen sampled posts per day versus all tweets in a state-week in 2011–2015.
* The aux columns are unknown (see above).
* The count models need a state, which the live posts do not have, so the state you select is an assumption.

## Saved models
Best statistical = **LogReg-L1** (test PR-AUC 0.3761) and best ML = **LightGBM** (test PR-AUC 0.3823), chosen by test PR-AUC in the notebook run.

## Files
* `app.py`: the Streamlit app
* `itrpa_models.py`: custom classes and functions (count GLM classifier, Bayesian posterior wrapper, sparse log1p) needed to load the models
* `artifacts/`: `best_stat_model.joblib`, `best_ml_model.joblib`, `meta.json` (names, thresholds, keyword list), `X_test.npz`, `test_meta.csv`,
  `test_predictions.csv`, `test_results.csv`, `runtime.csv`, `calibration_posthoc.csv`
* `sample_live_posts.json`, `live_daily_counts.json`, `live_keyword_overlap.json` (and `sample_live_posts_filtered_out.json`): live X data written by a separate collection step (illustration only)
* `requirements.txt`
* `screenshot.png` (test-set lookup), `screenshot_model_comparison.png`, `screenshot_live_dashboard.png`: the app running headless (Playwright)

## Anonymisation of the live-post sample

`sample_live_posts.json` and `sample_live_posts_filtered_out.json` are for the illustration tab only.
Usernames/handles were already replaced with `@user` and author IDs were not retained in the original sample.
The copies in this repository additionally have tweet IDs, status URLs and place metadata removed so posts cannot be looked up. Post text and timestamps are kept because the dashboard uses them.
