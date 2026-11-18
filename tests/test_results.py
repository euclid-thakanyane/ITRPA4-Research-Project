"""Schema and key-value checks on the notebook results CSVs."""
import pandas as pd
import pytest

# Values quoted in the dissertation / prototype README, from the saved notebook run.
LIGHTGBM_TEST_PR_AUC = 0.3823
LOGREG_L1_TEST_PR_AUC = 0.3761
ENSEMBLE_TEST_PR_AUC = 0.494325


def test_test_results_columns_and_key_pr_auc(results_dir):
    df = pd.read_csv(results_dir / "test_results.csv", index_col=0)
    expected = {
        "family",
        "pr_auc",
        "roc_auc",
        "f1",
        "precision",
        "recall",
        "mcc",
        "balanced_acc",
        "accuracy",
        "brier",
        "threshold",
    }
    assert expected.issubset(df.columns)
    assert "LightGBM" in df.index and "LogReg-L1" in df.index
    assert df.loc["LightGBM", "pr_auc"] == pytest.approx(LIGHTGBM_TEST_PR_AUC, abs=5e-5)
    assert df.loc["LogReg-L1", "pr_auc"] == pytest.approx(LOGREG_L1_TEST_PR_AUC, abs=5e-5)
    # Rounded to 4 d.p. as reported in the prototype README.
    assert round(float(df.loc["LightGBM", "pr_auc"]), 4) == LIGHTGBM_TEST_PR_AUC
    assert round(float(df.loc["LogReg-L1", "pr_auc"]), 4) == LOGREG_L1_TEST_PR_AUC


def test_improve_summary_ensemble_pr_auc(results_dir):
    df = pd.read_csv(results_dir / "improve_summary.csv")
    expected = {
        "model",
        "feature_set",
        "test_pr_auc_calibrated",
        "val_pr_auc_calibrated",
        "calibration",
    }
    assert expected.issubset(df.columns)
    ens = df[df["model"].str.contains("Ensemble", regex=False)]
    assert len(ens) == 1, "expected exactly one improved ensemble row"
    value = float(ens["test_pr_auc_calibrated"].iloc[0])
    assert value == pytest.approx(ENSEMBLE_TEST_PR_AUC, abs=5e-7)
    assert round(value, 6) == ENSEMBLE_TEST_PR_AUC


def test_results_csvs_are_readable_with_expected_columns(results_dir):
    required = {
        "test_results.csv": {"pr_auc", "roc_auc", "family"},
        "improve_summary.csv": {"model", "test_pr_auc_calibrated"},
        "improve_bootstrap_ci.csv": {"model", "metric", "ci_low", "ci_high"},
        "temporal_cv_summary.csv": {"model", "temporal_cv_pr_auc_mean", "test_pr_auc"},
        "imbalance_by_split.csv": {"n", "positives", "prevalence"},
        "per_state_pr_auc.csv": {"state", "LogReg-L1", "LightGBM"},
        "calibration_posthoc.csv": {"model", "method", "brier"},
    }
    for name, cols in required.items():
        df = pd.read_csv(results_dir / name)
        assert cols.issubset(df.columns), f"{name} missing columns: {cols - set(df.columns)}"
        assert len(df) > 0


def test_prototype_artifact_csvs_match_results(artifacts_dir, results_dir):
    """Copies under prototype/artifacts/ should match the notebook results/ tables."""
    for name in ("test_results.csv", "improve_summary.csv"):
        a = pd.read_csv(artifacts_dir / name)
        b = pd.read_csv(results_dir / name)
        pd.testing.assert_frame_equal(a, b)
