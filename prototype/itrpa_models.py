"""Custom model classes shared by the notebook and the Streamlit prototype (so joblib can unpickle them)."""
import numpy as np
from scipy import stats
from scipy.special import expit
import scipy.sparse as sp

def sparse_log1p(X):
    """log(1+x) that keeps sparse matrices sparse (module-level so pipelines can be pickled)."""
    if sp.issparse(X):
        X = X.copy().astype(np.float64); X.data = np.log1p(X.data); return X
    return np.log1p(np.asarray(X, dtype=np.float64))

class CountGLMClassifier:
    """Generative count classifier: total keyword count ~ Poisson/NB(mu(state, y)); posterior P(y=1|count, state)."""
    def __init__(self, family="poisson", n_aux=20):
        self.family, self.n_aux = family, n_aux
    def _design(self, state_idx, yflag):
        D = np.zeros((len(state_idx), self.n_states_ + 1)); D[np.arange(len(state_idx)), state_idx] = 1; D[:, -1] = yflag
        return D
    def fit(self, X, y, state_idx, n_states):
        import statsmodels.api as sm
        self.n_states_ = n_states
        c = np.asarray(X[:, self.n_aux:].sum(1)).ravel()
        D = self._design(state_idx, y)
        if self.family == "poisson":
            self.res_ = sm.GLM(c, D, family=sm.families.Poisson()).fit()
            self.params_, self.alpha_ = np.asarray(self.res_.params), None
        else:
            start = np.r_[np.asarray(sm.GLM(c, D, family=sm.families.Poisson()).fit().params), 1.0]
            self.res_ = sm.NegativeBinomial(c, D).fit(start_params=start, method="bfgs", disp=0, maxiter=2000)
            self.params_, self.alpha_ = np.asarray(self.res_.params[:-1]), float(self.res_.params[-1])
        self.prior_ = float(np.mean(y))
        return self
    def _logpmf(self, c, mu):
        if self.family == "poisson":
            return stats.poisson.logpmf(c, mu)
        n = 1.0 / self.alpha_; p = n / (n + mu)
        return stats.nbinom.logpmf(c, n, p)
    def predict_proba(self, X, state_idx):
        c = np.round(np.asarray(X[:, self.n_aux:].sum(1)).ravel())
        mu1 = np.exp(self._design(state_idx, 1) @ self.params_); mu0 = np.exp(self._design(state_idx, 0) @ self.params_)
        lo = self._logpmf(c, mu1) - self._logpmf(c, mu0) + np.log(self.prior_ / (1 - self.prior_))
        p = expit(lo); return np.c_[1 - p, p]

class BayesLogRegPosterior:
    """Bayesian logistic regression summarised by posterior draws. Preprocessing: log1p -> chi2 selection -> standardise."""
    def __init__(self, selected_idx, mu, sd, a_draws, b_draws, feature_names):
        self.selected_idx, self.mu, self.sd = np.asarray(selected_idx), mu, sd
        self.a_draws, self.b_draws, self.feature_names = a_draws, b_draws, feature_names
    def transform(self, X):
        Z = X[:, self.selected_idx]
        Z = Z.toarray() if hasattr(Z, "toarray") else np.asarray(Z)
        return (np.log1p(Z) - self.mu) / self.sd
    def predict_proba(self, X, return_draws=False):
        Z = self.transform(X)
        P = expit(self.a_draws[None, :] + Z @ self.b_draws.T)   # (n, draws)
        p = P.mean(1)
        return (np.c_[1 - p, p], P) if return_draws else np.c_[1 - p, p]
    @property
    def coef_mean(self): return self.b_draws.mean(0)
