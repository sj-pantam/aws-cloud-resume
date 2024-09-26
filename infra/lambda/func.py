import json
import boto3

# Initialize the DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('cloudresume-test')

def lambda_handler(event, context):
    # Define key for the item to retrieve
    key = {
        'id': '0'   # Partition key
    }
    
    # Get item from DynamoDB table
    response = table.get_item(Key=key)
    views = response['Item']['views']
    views = views + 1
    print(views)
    respose = table.put_item(Item={
        'id': '0',
        'views': views
    })
    return views