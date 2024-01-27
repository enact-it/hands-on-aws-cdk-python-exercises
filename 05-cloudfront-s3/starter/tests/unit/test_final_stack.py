import aws_cdk as core
import aws_cdk.assertions as assertions

from starter.final_stack import FinalStack


def test_s3_bucket_created():
    app = core.App()
    stack = FinalStack(app, "final")
    template = assertions.Template.from_stack(stack)
    template.resource_count_is("AWS::S3::Bucket", 1)


def test_cloudfront_distribution_created():
    app = core.App()
    stack = FinalStack(app, "final")
    template = assertions.Template.from_stack(stack)
    template.resource_count_is("AWS::CloudFront::Distribution", 1)


def test_cloudfront_distribution_has_origin_access_identity():
    app = core.App()
    stack = FinalStack(app, "final")
    template = assertions.Template.from_stack(stack)
    template.has_resource_properties(
        "AWS::CloudFront::Distribution",
        {
            "DistributionConfig": {
                "Origins": [{"S3OriginConfig": {"OriginAccessIdentity": {}}}]
            }
        },
    )
