#!/usr/bin/env python3
import os
import aws_cdk as cdk
from infra.infra_stack import FlaskStack

# Define parameters
APP_NAME = 'SimpleApp'
BACKEND_CODE_PATH = '../src/' + os.environ["ZAPPA_LAMBDA_PACKAGE"]
AWS_ACCOUNT= '527018699300'
AWS_REGION = 'us-west-2'

app = cdk.App()

# Deploy APIs
FlaskStack(app, "FlaskStack",
    env=cdk.Environment(account=AWS_ACCOUNT, region=AWS_REGION),
    app_name=APP_NAME,
    code_path=BACKEND_CODE_PATH
)

app.synth()