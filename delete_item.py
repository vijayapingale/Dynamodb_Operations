import boto3

client = boto3.client('dynamodb')
resource = boto3.resource('dynamodb')

### Get Item
table =resource.Table("Family")

def deleteitem(event,context):
    print("Hmmm")
    try:
        # TODO: write code...
        print("Good Evening")
        Age = '58' 
        response = table.delete_item( 
            Key={ 
                'Age' : '58' 
            } 
        )
        response

    except Exception as e:
        print('Get item from table exception:  ',e)
        return