def lambda_handler(event, context):
    """
    Lambda function wrapper
    Args:
        event: trigger event dict
        context: lambda methods and properties
    Returns:
        string: greeting response
    Functions:
        Added two test functions test-function and Matrix
    """
    print("Starting functions\n.....................................")
    if event["input"] == "Hello":
        return "World"
    if event["input"] == "Hi":
        return "World"
    else:
        raise ValueError("Input must be Hello")