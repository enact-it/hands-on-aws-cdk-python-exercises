import aws_cdk as core
import aws_cdk.assertions as assertions

from final.final_stack import FinalStack

# example tests. To run these tests, uncomment this file along with the example
# resource in final/final_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = FinalStack(app, "final")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
