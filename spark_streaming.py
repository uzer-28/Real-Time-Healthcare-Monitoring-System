from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder\
         .appName("HealthCare")\
         .config("spark.sql.adaptive.enabled", True)\
         .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0") \
         .getOrCreate()

df = spark.readStream\
    .format("kafka")\
    .option("kafka.bootstrap.servers", "localhost:9092")\
    .option("subscribe", "patient-vitals")\
    .option("startingOffsets", "latest")\
    .load()

schema = "timestamp STRING, temperature FLOAT, patient_id INTEGER, heart_rate INTEGER, blood_pressure STRING, oxygen_level INTEGER"

df_json = df.selectExpr("CAST(value as STRING)")\
    .select(from_json(col("value"), schema).alias("data"))\
    .select("data.*")

df_processed = df_json.withColumn(
    "systolic", split(col("blood_pressure"), "/")[0].cast("int")
        ).withColumn(
    "diastolic", split(col("blood_pressure"), "/")[1].cast("int")
        )

df_processed = df_processed.withColumn(
    "temperature",
    round((col("temperature") - 32) * 5/9, 1)
)

df_final = df_processed.withColumn(
    "risk_level",
    when((col("oxygen_level") < 88) | (col("heart_rate") > 122), "HIGH")
    .when((col("oxygen_level") < 92) | (col("heart_rate") > 110), "MEDIUM")
    .otherwise("LOW")
)

df_final = df_final.withColumn(
    "timestamp",
    date_format(to_timestamp("timestamp"), "yyyy-MMM-dd HH:mm:ss")
)

df_final = df_final.select(
    to_json(struct("*")).alias("value")
)

query = df_final.writeStream\
    .outputMode("append")\
    .format("kafka")\
    .option("kafka.bootstrap.servers", "localhost:9092")\
    .option("checkpointLocation", "/tmp/checkpoint") \
    .option("topic", "processed-vitals")\
    .start()

query.awaitTermination()

