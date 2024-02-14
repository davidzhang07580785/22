import boto3

def list_ec2_instances():
    # 创建 EC2 客户端
    ec2 = boto3.client('ec2')

    # 列出所有 EC2 实例
    response = ec2.describe_instances()

    # 提取实例信息
    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_details = {
                'InstanceId': instance['InstanceId'],
                'InstanceType': instance['InstanceType'],
                'State': instance['State']['Name']
            }
            instances.append(instance_details)

    # 打印实例信息
    for instance in instances:
        print(f"Instance ID: {instance['InstanceId']}")
        print(f"Instance Type: {instance['InstanceType']}")
        print(f"State: {instance['State']}")
        print('---')

# 调用函数列出 EC2 实例
list_ec2_instances()