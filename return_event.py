import json
## Simple Hello World Lambda Function
def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps({'event': event})
    }
