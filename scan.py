import boto3
from boto3.dynamodb.conditions import Key, Attr

client = boto3.client('dynamodb')
resource = boto3.resource('dynamodb')

### Get Item
table =resource.Table("Family")

def scanitem(event,context):
    print("-----Scan Here-----")
    try:
        # TODO: write code...
        print("Good Night")
        response = table.scan(
                FilterExpression=Key('Age').gt('32')
        )
        items = response['Items']
        for item in items:
            print(item)
    
    except Exception as e:
        print('Get item from table exception:  ',e)
        return