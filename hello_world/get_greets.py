import json
import boto3

"""


"""
def get_list_from_db():
    dynamodb_client = boto3.client('dynamodb')
    response = dynamodb_client.scan(
        TableName='UserData', )
    items = []
    if "Items" in response:
        items = [item["id"]["S"] for item in response["Items"]]

    return {
        "statusCode": 200,
        "body": json.dumps(items)
    }


def lambda_handler(event, context):
    print(event)
    return get_list_from_db()
