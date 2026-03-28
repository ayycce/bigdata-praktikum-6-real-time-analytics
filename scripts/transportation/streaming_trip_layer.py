from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *

# Inisialisasi Spark Session
spark = SparkSession.builder.appName("TransportationStreaming").getOrCreate()

# Mendefinisikan Schema sesuai dengan data JSON yang kita buat
schema = StructType([
    StructField("trip_id", StringType()),
    StructField("vehicle_type", StringType()),
    StructField("location", StringType()),
    StructField("distance", DoubleType()),
    StructField("fare", DoubleType()),
    StructField("timestamp", StringType())
])

# Membaca data streaming dari folder output generator
df = spark.readStream.schema(schema).json("stream_data/transportation")

# Mengubah tipe data kolom timestamp menjadi tipe Timestamp Spark
df = df.withColumn("timestamp", to_timestamp("timestamp"))

# Menulis data streaming ke format Parquet
df.writeStream \
    .format("parquet") \
    .option("path", "data/serving/transportation") \
    .option("checkpointLocation", "data/checkpoints/transportation") \
    .start() \
    .awaitTermination()