import boto3
import time

aws_console = boto3.session.Session(profile_name = "python_user")
ec2_console_re = aws_console.resource(service_name = "ec2", region_name = "ap-south-1")
ec2_console_client = aws_console.client(service_name = "ec2", region_name = "ap-south-1")

my_inst_obj = ec2_console_re.Instance("i-0283ebf1a88da5dc0")
print("starting the instance ..")
my_inst_obj.start()
waiter = ec2_console_client.get_waiter('instance_running')
waiter.wait(InstanceIds=["i-0283ebf1a88da5dc0"]) #400 checks after 15 seconds
print("now your instance is up and running")


'''
print("starting ec2 instance ..")
ec2_console_client.start_instances(InstanceIds=["i-0283ebf1a88da5dc0"])
waiter = ec2_console_client.get_waiter('instance_running')
waiter.wait(InstanceIds=["i-0283ebf1a88da5dc0"]) #400 checks after 15 seconds
print("now your instance is up and running")
'''

'''
my_inst_obj = ec2_console_re.Instance("i-0283ebf1a88da5dc0")
print("starting the instance ..")
my_inst_obj.start()
my_inst_obj.wait_until_running()      #Resource waiter waits for 200 seconds(400 checks after 5 seconds)
print("now your instance is up and running")
'''

'''
while True:
    my_inst_obj = ec2_console_re.Instance("i-0283ebf1a88da5dc0")
    print("the current status of your ec2 is: ",my_inst_obj.state['Name'])
    if my_inst_obj.state['Name'] == "running":
        break
    print("waiting to get running status")
    time.sleep(5)
'''

