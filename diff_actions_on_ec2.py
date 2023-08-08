import boto3
import sys

aws_console = boto3.session.Session(profile_name = "python_user")
ec2_console_re = aws_console.resource(service_name = "ec2", region_name = "ap-south-1")
ec2_console_cli = aws_console.client(service_name = "ec2", region_name = "ap-south-1")

while True:
    print("this script performs the following actions on ec2 instances")
    print("""
    1.start
    2.stop
    3.terminate
    4.exit
    """)

    opt=int(input("enter your options: "))

    if opt == 1:
        instance_id = input('enter your ec2 instance id: ')
        my_req_inst_obj = ec2_console_re.Instance(instance_id)
        #print(dir(my_req_inst_obj))
        print("starting ec2 instance.....")
        my_req_inst_obj.start()
    if opt == 2:
        instance_id = input('enter your ec2 instance id: ')
        print("stopping ec2 instance.....")
        my_req_inst_obj = ec2_console_re.Instance(instance_id)
        my_req_inst_obj.stop()
    if opt == 3:
        instance_id = input('enter your ec2 instance id: ')
        print("terminate ec2 instance.....")
        my_req_inst_obj = ec2_console_re.Instance(instance_id)
        my_req_inst_obj.terminate()
    if opt == 4:
        print("thank you for using this script")
        sys.exit()
    else:
        print("your option is invalid. please try once again")
