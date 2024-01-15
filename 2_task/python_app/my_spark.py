from pyspark.sql import SparkSession

spark = (SparkSession
         .builder
         .master("spark://spark-master:7077")
         .appName("spark_in_compose")
         .config("spark.jars", "file:/opt/bitnami/spark/driver/postgresql-42.2.27.jre6.jar")
         .config("spark.driver.extraClassPath", "file:/opt/bitnami/spark/driver/postgresql-42.2.27.jre6.jar")
         .getOrCreate())

sc = spark.sparkContext

jdbc_url = "jdbc:postgresql://postgres:5432/spark_db?serverTimezone=UTC"
df_prices = (
    spark.read
    .format("jdbc")
    .option("url", jdbc_url)
    .option("dbtable", "public.prices")
    .option("user", "postgres")
    .option("driver", "org.postgresql.Driver")
    .option("password", "postgres")
    .load()
)

df_prices.createOrReplaceTempView("prices")

result_df = spark.sql("""
    SELECT location, bedrooms, CEILING(AVG(price)) as average_price
    FROM prices
    GROUP BY location, bedrooms
""")
result_df.show()
