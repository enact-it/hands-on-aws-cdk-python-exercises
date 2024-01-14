from constructs import Construct
from aws_cdk import (
    Stack,
    aws_sns as sns,
    aws_s3 as s3,
    aws_s3_notifications as s3notify,
)


class CustomConstruct(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # TODO create a topic, and assign it to the "topic" attribute
        self.topic = sns.Topic(self, "Topic")

        # TODO create a bucket
        bucket = s3.Bucket(self, "Bucket")

        # TODO create an object created notification on the bucket and point it to the topic
        bucket.add_object_created_notification(s3notify.SnsDestination(self.topic))
