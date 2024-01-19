#!/usr/bin/env python3

import aws_cdk as cdk

from final.final_stack import FinalStack


app = cdk.App()
FinalStack(app, "03-Basic-Asset")
app.synth()
