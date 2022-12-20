import  boto3
dynamodb=boto3.resource('dynamodb')
table=dynamodb.Table('tracker')

response=table.update_item(
    Key={
        'tid':2,
        'name':'device2'
    },
    UpdateExpression="SET lat=:s",
    ExpressionAttributeValues={
        ':s':"11.12",
    },
    ReturnValues="UPDATED_NEW"


)
