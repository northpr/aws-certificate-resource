import json, os
from download import download_file
from upload import upload_s3, get_client

def lambda_handler(event, context):
    # TODO implement
    file = "2023-01-30-0.json.gz"
    download_res = download_file(file)
    bucket = os.environ.get('BUCKET_NAME')
    os.environ.setdefault('default', 'ntv-github')
    upload_res = upload_s3(
        body=download_res.content, 
        bucket=bucket,
        file_name=file)
    return upload_res