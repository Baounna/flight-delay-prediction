# Flight Delay Prediction 🚀

A small project that trains a Random Forest model to predict flight delays using PySpark. This repository contains the training pipeline, a Flask API for serving predictions, and a Streamlit UI.

## Contents

- `data/` — original dataset (ignored) and a small sample `data/sample_small.csv` included for quick tests.
- `models/` — saved Spark pipeline (ignored)
- `flask_app/` — Flask server to serve predictions (`/predict` endpoint)
- `streamlit_app.py` — simple UI that calls the Flask API
- `notebooks_or_scripts/` — data cleaning and training scripts

## Quick start 🔧

1. Create a Python environment and install dependencies (PySpark, Flask, Streamlit):

   pip install -r requirements.txt  # or install packages individually

2. Run the Flask API (default port 5001):

   python flask_app/app.py

3. In another terminal, run the Streamlit UI:

   streamlit run streamlit_app.py

4. The app will use `data/sample_small.csv` for quick tests. To use the full dataset, place `flight_delays.csv` under `data/` (note: large files are ignored by git by default).

## Notes

- `models/` and `data/` are in `.gitignore` to avoid committing large Spark artifacts. If you want to track models or data, consider using Git LFS or DVC.

## License

This project is licensed under the MIT License — see `LICENSE`.
