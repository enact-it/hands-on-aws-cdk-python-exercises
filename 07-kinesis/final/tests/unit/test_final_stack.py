import aws_cdk as core
import aws_cdk.assertions as assertions

from final.final_stack import FinalStack


def test_s3_bucket_created():
    app = core.App()
    stack = FinalStack(app, "final")
    template = assertions.Template.from_stack(stack)
    template.has_resource_properties("AWS::S3::Bucket", {})


def test_kinesis_stream_created():
    app = core.App()
    stack = FinalStack(app, "final")
    template = assertions.Template.from_stack(stack)
    template.has_resource_properties("AWS::Kinesis::Stream", {})


def test_kinesis_firehose_created():
    app = core.App()
    stack = FinalStack(app, "final")
    template = assertions.Template.from_stack(stack)
    template.has_resource_properties("AWS::KinesisFirehose::DeliveryStream", {})
