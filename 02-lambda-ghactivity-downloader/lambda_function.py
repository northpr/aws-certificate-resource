import json
from download import download_file

def lambda_handler(event, context):
    # TODO implement
    download_res = download_file("2023-01-30-0.json.gz")
    return {
        'statusCode': download_res.status_code,
        'body': json.dumps('Hello from Lambda using gha downloader!')
    }