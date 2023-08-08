import boto3

aws_console = boto3.session.Session(profile_name = "python_user")

sts_console = aws_console.client(service_name = "iam", region_name = "ap-south-1")
response = sts_console.get_caller_identity()
print(response['Account]')
