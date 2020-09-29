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
        
 ----------------------------------------------------------------------------------       
        distinct_table = service_table \
        .select(
        psf.col("original_crime_type_name"),
        psf.col("disposition"),
        psf.to_timestamp(psf.col("call_date_time")).alias("call_date_time")
    ) 
 
 ----------------------------------------------------------------------------------      
 
     agg_df = distinct_table\
        .groupBy("original_crime_type_name", 
                 psf.window("call_date_time", "60 minutes"))\
        .count()
        
  ----------------------------------------------------------------------------------            

     query = agg_df \
        .writeStream \
        .queryName("agg_query")\
        .format("console") \
        .outputMode("complete") \
        .start()
    ----------------------------------------------------------------------------------         
             
      join_query = agg_df \
        .join(radio_code_df, "disposition") \
        .writeStream \
        .format("console") \
        .queryName("join") \
        .start()
