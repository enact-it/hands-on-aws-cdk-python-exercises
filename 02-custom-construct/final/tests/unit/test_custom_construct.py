import aws_cdk as core
import aws_cdk.assertions as assertions
from custom_construct.custom_construct import CustomConstruct


def test_sns_topic_created():
    app = core.App()
    stack = CustomConstruct(app, "test")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::SNS::Topic", 1)


def test_s3_bucket_created():
    app = core.App()
    stack = CustomConstruct(app, "test")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::S3::Bucket", 1)


def test_s3_bucket_notification_created():
    app = core.App()
    stack = CustomConstruct(app, "test")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties(
        "Custom::S3BucketNotifications",
        {
            "NotificationConfiguration": {
                "TopicConfigurations": [{"Events": ["s3:ObjectCreated:*"]}]
            }
        },
    )
