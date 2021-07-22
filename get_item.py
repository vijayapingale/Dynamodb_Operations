import boto3

client = boto3.client('dynamodb')
resource = boto3.resource('dynamodb')

### Get Item
table =resource.Table("Family")

def getitem(event,context):
    print("HiHiHi")
    try:
        # TODO: write code...
        print("Good Morning")
        response = table.get_item(
            Key= {
            # Primary_Key_Column : Primary_Key_Value
                'Age' : '38'
            }
        )
        print(response)
    except Exception as e:
        print('Get item from table exception:  ',e)
        return