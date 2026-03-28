import os
import sys
from pyspark.sql import SparkSession

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

# Membuat Session Spark
spark = SparkSession.builder \
    .appName("SimpleJob") \
    .getOrCreate()

# Membuat Data Dummy
data = [("A", 10), ("B", 20), ("A", 30)]
columns = ["category", "value"]

# Membuat DataFrame dan Menjalankan Agregasi
df = spark.createDataFrame(data, columns)
df.groupBy("category").sum("value").show()

# Stop Spark
spark.stop()