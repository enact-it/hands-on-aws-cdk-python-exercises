#!/usr/bin/env python3
import aws_cdk as cdk

from final.final_stack import FinalStack


app = cdk.App()
stack = FinalStack(
    app,
    "CloudFront-S3",
)

app.synth()
