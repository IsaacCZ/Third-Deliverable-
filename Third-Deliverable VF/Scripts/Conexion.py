#!/usr/bin/env python3

import boto3
import pathlib

AWS_REGION = "us-west-2"

client = boto3.client("s3", region_name=AWS_REGION)

response = client.list_buckets()





BASE_DIR = pathlib.Path(__file__).parent.resolve()

S3_BUCKET_NAME = response['Buckets'][0]["Name"]
print(S3_BUCKET_NAME)

s3_client = boto3.client("s3", region_name=AWS_REGION)

def upload_files(file_name, bucket, object_name=None, args=None):
    if object_name is None:
        object_name = file_name

    s3_client.upload_file(file_name, bucket, object_name, ExtraArgs=args)
    print(f"'{file_name}' has been uploaded to '{S3_BUCKET_NAME}'")

upload_files("/home/sknow/Documents/Wizeline/Data CSV/movie_review.csv", S3_BUCKET_NAME,"reviews")
upload_files("/home/sknow/Documents/Wizeline/Data CSV/user_purchase.csv", S3_BUCKET_NAME,'user_purchase')

print("BASE_DIR")