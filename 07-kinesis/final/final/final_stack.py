from aws_cdk import (
    Stack,
    aws_kinesis as kinesis,
    aws_s3 as s3,
    aws_kinesisfirehose_alpha as firehose,
    aws_kinesisfirehose_destinations_alpha as firehose_destinations,
    CfnOutput,
    RemovalPolicy,
)
from constructs import Construct


class FinalStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        stream = kinesis.Stream(self, "stream", shard_count=1)

        bucket = s3.Bucket(
            self,
            "bucket",
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )

        firehose_delivery = firehose.DeliveryStream(
            self,
            "delivery_stream",
            destinations=[
                firehose_destinations.S3Bucket(
                    bucket=bucket,
                    data_output_prefix="data/year=!{timestamp:yyyy}/month=!{timestamp:MM}/day=!{timestamp:dd}/hour=!{timestamp:HH}/",
                    error_output_prefix="errors/year=!{timestamp:yyyy}/month=!{timestamp:MM}/day=!{timestamp:dd}/hour=!{timestamp:HH}/!{firehose:error-output-type}/",
                )
            ],
            source_stream=stream,
        )

        bucket.grant_write(firehose_delivery)
        stream.grant_read(firehose_delivery)

        CfnOutput(self, "kinesis_stream_name", value=stream.stream_name)
