This is a proof of concept for my idea of sharing feature for Zotero.

handler.py contains "get" function to fetch entry from DynamoDB and "create" to add entry to DynamoDB if it is not already there.

Zotero web or desktop client would hit "create" endpoint with a json object {"collection_items" : [...]}, and the 
endpoint would return a url which the end user can send whoever.

This url opens up index.html which is a static website on AWS S3 to display the entries, format them and export via provided
web services.

This is currently deployed on a sample API gateway project. 
POST endpoint url is https://gjc8c0bh1d.execute-api.us-east-1.amazonaws.com/dev/new. Feel free to try it out.
