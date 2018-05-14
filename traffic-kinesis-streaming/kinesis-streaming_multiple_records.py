import json
import boto3
import requests

"""See more AWS API documentation at http://boto3.readthedocs.io/en/latest/reference/services/kinesis.html"""

kinesis_client = boto3.client('kinesis')
kinesis_stream = "traffic-message-stream"
traffic_message_service_endpoint = "http://localhost:5000/traffic"


def get_traffic_messages(no_of_messages: int = 10):
    parameters = "?count={}".format(no_of_messages)
    endpoint = traffic_message_service_endpoint + parameters
    req = requests.get(endpoint)
    if req.status_code == 200:
        return req.json()
    else:
        return {}


if __name__ == "__main__":
    while True:
        # max 500 record at at time for put_records
        number_of_messages = 10
        data = get_traffic_messages(number_of_messages)
        records = list()
        for message in data:
            records.append(
                {
                    'Data': json.dumps(message),
                    'PartitionKey': message['location']['roadNumber']
                },
            )
        kinesis_client.put_records(Records=records, StreamName=kinesis_stream)
        print("Put {} records to Kinesis stream {}...".format(number_of_messages, kinesis_stream))
