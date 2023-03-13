This is a proof of concept for my idea of sharing feature for Zotero.

handler.py contains "get" function to fetch entry from DynamoDB and "create" to add entry to DynamoDB if it is not already there.

Zotero web or desktop client would hit "create" endpoint with a json object {"collection_items" : [...]}, and the 
endpoint would return a url which the end user can send whoever.

This received url opens up index.html which is a static website on AWS S3 to display the entries, format them and export via provided
web services. It uses the "get" endpoint to fetch data.

This is currently deployed on a sample API gateway project. 
POST endpoint url is https://gjc8c0bh1d.execute-api.us-east-1.amazonaws.com/dev/new. Feel free to try it out.

Here is a sample of a shared url the POST endpoint returns: http://zotero-sharing-demo-123456789.s3-website-us-east-1.amazonaws.com?key=e2fd95f2129ca472a15041431916d1792b3432dcd71bfc1ec770c22a3da04471
