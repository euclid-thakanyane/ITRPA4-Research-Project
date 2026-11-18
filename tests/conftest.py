import os

os.environ.setdefault("MPLBACKEND", "Agg")

"""Shared paths and fixtures for the ITRPA4 thesis tests."""
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
PROTOTYPE = ROOT / "prototype"
ARTIFACTS = PROTOTYPE / "artifacts"
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"


@pytest.fixture(scope="session")
def repo_root() -> Path:
    return ROOT


@pytest.fixture(scope="session")
def artifacts_dir() -> Path:
    return ARTIFACTS


@pytest.fixture(scope="session")
def results_dir() -> Path:
    return RESULTS


@pytest.fixture(scope="session")
def prototype_dir() -> Path:
    return PROTOTYPE
