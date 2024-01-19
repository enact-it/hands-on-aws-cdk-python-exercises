#!/usr/bin/env python3

import aws_cdk as cdk
from constructs import Construct

# TODO uncomment
# from aws_cdk import (
#     aws_sns_subscriptions as subs,
# )

# from custom_construct.custom_construct import CustomConstruct


class MainApp(Construct):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # TODO create an instance of the CustomConstruct class, and assign it to a variable

        # TODO create a subscription of type "UrlSubscription" on the topic exported by the CustomConstruct class, use webhook.site as the endpoint


app = cdk.App()
MainApp(app, "02-Custom-Construct")

app.synth()
