import boto3

aws_console = boto3.session.Session(profile_name = "python_user")
iam_users = aws_console.resource(service_name = "iam")

for each_user in iam_users.users.all():
    print(each_user.name)
