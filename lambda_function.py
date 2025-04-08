import json

# def lambda_handler(event, context):
#     print("Event:", event)
    
#     return {
#         'statusCode': 200,
#         'body': json.dumps({'message': 'Hello from Python Lambda!', 'input': event})
#     }
import json
import requests

def lambda_handler(event, context):
    try:
        # Making a GET request to a public API (e.g., JSONPlaceholder)
        response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
        
        # If the request was successful
        if response.status_code == 200:
            post_data = response.json()  # Get the JSON response
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'message': 'Data fetched from API successfully!',
                    'post': post_data
                })
            }
        else:
            return {
                'statusCode': response.status_code,
                'body': json.dumps({'message': 'Failed to fetch data from API'})
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'An error occurred', 'error': str(e)})
        }
