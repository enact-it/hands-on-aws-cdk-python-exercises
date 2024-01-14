import aws_cdk as core
import aws_cdk.assertions as assertions

from final.final_stack import FinalStack


def test_lambda_function_created():
    app = core.App()
    stack = FinalStack(app, "final")
    template = assertions.Template.from_stack(stack)
    template.resource_count_is("AWS::Lambda::Function", 1)
