from kafka import KafkaProducer
import json
import time

# Producers produce messages to a topic of their choice. 
# It is possible to attach a key to each message, in which case the producer guarantees that all messages with the same key will arrive to the same partition.

# Topics are logs that receive data from the producers and store them across their partitions. Producers always write new messages at the end of the log.

# To read from the Topics we will require a Consumer
# Consumers read the messages of a set of partitions of a topic of their choice at their own pace. 
# If the consumer is part of a consumer group,i.e. a group of consumers subscribed to the same topic, they can commit their offset. 
# The offset is the position in the log where the consumer last consumed or read a message. 

class ProducerServer(KafkaProducer):

    def __init__(self, input_file, topic, **kwargs):
        super().__init__(**kwargs)
        self.input_file = input_file
        self.topic = topic

    #Generates dummy data from the input file
    def generate_data(self):
        print(self.topic)  # remove after testing
        with open(self.input_file) as file:
            # experiment with placement of data = json.load(file) 
            # data = json.load(file) 
            
            for line in file:
                message = self.dict_to_binary(line)
                # TODO send the correct data
                data = json.load(file)  #clarify why we have reassigned to data attribute
                self.topic, message
                self.send()
                time.sleep(1)

    # TODO fill this in to return the json dictionary to binary
    def dict_to_binary(self, json_dict):
        return json.dumps(json_dict).encode('utf-8')
 
