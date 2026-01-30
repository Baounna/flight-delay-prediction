from flask import Flask, request, jsonify, render_template
from pyspark.sql import SparkSession
from pyspark.ml.pipeline import PipelineModel

LABEL_COL = "AA"
MODEL_PATH = "models/flight_delay_pipeline"

app = Flask(__name__)
spark = (
    SparkSession.builder
    .appName("FlightDelay-Flask")
    .master("local[*]")
    .config("spark.ui.enabled", "false")
    .config("spark.driver.bindAddress", "127.0.0.1")
    .getOrCreate()
)

model = PipelineModel.load(MODEL_PATH)

assembler = model.stages[0]
REQUIRED_FEATURES = assembler.getInputCols()


@app.route("/", methods=["GET"])
def home():
    # نبعث لائحة الأعمدة للواجهة باش تولّد inputs تلقائياً
    return render_template("index.html", features=REQUIRED_FEATURES, label=LABEL_COL)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)

    missing = [c for c in REQUIRED_FEATURES if c not in data]
    if missing:
        return jsonify({"error": "Missing features", "missing": missing}), 400

    row = {k: float(data[k]) for k in REQUIRED_FEATURES}
    df = spark.createDataFrame([row])

    pred = model.transform(df).select("prediction").collect()[0][0]
    return jsonify({"label": LABEL_COL, "prediction": float(pred)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)
