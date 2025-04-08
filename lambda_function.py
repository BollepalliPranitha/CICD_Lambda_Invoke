# import json
# import requests
import pandas as pd
import boto3
import os
# def lambda_handler(event, context):
#     print("Event:", event)
    
#     return {
#         'statusCode': 200,
#         'body': json.dumps({'message': 'Hello from Python Lambda!', 'input': event})
#     }


# def lambda_handler(event, context):
#     try:
#         # Making a GET request to a public API (e.g., JSONPlaceholder)
#         response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
        
#         # If the request was successful
#         if response.status_code == 200:
#             post_data = response.json()  # Get the JSON response
#             return {
#                 'statusCode': 200,
#                 'body': json.dumps({
#                     'message': 'Data fetched from API successfully!',
#                     'post': post_data
#                 })
#             }
#         else:
#             return {
#                 'statusCode': response.status_code,
#                 'body': json.dumps({'message': 'Failed to fetch data from API'})
#             }
#     except Exception as e:
#         return {
#             'statusCode': 500,
#             'body': json.dumps({'message': 'An error occurred', 'error': str(e)})
#         }


# Initialize S3 client
s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Bucket and file details
    bucket_name = 'sn-bd-test'
    file_key = 'car_dataset.csv'
    
    # Download the file from S3
    s3.download_file(bucket_name, file_key, '/tmp/car_dataset.csv')
    
    # Read the CSV file using pandas
    df = pd.read_csv('/tmp/car_dataset.csv')
    
    # Get the first 5 rows of the DataFrame
    result = df.head()

    # Convert the DataFrame to JSON format and return it as a response
    return {
        'statusCode': 200,
        'body': result.to_json(orient='split')  # You can choose other formats like 'records' or 'index'
    }