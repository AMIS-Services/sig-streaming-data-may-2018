import json
from boto import kinesis
import requests
import time


kinesis_client = kinesis.connect_to_region("us-east-1")
print('Connected to {}'.format(kinesis_client))
kinesis_stream = "traffic-message-stream"
traffic_message_service_endpoint = "http://localhost:5000/traffic"


def get_traffic_messages(no_of_messages: int=10):
    parameters = "?count={}".format(no_of_messages)
    endpoint = traffic_message_service_endpoint + parameters
    req = requests.get(endpoint)
    if req.status_code == 200:
        return req.json()
    else:
        return {}


if __name__ == "__main__":
    print("Start streaming data to Kinesis stream {}".format(kinesis_stream))
    counter = 0
    while True:
        number_of_messages = 100
        data = get_traffic_messages(number_of_messages)
        #  print(data)
        for i in range(number_of_messages):
            message = data[i]
            message['location']['geoCoordinates']['latitude'] = \
                message['location']['geoCoordinates']['latitude'][:-1]
            partitionkey = message['location']['roadNumber']
            print(data[i])
            # Write a single record at a time to Kinesis stream
            kinesis_client.put_record(kinesis_stream, json.dumps(message), partitionkey)
            counter += 1
        print(">>> {} messages send to kinesis stream".format(counter))
        time.sleep(5)  # Wait 5 seconds for sending the next messages
