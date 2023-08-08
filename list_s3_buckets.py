import boto3

'''
aws_console = boto3.session.Session()
s3_console = aws_console.resource("s3")
'''

s3_console = boto3.resource(service_name = "s3",region_name = "us-east-1")
for each_buckets in s3_console.buckets.all():
    print(each_buckets.name)
