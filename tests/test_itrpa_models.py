"""Unit tests for the functions and classes in itrpa_models.py."""
import numpy as np
import pytest
import scipy.sparse as sp

from itrpa_models import BayesLogRegPosterior, CountGLMClassifier, sparse_log1p


def test_sparse_log1p_keeps_csr_sparse_and_applies_log1p():
    X = sp.csr_matrix(np.array([[0.0, 1.0, 0.0], [3.0, 0.0, 8.0]]))
    Y = sparse_log1p(X)
    assert sp.issparse(Y)
    assert Y.shape == X.shape
    assert Y.nnz == X.nnz
    np.testing.assert_allclose(Y.data, np.log1p(X.data))
    # original matrix is not modified
    np.testing.assert_array_equal(X.data, np.array([1.0, 3.0, 8.0]))


def test_sparse_log1p_dense():
    X = np.array([[0.0, 1.0], [3.0, 8.0]])
    Y = sparse_log1p(X)
    np.testing.assert_allclose(Y, np.log1p(X))
    assert Y.dtype == np.float64


def test_sparse_log1p_zero_matrix_stays_empty():
    X = sp.csr_matrix((4, 6), dtype=np.float64)
    Y = sparse_log1p(X)
    assert Y.nnz == 0
    assert Y.shape == (4, 6)


@pytest.mark.parametrize("family", ["poisson", "nb"])
def test_count_glm_classifier_fit_predict_proba(family):
    rng = np.random.default_rng(42)
    n, n_states, n_aux, n_kw = 240, 4, 20, 5
    state_idx = rng.integers(0, n_states, size=n)
    y = rng.integers(0, 2, size=n).astype(float)
    # Higher keyword volume when y=1, so the generative model has a signal.
    lam = np.where(y == 1, 18.0, 4.0)
    counts = rng.poisson(lam)
    X = np.zeros((n, n_aux + n_kw), dtype=np.float64)
    X[:, n_aux] = counts

    clf = CountGLMClassifier(family="poisson" if family == "poisson" else "nb", n_aux=n_aux)
    clf.fit(X, y, state_idx, n_states)
    proba = clf.predict_proba(X, state_idx)

    assert proba.shape == (n, 2)
    assert np.all(np.isfinite(proba))
    assert np.all(proba >= 0.0) and np.all(proba <= 1.0)
    np.testing.assert_allclose(proba.sum(axis=1), 1.0, atol=1e-10)
    # Observations with larger counts should tend to get a higher outbreak probability.
    p = proba[:, 1]
    assert p[counts >= 15].mean() > p[counts <= 5].mean()


def test_count_glm_classifier_accepts_sparse_X():
    rng = np.random.default_rng(0)
    n, n_states, n_aux = 80, 3, 20
    state_idx = rng.integers(0, n_states, size=n)
    y = rng.integers(0, 2, size=n).astype(float)
    X = np.zeros((n, n_aux + 3), dtype=np.float64)
    X[:, n_aux] = rng.poisson(np.where(y == 1, 10.0, 3.0))
    clf = CountGLMClassifier(family="poisson", n_aux=n_aux)
    clf.fit(sp.csr_matrix(X), y, state_idx, n_states)
    proba = clf.predict_proba(sp.csr_matrix(X), state_idx)
    assert proba.shape == (n, 2)
    np.testing.assert_allclose(proba.sum(axis=1), 1.0, atol=1e-10)


def test_bayes_logreg_posterior_predict_proba_and_draws():
    n, p, n_sel, n_draws = 12, 8, 4, 25
    selected_idx = np.arange(n_sel)
    mu = np.zeros(n_sel)
    sd = np.ones(n_sel)
    a_draws = np.zeros(n_draws)
    b_draws = np.full((n_draws, n_sel), 0.4)
    names = [f"f{i}" for i in range(n_sel)]
    model = BayesLogRegPosterior(selected_idx, mu, sd, a_draws, b_draws, names)

    X = np.ones((n, p), dtype=np.float64)
    proba = model.predict_proba(X)
    assert proba.shape == (n, 2)
    assert np.all((proba >= 0.0) & (proba <= 1.0))
    np.testing.assert_allclose(proba.sum(axis=1), 1.0, atol=1e-10)

    proba2, draws = model.predict_proba(X, return_draws=True)
    np.testing.assert_allclose(proba2, proba)
    assert draws.shape == (n, n_draws)
    assert np.all((draws >= 0.0) & (draws <= 1.0))
    np.testing.assert_allclose(model.coef_mean, np.full(n_sel, 0.4))


def test_bayes_logreg_posterior_transform_matches_log1p_standardise():
    selected_idx = np.array([1, 3])
    mu = np.array([0.0, 1.0])
    sd = np.array([1.0, 2.0])
    model = BayesLogRegPosterior(
        selected_idx, mu, sd, np.zeros(3), np.zeros((3, 2)), ["a", "b"]
    )
    X = np.array([[0.0, 1.0, 0.0, 3.0, 0.0]])
    Z = model.transform(X)
    expected = (np.log1p(np.array([[1.0, 3.0]])) - mu) / sd
    np.testing.assert_allclose(Z, expected)

    Z_sparse = model.transform(sp.csr_matrix(X))
    np.testing.assert_allclose(Z_sparse, expected)
