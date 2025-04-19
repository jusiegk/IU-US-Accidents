from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count

spark = SparkSession.builder \
    .appName("KafkaToPostgres") \
    .getOrCreate()

df = spark \
    .read \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "accidents") \
    .option("startingOffsets", "earliest") \
    .load()

df_string = df.selectExpr("CAST(value AS STRING) as json_str")

from pyspark.sql.functions import from_json
from pyspark.sql.types import StructType, StringType

schema = StructType().add("State", StringType())

parsed_df = df_string.select(from_json(col("json_str"), schema).alias("data")).select("data.*")

result = parsed_df.groupBy("State").agg(count("*").alias("Unfallanzahl"))

result.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://postgres:5432/traffic") \
    .option("dbtable", "unfall_aggregation") \
    .option("user", "user") \
    .option("password", "pass") \
    .option("driver", "org.postgresql.Driver") \
    .mode("overwrite") \
    .save()

print("Spark")

