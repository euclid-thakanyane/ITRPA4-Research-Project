"""No-leakage check: the official train/test split is temporal, not random."""
import json

import pandas as pd


def test_test_timesteps_are_after_training_period(artifacts_dir, results_dir):
    meta = json.loads((artifacts_dir / "meta.json").read_text())
    train_steps = int(meta["train_steps"])
    te = pd.read_csv(artifacts_dir / "test_meta.csv")

    assert {"state", "t", "y"}.issubset(te.columns)
    assert train_steps == 1095
    # Time index is 0-based over 1,580 steps; training uses t = 0..1094, test starts at 1095.
    assert int(te["t"].min()) == train_steps
    assert (te["t"] >= train_steps).all()
    assert int(te["t"].max()) == 1579  # 1095 + 485 - 1

    # Every state uses the same later window; no state has a test row from the training period.
    for state, g in te.groupby("state"):
        assert g["t"].min() >= train_steps, f"{state} has a test row in the training period"
        assert not (g["t"] < train_steps).any()

    n_states = te["state"].nunique()
    n_test_steps = int(te["t"].max()) - train_steps + 1
    assert n_states == 48
    assert n_test_steps == 485
    assert len(te) == n_states * n_test_steps

    imb = pd.read_csv(results_dir / "imbalance_by_split.csv", index_col=0)
    assert int(imb.loc["train", "n"]) == n_states * train_steps
    assert int(imb.loc["test", "n"]) == len(te)
    assert int(imb.loc["all", "n"]) == int(imb.loc["train", "n"]) + int(imb.loc["test", "n"])


def test_validation_block_is_inside_training_period(artifacts_dir):
    """Section 14 tunes on steps 657-1094, which are still before the test split."""
    meta = json.loads((artifacts_dir / "improved_meta.json").read_text())
    train_steps = json.loads((artifacts_dir / "meta.json").read_text())["train_steps"]
    # The note records the validation window explicitly.
    assert "657-1094" in meta["note"]
    val_end = 1094
    assert val_end < train_steps
