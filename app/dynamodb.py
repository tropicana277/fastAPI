import boto3
import logging


logger = logging.getLogger(__name__)


def get_table():
    try:
        dynamodb = boto3.resource("dynamodb", region_name="ap-northeast-1")
        table = dynamodb.Table("Users")

        # ここで明示的に存在・権限チェック
        table.load()

        return table

    except Exception as e:
        logger.exception("❌ DynamoDB initialization failed")
        raise


# def get_table():
#     dynamodb = boto3.resource("dynamodb", region_name="ap-northeast-1")
#     return dynamodb.Table("Users")


# dynamodb = boto3.resource("dynamodb", region_name="ap-northeast-1")

# table = dynamodb.Table("Users")
