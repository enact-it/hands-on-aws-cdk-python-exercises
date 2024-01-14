import aws_cdk as core
import aws_cdk.assertions as assertions

from final.final_stack import FinalStack


# example tests. To run these tests, uncomment this file along with the example
# resource in final/final_stack.py
def test_s3_bucket_created_properly():
    app = core.App()
    stack = FinalStack(app, "final")
    template = assertions.Template.from_stack(stack)

    # Bucket should have a public access block configuration
    template.has_resource_properties(
        "AWS::S3::Bucket", {"PublicAccessBlockConfiguration": {"BlockPublicAcls": True}}
    )

    # Bucket should have versioning enabled
    template.has_resource_properties(
        "AWS::S3::Bucket", {"VersioningConfiguration": {"Status": "Enabled"}}
    )

    # Bucket should have KMS encryption enabled
    template.has_resource_properties(
        "AWS::S3::Bucket",
        {
            "BucketEncryption": {
                "ServerSideEncryptionConfiguration": [
                    {"ServerSideEncryptionByDefault": {"SSEAlgorithm": "AES256"}}
                ]
            }
        },
    )
