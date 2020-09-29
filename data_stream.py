import logging
import json
from pyspark.sql import SparkSession
from pyspark.sql.types import *
import pyspark.sql.functions as psf


# TODO Create a schema for incoming resources
# To create a PySpark Dataframe we have to specify its structure using StructType and StructField classes
# A StructType is a collection of StructFields used to define the column name, data type and flag for nullable
# Alternatively; I could have used df2.schema.json() to create the schema form the JSON file; 
# but as I believe there are not too many columns and my DataFrame is not changing I wont
# Reference: https://sparkbyexamples.com/pyspark/pyspark-structtype-and-structfield/
schema = StructType([
    StructField("crime_id", StringType(), True),
    StructField("original_crime_type_name", StringType(), True),
    StructField("report_date", StringType(), True),
    StructField("call_date", StringType(), True),
    StructField("offense_date", StringType(), True),
    StructField("call_time", StringType(), True),
    StructField("call_date_time", TimestampType(), True),
    StructField("disposition", StringType(), True),
    StructField("address", StringType(), True),
    StructField("city", StringType(), True),
    StructField("state", StringType(), True),
    StructField("agency_id", StringType(), True),
    StructField("address_type", StringType(), True),
    StructField("common_location", StringType(), True)
])

def run_spark_job(spark):

    # TODO Create Spark Configuration
    # Create Spark configurations with max offset of 200 per trigger
    # set up correct bootstrap server and port
    # REFERENCE: https://spark.apache.org/docs/latest/configuration.html
    df = spark \
        .readStream \
        .format("kafka")\
        .option("kafka.bootstrap.servers","localhost:9092")\
        .option("subscribe","com.sf.police.event.calls")\
        .option("startingOffsets","earliest")\
        .option("maxRatePerPartition",100)\
        .option("maxOffsetsPerTrigger",200)\
        .option("stopGracefullyOnShutdown", "true") \
        .load()
  

    # Show schema for the incoming resources for checks
    # With the printSchema() function, we can see that the schema has been taken into consideration:
    df.printSchema()

    # TODO extract the correct column from the kafka input resources
    # Take only value and convert/CAST it to String
    # Chose to use selectExpr as it is considered to be easy to use for casing Data Types
    # Reference: https://medium.com/analytics-vidhya/spark-select-and-select-expr-deep-dive-d63ef5e04c87
    
    kafka_df = df.selectExpr("CAST(value as STRING)")

    service_table = kafka_df\
        .select(psf.from_json(psf.col('value'), schema).alias("POLICE_SERVICE_CALLS"))\
        .select("POLICE_SERVICE_CALLS.*")

    # TODO select original_crime_type_name and disposition
    
    # In distributed and networked systems, there’s always a chance for disruption. 
    # So it is not guaranteed that the data will arrive to the Stream Processing Engine in the order they were created. 
    # To therefore handle the risk of Out-of-Order data and be able to run in the event of late arriving events; 
    # I want to preserve the state of events but not so long it consumes too much of systems resource. 
    # So I have used withWatermark() to specify how long the solution would wait for late events. 
    # Reference: https://towardsdatascience.com/watermarking-in-spark-structured-streaming-9e164f373e9
    
    # note: the col() function Returns a Column based on the given column name
    
    
    distinct_table = service_table \
        .select(
        psf.col("original_crime_type_name"),
        psf.col("disposition"),
        psf.to_timestamp(psf.col("call_date_time")).alias("call_date_time")
    ) 
    
    print("-------------------------------------------")
    distinct_table.printSchema()
    print("-------------------------------------------")
    
    # count the number of original crime type
    # have used the pyspark function window() to calculate over the group of rows
    
    agg_df = distinct_table\
        .groupBy("original_crime_type_name", 
                 psf.window("call_date_time", "60 minutes"))\
        .count()
    
    # look at understanding window() function better
              

    # TODO Q1. Submit a screen shot of a batch ingestion of the aggregation
    # TODO write output stream
    query = agg_df \
        .writeStream \
        .queryName("agg_query")\
        .format("console") \
        .outputMode("complete") \
        .start()
    
    print("-------------------------------------------")
    print(agg_df)
    print("-------------------------------------------")

    # TODO attach a ProgressReporter
    query.awaitTermination()

    # TODO get the right radio code json path
    radio_code_json_filepath = "radio_code.json"
    radio_code_df = spark.read.json(radio_code_json_filepath)

    # clean up your data so that the column names match on radio_code_df and agg_df
    # we will want to join on the disposition code

    # TODO rename disposition_code column to disposition
    radio_code_df = radio_code_df.withColumnRenamed("disposition_code", "disposition")

    # TODO join on disposition column
    join_query = agg_df \
        .join(radio_code_df, "disposition") \
        .writeStream \
        .format("console") \
        .queryName("join") \
        .start()

    join_query.awaitTermination()


if __name__ == "__main__":
    logger = logging.getLogger(__name__)

    # TODO Create Spark in Standalone mode
    spark = SparkSession \
        .builder \
        .master("local[*]") \
        .appName("KafkaSparkStructuredStreaming") \
        .config("spark.ui.port", 3000) \
        .getOrCreate()

    print("-------------------------------------------")
    logger.info("Spark started")
    print("-------------------------------------------")
    run_spark_job(spark)

    spark.stop()
