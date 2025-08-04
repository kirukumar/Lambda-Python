import json

def userDetails(token):
  return {
    "id": "123",
    "name": "John Doe",
    "email": "john.doe@example.com",
    "role": "admin"
  }

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
  },
  "context": userDetails(principalId)
  }
  

def lambda_handler(event, context):
  print('TestEvent:',event)

  token = event.get('authorizationToken')
  if token == 'test123':
    return generatePolicy('user123', 'Allow', event.get('methodArn'))
  else:
    return generatePolicy('user123', 'Deny', event.get('methodArn'))

