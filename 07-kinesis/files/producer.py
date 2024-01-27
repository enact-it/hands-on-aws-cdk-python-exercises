from markovclick import dummy
from botocore.exceptions import ClientError
import boto3
import json
import logging
import _sha256
import time
import random

KINESIS_STREAM_NAME = "FinalStack-stream19075594-GXZFSrHWYXgw"


class KinesisStream:
    """Encapsulates a Kinesis stream."""

    def __init__(self, kinesis_client, name=KINESIS_STREAM_NAME):
        """
        :param kinesis_client: A Boto3 Kinesis client.
        """
        self.kinesis_client = kinesis_client
        self.name = name
        self.details = None
        self.stream_exists_waiter = kinesis_client.get_waiter("stream_exists")

    def put_record(self, data, partition_key):
        """
        Puts data into the stream. The data is formatted as JSON before it is passed
        to the stream.

        :param data: The data to put in the stream.
        :param partition_key: The partition key to use for the data.
        :return: Metadata about the record, including its shard ID and sequence number.
        """
        try:
            response = self.kinesis_client.put_record(
                StreamName=self.name, Data=json.dumps(data), PartitionKey=partition_key
            )
            logger.info(f"Success, sequence number: {response.get('SequenceNumber')}")
        except ClientError:
            logger.exception(
                f"Couldn't put record {partition_key} in stream {self.name}"
            )
            raise
        else:
            return response


if __name__ == "__main__":
    # Set up logging with a level of INFO
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)

    # Create a Kinesis client
    kinesis_client = boto3.client("kinesis", region_name="eu-west-1")
    input_stream = KinesisStream(kinesis_client)

    # Generate some random clickstream data
    n_of_streams = 10000
    logger.info(f"Generating {n_of_streams} streams of clickstream data...")
    clickstream = dummy.gen_random_clickstream(n_of_streams=n_of_streams, n_of_pages=12)
    delay = 0

    # Put the clickstream data into the stream
    logger.info(
        f"Putting records in stream {input_stream.name} with delay of {delay} seconds."
    )
    for clicks in clickstream:
        visitor = random.choice(range(1, 100))
        record = {
            "visitor": visitor,
            "clicks": clicks,
            # Add a UTC timestamp suitable for SQL
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()),
        }
        logger.info(f"Uploading {record}")
        input_stream.put_record(
            record, _sha256.sha256("".join(clicks).encode()).hexdigest()
        )
        time.sleep(delay)
