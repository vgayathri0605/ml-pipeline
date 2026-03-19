import boto3
import os

def download_latest_file(bucket_name, prefix, download_path):
    s3 = boto3.client("s3")

    # list files in bucket
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

    if "Contents" not in response:
        raise Exception("No files found in S3")

    files = response["Contents"]

    # find latest file
    latest_file = max(files, key=lambda x: x["LastModified"])

    file_key = latest_file["Key"]
    filename = os.path.basename(file_key)

    local_path = os.path.join(download_path, filename)

    # download file
    s3.download_file(bucket_name, file_key, local_path)

    return local_path, filename