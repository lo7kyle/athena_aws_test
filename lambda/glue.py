# Glue Handler Code that starts Glue Job
from textwrap import indent
import json
import os

import boto3

client = boto3.client('glue')


def handler(event, context):
    glueJobName = os.environ['JOB_NAME']
    response = client.start_job_run(
        JobName=glueJobName,
        Timeout=10
    )
    print('--------------------------------------')
    print(json.dumps(response, indent=4))
    return True