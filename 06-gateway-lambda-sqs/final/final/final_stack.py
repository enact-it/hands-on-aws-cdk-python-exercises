from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_lambda_event_sources as lambda_event_sources,
    aws_sqs as sqs,
    aws_apigateway as apigw,
    CfnOutput,
)
from constructs import Construct
import os.path


class FinalStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = sqs.Queue(self, "queue")

        producer = _lambda.Function(
            self,
            "producer",
            code=_lambda.Code.from_asset(os.path.join("../files/producer")),
            runtime=_lambda.Runtime.NODEJS_20_X,
            handler="index.handler",
            environment={"QUEUE_URL": queue.queue_url},
        )

        queue.grant_send_messages(producer)

        api_gateway = apigw.LambdaRestApi(self, "api", handler=producer)

        consumer = _lambda.Function(
            self,
            "consumer",
            code=_lambda.Code.from_asset(os.path.join("../files/consumer")),
            runtime=_lambda.Runtime.NODEJS_20_X,
            handler="index.handler",
        )
        consumer.add_event_source(lambda_event_sources.SqsEventSource(queue))

        queue.grant_consume_messages(consumer)

        CfnOutput(self, "queue_url", value=queue.queue_url)
        CfnOutput(self, "api_gateway_url", value=api_gateway.url)
