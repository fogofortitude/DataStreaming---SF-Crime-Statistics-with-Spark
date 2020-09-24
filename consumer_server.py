from kafka import KafkaConsumer


bootstrap_servers = ['localhost:9092']
topicName = 'com.sf.police.event.calls'

consumer = KafkaConsumer (topicName, group_id = 'group1',bootstrap_servers = bootstrap_servers,
auto_offset_reset = 'earliest')

for message in consumer:
    if message is not None:
        print( message.value.decode('utf-8') )
