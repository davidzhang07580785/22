import boto3

def start_ec2_instance(instance_id):
    ec2 = boto3.client('ec2')
    ec2.start_instances(InstanceIds=[instance_id])
    print(f"EC2 instance {instance_id} started.")

def stop_ec2_instance(instance_id):
    ec2 = boto3.client('ec2')
    ec2.stop_instances(InstanceIds=[instance_id])
    print(f"EC2 instance {instance_id} stopped.")

def reboot_ec2_instance(instance_id):
    ec2 = boto3.client('ec2')
    ec2.reboot_instances(InstanceIds=[instance_id])
    print(f"EC2 instance {instance_id} rebooted.")

# 调用函数控制 EC2 实例开关状态
instance_id = 'i-00c9885624a277f1c'
start_ec2_instance(instance_id)
stop_ec2_instance(instance_id)
reboot_ec2_instance(instance_id)