import json
import os
import boto3
import hashlib


TABLE = os.environ['TABLE']
ROOT_URL = os.environ['ROOT_URL']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE)


'''
GET - Retrieves existing collection items from the database.
Path parameter - key - is the hash key of the collection items
'''
def get(event,context):
    key = event['pathParameters']['key']
    result = table.get_item( Key={'key':  key })
    collection_items = result.get('Item')

    return {
        "statusCode" : 200,	
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers" : "*",
            },
        "body" : json.dumps(collection_items)
    }

'''
POST - Adds a list of entries from a shared collection to the database
if it is not already present.
Requires collection_items passed in request body
'''
def create(event,context):
    collection_items = json.loads(event['body']).get('collection_items')
    if collection_items is None:
        return {
            'statusCode' : 400,
            'body' : 'collection_items is missing'
        }
    hashed_key = hashlib.sha256(json.dumps(collection_items).encode()).hexdigest()
    check_if_exists = table.get_item( Key={'key':  hashed_key })
    comment = "Item already exists"

    if not check_if_exists.get('Item'):
        table.put_item(Item={'key' : hashed_key, 'items' :  collection_items })
        comment = "New item created"
    
    return  {
        "statusCode" : 200,
        'body' : json.dumps({ 
            'url' : f"{ROOT_URL}?key={hashed_key}",
            'comment' : comment 
            })
        }