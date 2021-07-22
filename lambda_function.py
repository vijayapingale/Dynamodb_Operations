import boto3
import json
from get_item import getitem
from put_item import putitem
from delete_item import deleteitem
from query import querygetitem
from scan import scanitem
    
def lambda_handler(event, context):
    try:
        print("### DingDong##")
        if(event['op'] == 'getitem'):
            return getitem(event, context)
        elif(event['op'] == 'putitem'):
            return putitem(event, context)
        elif(event['op'] == 'deleteitem'):
            return deleteitem(event, context)
        elif(event['op'] == 'querygetitem'):
            return querygetitem(event, context)   
        elif(event['op'] == 'scanitem'):
            return scanitem(event, context)
        
            
            
        return {'message':'exception','exception':'invalid option'}
    except Exception as e:
        print('get_item exception',str(e))
        return {'message':'exception','exception':str(e)}
    
    

    
    
