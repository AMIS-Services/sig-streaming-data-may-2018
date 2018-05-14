import boto3
import json
import time


kinesis_client = boto3.client('kinesis')
kinesis_stream = "traffic-message-stream"
get_record_limit = 10
dump_filename = 'traffic-messages.json'

response = kinesis_client.describe_stream(StreamName=kinesis_stream)
# print(response)

my_shard_id = response['StreamDescription']['Shards'][0]['ShardId']

shard_iterator = kinesis_client.get_shard_iterator(StreamName=kinesis_stream,
                                                   ShardId=my_shard_id,
                                                   ShardIteratorType='LATEST')

my_shard_iterator = shard_iterator['ShardIterator']

record_response = kinesis_client.get_records(ShardIterator=my_shard_iterator,
                                             Limit=get_record_limit)
if __name__ == "__main__":
    print("Start consuming Kinesis stream {}".format(kinesis_stream))
    while 'NextShardIterator' in record_response:
        no_record_retrieved = len(record_response['Records'])
        print("  {} records retrieved from stream".format(no_record_retrieved))
        for i in range(no_record_retrieved):
            d = record_response['Records'][i]['Data'].decode('utf-8')
            # For formatted JSON uncomment this line
            # print(json.dumps(json.loads(d), indent=2))
            with open(dump_filename, 'a') as file:
                file.write(d)
            print(d)

        # wait for a few seconds and get the next records
        time.sleep(1)

        record_response = kinesis_client.get_records(ShardIterator=record_response['NextShardIterator'],
                                                     Limit=get_record_limit)
        no_record_retrieved = len(record_response['Records'])
        print("  {} records retrieved from stream".format(no_record_retrieved))
