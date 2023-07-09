from aws_cdk import (
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
    Stack,
    Duration
)

from constructs import Construct

class FlaskStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, app_name: str, code_path: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a Lambda function with the code from the 'src' directory
        lambda_handler = _lambda.Function(
            self,
            app_name + '-LambdaHandler',
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.from_asset(code_path),
            handler='handler.lambda_handler',
            timeout=Duration.seconds(30),
        )

        # Create an API Gateway REST API
        apigw =apigateway.LambdaRestApi(
            self,
            app_name + '-ApiGateway',
            handler=lambda_handler,
            deploy_options=apigateway.StageOptions(
                stage_name='staging'    # you can change to prod
            )
        )
