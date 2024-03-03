def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda, This is CI-CD pipeline example, added!'
    }
