from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("FlightDelay-Check").getOrCreate()

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("data/flight_delays.csv")
)

print("Columns:", df.columns)
df.printSchema()
df.show(5, truncate=False)

spark.stop()
