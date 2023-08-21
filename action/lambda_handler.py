def lambda_handler(event, context):
    print("Starting functions\n.....................................")
    if event["input"] == "Hello":
        return "World"
    if event["input"] == "Hi":
        return "Hi There"
    else:
        raise

