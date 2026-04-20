import boto3

s3 = boto3.client('s3')
s3.upload_file('index.html', 'my-static-site-1234556', 'index.html')
