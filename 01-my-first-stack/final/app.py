#!/usr/bin/env python3

import aws_cdk as cdk

from myfirst.my_first_stack import MyFirstStack


app = cdk.App()
MyFirstStack(app, "MyFirstStack")

app.synth()
