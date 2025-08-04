import json


def generatePolicy(principalId, effect, resource):
    return {
  "principalId": principalId,
  "policyDocument":{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Statement1",
      "Effect": effect,
      "Action": [
        "execute-api:Invoke"
      ],
      "Resource": resource
    }
  ]
  }

  }
  

def lambda_handler(event, context):
  print('TestEvent:',event)

  token = event.get('authorizationToken')
  if token == 'test123':
    return generatePolicy('user123', 'Allow', event.get('methodArn'))
  else:
    return generatePolicy('user123', 'Deny', event.get('methodArn'))

