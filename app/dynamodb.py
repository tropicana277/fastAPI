import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)

print("### main.py imported ###", flush=True)

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)


def get_table():
    try:
        dynamodb = boto3.resource(
            "dynamodb",
            region_name="ap-northeast-1",
        )

        table = dynamodb.Table("Users")

        # ❗ 起動時ではなく、必要なときだけ軽く確認したい場合
        # table.load() は通常は呼ばない

        return table

    except ClientError as e:
        logger.exception("❌ DynamoDB ClientError")
        raise RuntimeError("DynamoDB access failed") from e

    except Exception as e:
        logger.exception("❌ Unexpected DynamoDB initialization error")
        raise


# def get_table():
#     dynamodb = boto3.resource("dynamodb", region_name="ap-northeast-1")
#     return dynamodb.Table("Users")


# dynamodb = boto3.resource("dynamodb", region_name="ap-northeast-1")

# table = dynamodb.Table("Users")
