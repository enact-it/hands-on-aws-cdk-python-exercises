from aws_cdk import (
    # Duration,
    Stack,
    # TODO uncomment
    # aws_s3 as s3,
    # aws_cloudfront as cloudfront,
    # aws_cloudfront_origins as origins,
    # RemovalPolicy,
    # CfnOutput
)
from constructs import Construct


class FinalStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # TODO create a Bucket

        # TODO Add CloudFront origin access identity

        # TODO Grant the origin access identity read permissions on the bucket

        # TODO Create a CloudFront distribution with the bucket as an origin

        # TODO create a CfnOutput for the distribution domain name
