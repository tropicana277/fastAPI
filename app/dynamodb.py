import boto3
import os

dynamodb = boto3.resource("dynamodb", region_name="ap-northeast-1")

table = dynamodb.Table("Users")
