#!/usr/bin/env python3
import aws_cdk as cdk

from starter.final_stack import FinalStack


app = cdk.App()
stack = FinalStack(
    app,
    "FinalStack",
)

app.synth()
