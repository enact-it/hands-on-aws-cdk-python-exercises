from aws_cdk import Stack, RemovalPolicy, aws_s3 as s3, aws_iam as iam, CfnOutput
from constructs import Construct


class FinalStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(
            self,
            "Bucket",
            versioned=True,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
            encryption=s3.BucketEncryption.S3_MANAGED,
            enforce_ssl=True,
        )
        bucket.grant_write(iam.OrganizationPrincipal("o-2jn6qr72pe"), "/training/*")
        CfnOutput(self, "BucketName", value=bucket.bucket_name)
