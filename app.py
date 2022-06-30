#!/usr/bin/env python3

import aws_cdk as cdk

from athena_aws_test.athena_aws_test_stack import AthenaAwsTestStack


app = cdk.App()
AthenaAwsTestStack(app, "athena-aws-test")

app.synth()
