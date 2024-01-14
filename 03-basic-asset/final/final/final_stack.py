from aws_cdk import Stack, aws_lambda as _lambda
from constructs import Construct
import os.path


class FinalStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        _lambda.Function(
            self,
            "lambda_function",
            code=_lambda.Code.from_asset(os.path.join("../handler")),
            runtime=_lambda.Runtime.PYTHON_3_12,
            handler="handler.lambda_handler",
        )
