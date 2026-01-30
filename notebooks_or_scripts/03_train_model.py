from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import RandomForestRegressor
from pyspark.ml import Pipeline
from pyspark.ml.evaluation import RegressionEvaluator

LABEL_COL = "AA"  

spark = SparkSession.builder.appName("FlightDelay-Train").getOrCreate()

df = spark.read.option("header", True).option("inferSchema", True).csv("data/flight_delays.csv").dropna()

feature_cols = [c for c in df.columns if c != LABEL_COL]

assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
model = RandomForestRegressor(featuresCol="features", labelCol=LABEL_COL, numTrees=200, maxDepth=10)

pipeline = Pipeline(stages=[assembler, model])

train_df, test_df = df.randomSplit([0.8, 0.2], seed=42)

fitted = pipeline.fit(train_df)
pred = fitted.transform(test_df)

evaluator = RegressionEvaluator(labelCol=LABEL_COL, predictionCol="prediction", metricName="rmse")
rmse = evaluator.evaluate(pred)
print(f"RMSE = {rmse}")

fitted.write().overwrite().save("models/flight_delay_pipeline")

spark.stop()
