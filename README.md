# Predicting Epidemic Outbreaks from Sparse Twitter Data

Code, results, figures and the Streamlit prototype for the ITRPA4 mini-dissertation
*Predicting Epidemic Outbreaks from Sparse Twitter Data: Statistical vs. Machine Learning Approaches*
(Omolemo Euclid Thakanyane, student no. 2PQLM3S99).

The repository holds the experiment notebook, the helper module, saved results and figures, and a prototype that loads the trained models. The raw UCI dataset is **not** committed (it is larger than needed in git, and should be downloaded from the official source).

## Layout

| Path | What it is |
|---|---|
| `itrpa_experiments.ipynb` | Full experiment pipeline, already executed with outputs saved |
| `itrpa_models.py` | Helper module (custom model classes shared with the prototype) |
| `results/` | CSV tables from the notebook (raw, unrounded values). Section 14 tables are `improve_*.csv` |
| `results_summary.md` | Numeric results in tables, plus caveats and deviations from the proposal |
| `figures/` | Chapter 4 figures (`fig4_01`–`fig4_24`; `live_daily_counts.png` is the live-data illustration) |
| `prototype/` | Streamlit app (see `prototype/README.md`) |
| `tests/` | pytest suite for the model code, saved artefacts, results tables and the temporal split |
| `.github/workflows/tests.yml` | GitHub Actions workflow that runs `pytest` |

## Data source (not in this repo)

The experiments use the **Influenza Outbreak Event Prediction via Twitter** dataset:

- Zhao, Q. et al. (2015). UCI Machine Learning Repository, dataset 861.
- DOI: [10.24432/C5CP7V](https://doi.org/10.24432/C5CP7V)
- Licence: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- Download: [UCI repository – Influenza Outbreak Event Prediction via Twitter](https://archive.ics.uci.edu/dataset/861/influenza+outbreak+event+prediction+via+twitter)

Place the file as `influenza_outbreak_dataset.mat` in the repository root (next to the notebook) before re-running the notebook. The notebook also accepts an upload if you run it in Google Colab.

Saved models, `prototype/artifacts/X_test.npz` and the results CSVs are included so the tests and the prototype can run without the `.mat` file. Two large regenerated matrices (`X_test_temporal_linear.npz` and `X_test_temporal_tree.npz`, about 31 MB) are not included; re-running the notebook recreates them.

## Setup

Python 3.11+ (the saved run used Python 3.13.5). A virtual environment is recommended:

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt -r requirements-dev.txt
pip install -r prototype/requirements.txt   # only needed for the Streamlit app
```

Saved models were produced with scikit-learn 1.9.1, LightGBM 4.7.0 and XGBoost 3.4.1 (see `results_summary.md`). Use the same major versions when loading the pickles.

## Run the notebook

```bash
# after placing influenza_outbreak_dataset.mat in this directory
jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=-1 itrpa_experiments.ipynb
```

In Colab: upload the notebook, run the first code cell, and upload the `.mat` file when asked.

All seeds are fixed (`SEED = 42`). The tree ensembles and MLP use multithreading, so tiny floating-point differences across machines are possible.

## Run the tests

```bash
pip install -r requirements.txt -r requirements-dev.txt
pytest
```

The tests check:

- the functions and custom classes in `itrpa_models.py`;
- that the saved joblib models load and predict on `prototype/artifacts/X_test.npz` (correct shape, probabilities in `[0, 1]`);
- that the results CSVs have the expected columns, including LightGBM test PR-AUC **0.3823**, L1 logistic regression **0.3761**, and the improved ensemble **0.494325**;
- that the train/test split is temporal (every test time step comes after the training period);
- a smoke import of `prototype/app.py`.

## Run the prototype

```bash
cd prototype
pip install -r requirements.txt
streamlit run app.py          # opens http://localhost:8501
```

Details of each tab, contribution methods and the live-data caveats are in `prototype/README.md`.

## Live X sample (illustration only)

`prototype/sample_live_posts.json` and `sample_live_posts_filtered_out.json` are a small public-post sample used only by the live dashboard tab. They are **not** part of the evaluated dissertation results.

Usernames and handles in that sample had already been replaced with `@user`, and author IDs were not retained. Before this repository was committed, tweet IDs, status URLs and place metadata were also removed so that individual posts cannot be looked up. Post text and timestamps remain, because the dashboard needs them.

## Licence notes

The UCI dataset is CC BY 4.0 (Zhao et al., 2015, DOI 10.24432/C5CP7V). Please cite that source if you reuse the data or results that depend on it.
