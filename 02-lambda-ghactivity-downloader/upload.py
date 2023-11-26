import boto3

def get_client():
    return boto3.client("s3")

def upload_s3(body, bucket, file_name):
    s3_client = get_client()
    res = s3_client.put_object(
        Bucket= bucket,
        Key=file_name,
        Body=body
    )
    return res