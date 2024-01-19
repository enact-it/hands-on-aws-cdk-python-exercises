from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins,
    RemovalPolicy,
    CfnOutput,
)
from constructs import Construct


class FinalStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # TODO create a Bucket
        bucket = s3.Bucket(
            self,
            "Bucket",
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
            # Add bucket asset
        )

        # TODO Add CloudFront origin access identity
        origin_access_identity = cloudfront.OriginAccessIdentity(
            self,
            "OriginAccessIdentity",
        )

        # TODO Grant the origin access identity read permissions on the bucket
        bucket.grant_read(origin_access_identity)

        # TODO Create a CloudFront distribution with the bucket as an origin
        distribution = cloudfront.Distribution(
            self,
            "Distribution",
            default_root_object="index.html",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.S3Origin(
                    bucket, origin_access_identity=origin_access_identity
                )
            ),
        )

        # TODO create a CfnOutput for the distribution domain name
        CfnOutput(self, "DistributionDomainName", value=distribution.domain_name)
