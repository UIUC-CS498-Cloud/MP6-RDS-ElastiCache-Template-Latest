import redis

REDIS_URL = ""

def lambda_handler(event, context):
    """Lambda handler to retrieve a value from Redis based on the provided key."""


    try:
        redis_client = redis.from_url(REDIS_URL)

        key = str(event['key'])
        value = redis_client.get(key)

        return {
            "body": value,
            "statusCode": 200
        }

    except Exception as e:
        print(f"Error occurred: {e}")
        return {
            "body": str(e),
            "statusCode": 500
        }
