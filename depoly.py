import boto3

s3 = boto3.client('s3')

s3.upload_file('index.html', 'shrihair1234567', 'index.html')
