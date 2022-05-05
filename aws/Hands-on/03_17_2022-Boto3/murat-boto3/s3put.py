import boto3

s3 = boto3.resource('s3')

data = open('test.txt', 'rb')
s3.Bucket('huseyin-boto3').put_object(Key='test.txt', Body=data)
