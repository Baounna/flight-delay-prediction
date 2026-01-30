from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("FlightDelay-Clean").getOrCreate()

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("data/flight_delays.csv")
)

# Supprimer lignes null
df = df.dropna()

# Exemple: s'assurer que Month est numérique
df = df.withColumn("Month", col("Month").cast("int"))

df.printSchema()
print("Rows after clean:", df.count())

# Sauvegarder cleaned (optionnel)
df.coalesce(1).write.mode("overwrite").option("header", True).csv("results/cleaned_csv")

spark.stop()
