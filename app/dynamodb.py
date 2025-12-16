import boto3


def get_table():
    dynamodb = boto3.resource("dynamodb", region_name="ap-northeast-1")
    return dynamodb.Table("Users")


# dynamodb = boto3.resource("dynamodb", region_name="ap-northeast-1")

# table = dynamodb.Table("Users")
