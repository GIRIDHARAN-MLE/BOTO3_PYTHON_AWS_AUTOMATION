import boto3

aws_console = boto3.session.Session(profile_name = "python_user")

#iam, ec2, and s3 using client object

iam_console = aws_console.client(service_name = "iam", region_name = "us-east-1")
ec2_console = aws_console.client(service_name = "ec2", region_name = "us-east-1")
s3_console = aws_console.client(service_name = "s3", region_name = "us-east-1")

#list all the iam_users using client object

response = iam_console.list_users()

for each_items in response['Users']:
    print(each_items['UserName'])

#list of all ec2_ids

response = ec2_console.describe_instances()

for each_ids in response['Reservations']:
    for each_ins_ids in each_ids['Instances']:
        print(each_ins_ids['InstanceId'])

#list all the s3_buckets using client object

response = s3_console.list_buckets()

for each_buc_data in response['Buckets']:
    print(each_buc_data['Name'])



