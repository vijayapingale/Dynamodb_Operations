import boto3

client = boto3.client('dynamodb')
resource = boto3.resource('dynamodb')

### Get Item
table =resource.Table("Family")

def putitem(event,context):
    print("Hello")
    try:
        # TODO: write code...
        print("Good Afternoon")
        table.put_item(
            Item= {
                'Age' : '2',
                'First_Name' : 'Gargi',
                'Last_Name' : 'Pingale',
                'Visa' : 'Citizen',
                'Age': '58',
                'First_Name' : 'Vandana',
                'Last_Name' : 'Pingale',
                'Visa' : 'Indian'
            }
        )
        # response = {"message" : "Item successfully added" }
       
    except Exception as e:
        print('Put item into table exception:  ',e)
        return