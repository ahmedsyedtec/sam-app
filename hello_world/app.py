import json
import boto3


# if 'Items' in response:
#     items = [item['id']['S'] for item in response['Items']]
#     print(items)
def hello_param(payload):
    greeting = json.loads(payload).get("greetPerson")
    dynamodb_client = boto3.client('dynamodb')
    dynamodb_client.put_item(TableName='UserData', Item={'id': {'S': greeting}})
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"hello {greeting}",
        }),
    }


def lambda_handler(event, context):
    print(event)
    return hello_param(event.get("body"))


if __name__ == '__main__':
    hello_param("{\n  \"greetPerson\": \"iiiiiii\"\n}")
