"""Load saved prototype models and check predictions on X_test.npz."""
import json

import joblib
import numpy as np
import pandas as pd
import pytest
import scipy.sparse as sp

import itrpa_models  # noqa: F401  — required so joblib can unpickle custom classes


@pytest.fixture(scope="module")
def x_test(artifacts_dir):
    path = artifacts_dir / "X_test.npz"
    X = sp.csr_matrix(sp.load_npz(path))
    return X


@pytest.fixture(scope="module")
def saved_predictions(artifacts_dir):
    return pd.read_csv(artifacts_dir / "test_predictions.csv")


def test_x_test_shape(x_test):
    assert x_test.shape == (23280, 545)
    assert x_test.format == "csr"


def test_best_stat_and_ml_models_predict_on_x_test(artifacts_dir, x_test, saved_predictions):
    meta = json.loads((artifacts_dir / "meta.json").read_text())
    m_stat = joblib.load(artifacts_dir / "best_stat_model.joblib")
    m_ml = joblib.load(artifacts_dir / "best_ml_model.joblib")

    p_stat = m_stat.predict_proba(x_test)[:, 1]
    p_ml = m_ml.predict_proba(x_test)[:, 1]

    n = x_test.shape[0]
    assert p_stat.shape == (n,)
    assert p_ml.shape == (n,)
    assert np.all(np.isfinite(p_stat)) and np.all(np.isfinite(p_ml))
    assert np.all((p_stat >= 0.0) & (p_stat <= 1.0))
    assert np.all((p_ml >= 0.0) & (p_ml <= 1.0))

    # Predictions should match the values written by the notebook (within float tolerance).
    assert len(saved_predictions) == n
    np.testing.assert_allclose(p_stat, saved_predictions["p_stat"].to_numpy(), atol=1e-5, rtol=1e-4)
    np.testing.assert_allclose(p_ml, saved_predictions["p_ml"].to_numpy(), atol=1e-5, rtol=1e-4)

    assert meta["best_stat"] == "LogReg-L1"
    assert meta["best_ml"] == "LightGBM"


def test_improved_member_models_load(artifacts_dir):
    """Improved ensemble members load; they use temporal features, so they are not scored on X_test.npz."""
    m1 = joblib.load(artifacts_dir / "improved_member1.joblib")
    m2 = joblib.load(artifacts_dir / "improved_member2.joblib")
    assert m1 is not None and m2 is not None
    meta = json.loads((artifacts_dir / "improved_meta.json").read_text())
    assert "Ensemble" in meta["name"]
    assert set(meta["member_files"].values()) == {
        "improved_member1.joblib",
        "improved_member2.joblib",
    }
