"""Smoke tests for the Streamlit prototype (app.py) without starting a server."""
import ast
import importlib
import json
import sys
import types
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
APP_PATH = REPO / "prototype" / "app.py"


def test_app_py_parses():
    source = APP_PATH.read_text(encoding="utf-8")
    ast.parse(source)
    assert "streamlit" in source
    compile(source, str(APP_PATH), "exec")



class _Widgets:
    """Widget methods shared by the top-level stub and column/tab context objects."""

    def _identity_decorator(self, fn=None, **kwargs):
        def _wrap(f):
            return f

        return _wrap if fn is None else fn

    def cache_resource(self, fn=None, **kwargs):
        return self._identity_decorator(fn, **kwargs)

    def cache_data(self, fn=None, **kwargs):
        return self._identity_decorator(fn, **kwargs)

    def fragment(self, fn=None, **kwargs):
        return self._identity_decorator(fn, **kwargs)

    def cache(self, fn=None, **kwargs):
        return self._identity_decorator(fn, **kwargs)

    def set_page_config(self, *a, **k):
        return None

    def tabs(self, labels):
        return [_Ctx() for _ in labels]

    def columns(self, spec):
        n = spec if isinstance(spec, int) else len(spec)
        return [_Ctx() for _ in range(n)]

    def expander(self, *a, **k):
        return _Ctx()

    def selectbox(self, label, options, index=0, **k):
        options = list(options)
        return options[index] if options else None

    def slider(self, label, min_value=None, max_value=None, value=None, **k):
        if value is not None:
            return value
        return min_value

    def radio(self, label, options, **k):
        return list(options)[0]

    def text_area(self, label, value="", **k):
        return value

    def text_input(self, *a, **k):
        return k.get("value", "")

    def file_uploader(self, *a, **k):
        return None

    def date_input(self, label, value=None, **k):
        return value

    def multiselect(self, label, options, default=None, **k):
        if default is not None:
            return list(default)
        return list(options)

    def checkbox(self, label, value=False, **k):
        return value

    def number_input(self, label, **k):
        return k.get("value", k.get("min_value", 0))

    def stop(self):
        raise RuntimeError("st.stop() called during import")

    def __getattr__(self, name):
        def _noop(*a, **k):
            return None

        return _noop


class _Ctx(_Widgets):
    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


class _StreamlitStub(_Widgets):
    """Minimal Streamlit stand-in so app.py can be imported outside `streamlit run`."""

    def sidebar(self):
        return _Ctx()


@pytest.fixture(scope="module")
def app_module():
    stub = _StreamlitStub()
    sys.modules["streamlit"] = stub
    proto = str(REPO / "prototype")
    sys.path.insert(0, proto)
    if "app" in sys.modules:
        del sys.modules["app"]
    try:
        import app as mod
        if not isinstance(sys.modules.get("streamlit"), _StreamlitStub):
            sys.modules["streamlit"] = stub
            mod = importlib.reload(mod)
        return mod
    finally:
        if sys.path and sys.path[0] == proto:
            sys.path.pop(0)


def test_app_imports_and_loads_artifacts(app_module):
    assert app_module.M_STAT is not None
    assert app_module.M_ML is not None
    assert app_module.X_TE.shape[0] == len(app_module.TE_META)
    assert app_module.NAME_STAT == "LogReg-L1"
    assert app_module.NAME_ML == "LightGBM"
    assert app_module.IMP is not None


def test_app_predict_and_vector_helpers(app_module):
    # One test-set row
    x = app_module.X_TE[0]
    state = app_module.TE_META.iloc[0]["state"]
    p = app_module.predict(app_module.M_STAT, x, state)
    assert p.shape == (1,)
    assert 0.0 <= float(p[0]) <= 1.0

    vec = app_module.vector_from_counts({"flu": 4, "fever": 2, "not_a_keyword": 9}, "zero")
    assert vec.shape == (1, len(app_module.FEATS))
    # unknown keyword is ignored; two known keywords are stored past the aux block
    assert int(vec[:, app_module.N_AUX :].sum()) == 6


def test_app_tokenize_counts_hashtags_as_keywords(app_module):
    tokens = app_module.tokenize("I have the #flu and a fever")
    assert "flu" in tokens and "fever" in tokens
    counts = app_module.keyword_counts(["got the flu", "flu and cough", "#flu"])
    assert counts["flu"] == 3
    assert counts.get("cough") == 1


def test_sanitised_live_posts_have_no_handles_or_ids(prototype_dir):
    """Repo copies of the live-post samples must not contain real X usernames, tweet IDs or status URLs."""
    import re

    handle = re.compile(r"(?<!\w)@([A-Za-z0-9_]{1,15})\b")
    for name in ("sample_live_posts.json", "sample_live_posts_filtered_out.json"):
        data = json.loads((prototype_dir / name).read_text())
        posts = data["posts"]
        assert len(posts) > 0
        for post in posts:
            assert "id" not in post
            assert "url" not in post
            assert "place" not in post
            for mention in handle.findall(post.get("text") or ""):
                assert mention.lower() == "user", f"non-anonymised handle @{mention} in {name}"
