import boto3

aws_console = boto3.session.Session(profile_name = "python_user")

#iam, ec2, and s3 using resource object


iam_console = aws_console.resource(service_name = "iam", region_name = "ap-south-1")
ec2_console = aws_console.resource(service_name = "ec2", region_name = "ap-south-1")
s3_console = aws_console.resource(service_name = "s3", region_name = "ap-south-1")

#list all the iam_users using resource object

for each_user in iam_console.users.all():
    print(each_user.user_name)

#list all the s3_buckets using resource object

for each_bucket in s3_console.buckets.all():
    print(each_bucket.name)

#list all the ec2_instances using resource object

for each_instance in ec2_console.instances.all():
    print(each_instance.instance_id)

