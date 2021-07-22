import boto3
import json
from boto3.dynamodb.conditions import Key, Attr

client = boto3.client('dynamodb')
resource = boto3.resource('dynamodb')

### How to Get data using query from DynamoDb
table =resource.Table("Family")

def querygetitem(event,context):
    print("How are you?")
    try:
        # TODO: write code...
        print("Good bye!!!")
        
        response = table.query(
            KeyConditionExpression=Key('Age').eq('2') 
        )
        print(response)
    except Exception as e:
        print('Query item from table exception:  ',e)
        return
    


