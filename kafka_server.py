import producer_server

TOPIC_NAME = 'com.sf.police.event.calls'
SERVER_URL = 'localhost:9092'
CLIENT_ID = 'com.udacity.dep.police.broker'

def run_kafka_server():
	# TODO get the json file path
    input_file = "./police-department-calls-for-service.json"

    # client id: is used as an identifier for the client application. It will be used when logging errors, monitoring aggregates. 
    # it acts as a logical grouping across all requests from a particular client.
    # for exmample; one might want to monitor not just the requests per second overall, but the number coming from each client application 
    # (each of which could reside on multiple servers). 

    producer = producer_server.ProducerServer(
        input_file=input_file,
        topic=TOPIC_NAME,
        bootstrap_servers=SERVER_URL ,
        client_id=CLIENT_ID  
    )

    return producer


def feed():
    producer = run_kafka_server()
    producer.generate_data()


if __name__ == "__main__":
    feed()
