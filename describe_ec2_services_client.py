import boto3
from pprint import pprint

aws_console = boto3.session.Session(profile_name = "python_user")
ec2_console = aws_console.client(service_name = "ec2", region_name = "ap-south-1")

response = ec2_console.describe_instances()['Reservations']
for each_item in response:
    for each_instance in each_item['Instances']:
        print("The image id is: {}\nThe instances id is: {}\nThe instances launch time is: {}".format(each_instance['ImageId'], each_instance[ 'InstanceId'], each_instance['LaunchTime'].strftime("%Y-%m-%d")))

response_volume = ec2_console.describe_volumes()['Volumes']
for each_instance_volumes in response_volume:
    print("The volume id is : {}\nThe AvailabilityZone is : {}\nThe VolumeType is : {}".format(each_instance_volumes['VolumeId'], each_instance_volumes['AvailabilityZone'], each_instance_volumes['VolumeType']))
