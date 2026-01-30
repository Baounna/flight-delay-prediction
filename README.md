# Flight Delay Prediction 🚀

[![CI](https://github.com/Baounna/flight-delay-prediction/actions/workflows/ci.yml/badge.svg)](https://github.com/Baounna/flight-delay-prediction/actions)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg?logo=python)](https://www.python.org/)
[![Apache Spark](https://img.shields.io/badge/Apache%20Spark-3.0-orange.svg?logo=apachespark)](https://spark.apache.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey.svg?logo=flask)](https://flask.palletsprojects.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-%E2%89%A50-orange.svg?logo=streamlit)](https://streamlit.io/)
[![License](https://img.shields.io/github/license/Baounna/flight-delay-prediction)](LICENSE)

## Project Overview

**Flight Delay Prediction** is a compact end-to-end proof-of-concept that demonstrates how to build a data pipeline and serve predictions using Apache Spark (PySpark). The project includes data cleaning, a Spark ML pipeline (VectorAssembler → RandomForestRegressor), a Flask API for model serving, and a Streamlit UI for demoing predictions.

This repo is curated to be portfolio-ready for recruiters and sharing on LinkedIn — it includes reproducible instructions, CI checks, and contribution guidance.

---

## Architecture (simple diagram)

```
CSV data -> cleaning -> Train pipeline (Spark) -> Saved Pipeline (models/)
                                         ↑
                              Flask API loads pipeline
                                         ↓
                             Streamlit UI -> POST /predict
```

### Architecture – Explanation
- Data is ingested from `data/flight_delays.csv` (a small sample is included at `data/sample_small.csv`).
- `notebooks_or_scripts/02_clean.py` performs cleaning and writes a cleaned CSV to `results/cleaned_csv`.
- `notebooks_or_scripts/03_train_model.py` builds a Spark ML Pipeline (VectorAssembler + RandomForest) and writes the fitted pipeline to `models/flight_delay_pipeline`.
- `flask_app/app.py` loads the saved pipeline and exposes `/predict` and `/health` endpoints.
- `streamlit_app.py` provides a simple UI that sends features to the Flask API and displays predictions.

---

## End-to-end pipeline

1. Prepare data: put the full dataset at `data/flight_delays.csv` (or use the provided sample).
2. Clean data: `python notebooks_or_scripts/02_clean.py` (writes to `results/cleaned_csv`).
3. Train: `python notebooks_or_scripts/03_train_model.py` (saves pipeline to `models/flight_delay_pipeline`).
4. Serve: `python flask_app/app.py` (default port `5001`).
5. Demo UI: `streamlit run streamlit_app.py` and use the UI to call the API.

---

## Tech stack

| Layer | Technology |
|-------|------------|
| Data processing & ML | PySpark (Spark ML) |
| Model | RandomForestRegressor (Spark ML) |
| API | Flask |
| UI / Demo | Streamlit |
| CI | GitHub Actions (lint + tests) |

---

## Screenshots

*Add screenshots to `docs/images/` and replace links below.*

- Streamlit UI (example): `docs/images/streamlit_screenshot.png`
- Flask UI (index): `docs/images/flask_index.png`

---

## Demo instructions

1. (Optional) Create virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Start the Flask API:
```bash
python flask_app/app.py
```
3. In a new terminal, start Streamlit:
```bash
streamlit run streamlit_app.py
```
4. Use the web UI to enter features and get a prediction.

---

## Folder structure

```
FlightDelay_BigData/
├── flask_app/            # Flask server and templates
├── data/                 # Dataset (ignored in git); sample included
├── models/               # Saved Spark pipeline (ignored in git)
├── notebooks_or_scripts/ # Cleaning, training scripts
├── results/              # Cleaned/exported CSV outputs
├── streamlit_app.py      # Streamlit demo
├── tests/                # Unit tests
├── .github/              # Workflows and templates
├── README.md
└── LICENSE
```

---

## Reproducibility

- This project tries to be easy to reproduce using `requirements.txt` (add your Python deps there). For large data/models, consider using Git LFS or DVC.
- Recommended: Python 3.10+, Java 11+ for Spark, and local Spark installed or use PySpark wheel in the environment.

---

## Future improvements

- Add end-to-end unit/integration tests that can mock Spark objects.
- Add model evaluation, explainability (SHAP) and feature importance export.
- Add Dockerfile + docker-compose for local reproducible dev environment.
- Use DVC to version datasets and model artifacts.
- Improve input validation and error handling in the Flask API.

---

## Code quality & suggestions

- Add docstrings and type hints for functions and scripts.
- Split monolithic scripts into modules with testable functions.
- Add logging (instead of print) with structured logs and levels.
- Add more unit tests and a linter (flake8/pylint) which is included in CI.
- Avoid importing Spark at module import time — initialize Spark inside `if __name__ == "__main__"` blocks or factory functions so tests can import modules without starting Spark.

---

## Contributing

See `CONTRIBUTING.md` for contribution guidelines, code style, and PR template.

---

## License

MIT — see `LICENSE` for details.

---

