import json

def lambda_handler(event, context):
    print("Event:", event)
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Hello from Python Lambda!', 'input': event})
    }
