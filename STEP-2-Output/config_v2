    Increased maxRatePerPartition from 100 to 200
    
    
    df = spark \
        .readStream \
        .format("kafka")\
        .option("kafka.bootstrap.servers","localhost:9092")\
        .option("subscribe","com.sf.police.event.calls")\
        .option("startingOffsets","earliest")\
        .option("maxRatePerPartition",200)\
        .option("maxOffsetsPerTrigger",200)\
        .option("stopGracefullyOnShutdown", "true") \
        .load()
