import json
import boto3

def lambda_handler(event, context):
    
    sf = boto3.client('stepfunctions', region_name = 'sa-east-1')
    response = sf.start_sync_execution(stateMachineArn = 'arn:aws:states:sa-east-1:{AWS_ACCOUNT_ID}:stateMachine:CompanyIntegrationTest')
    responseMsg = response['status']
    
    statusCode = 200
    if(responseMsg == "FAILED"):
        statusCode = 500

    return {
        'statusCode': statusCode,
        'body': responseMsg
    }

