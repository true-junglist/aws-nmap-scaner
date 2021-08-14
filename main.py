

import sys
# import nmap3
import boto3
from collections import defaultdict
from botocore.exceptions import ClientError

instance_id = 'i-06edd4f2a87e541a8'
action = ''
region = 'eu-west-1'

# ec2 = boto3.client('ec2', region)

# if action == 'ON':
#     # Do a dryrun first to verify permissions
#     try:
#         ec2.start_instances(InstanceIds=[instance_id], DryRun=True)
#     except ClientError as e:
#         if 'DryRunOperation' not in str(e):
#             raise
#
#     # Dry run succeeded, run start_instances without dryrun
#     try:
#         response = ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
#         print(response)
#     except ClientError as e:
#         print(e)
# else:
#     # Do a dryrun first to verify permissions
#     try:
#         ec2.stop_instances(InstanceIds=[instance_id], DryRun=True)
#     except ClientError as e:
#         if 'DryRunOperation' not in str(e):
#             raise
#
#     # Dry run succeeded, call stop_instances without dryrun
#     try:
#         response = ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
#         print(response)
#     except ClientError as e:
#         print(e)

"""
A tool for retrieving basic information from the running EC2 instances.
"""


# Connect to EC2
ec2r = boto3.resource('ec2', region)

# Get information for all running instances
running_instances = ec2r.instances.filter(Filters=[{
    'Name': 'instance-state-name',
    'Values': ['running']}])

ec2info = defaultdict()
for instance in running_instances:
    # for tag in instance.tags:
    for tag in instance.tags:
        if 'Name'in tag['Key']:
            name = tag['Value']
    # Add instance info to a dictionary
    assert isinstance(instance, object)
    ec2info[instance.id] = {
        'Name': name,
        'Type': instance.instance_type,
        'State': instance.state['Name'],
        'Private IP': instance.private_ip_address,
        'Public IP': instance.public_ip_address,
        'Launch Time': instance.launch_time,
        'Key pair name' : instance.key_name
        }

attributes = ['Name', 'Type', 'State', 'Private IP', 'Public IP', 'Launch Time', 'Key pair name']
for instance_id, instance in ec2info.items():
    for key in attributes:
        print("{0}: {1}".format(key, instance[key]))
    print("------")

for instance in running_instances:
    print(instance.public_ip_address)
# import boto3
# import boto3.utils
#
# client = boto3.client('ec2', region_name='eu-west-1')
# # client = boto3.client('ec2')
#
# response = client.describe_instances(
#     # MaxResults=20,
# )
#
# for r in response['Reservations']:
#     for i in r['Instances']:
#         tag_values_list = []
#         for tags in i['Tags']:
#             for key, value in tags.items():
#                 tag_values_list.append(value)
#                 print('id:', i['InstanceId'], 'zone:', i['Placement']['AvailabilityZone'], 'state:', i['State']['Name'],
#                       i['PublicIpAddress'],
#                       'tags:',
#                       tag_values_list)

# def create_conn(aws_access_key, aws_secret_key, ec2_region):
#     conn = boto3.client('ec2', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=ec2_region)
#     return conn

# def handler(context, inputs):
#     ec2 = boto3.resource('ec2')
#     filters = [{
#         'Name': 'instance-state-name',
#         'Values': ['running']
#     }]
#
#     instances = ec2.instances.filter(Filters=filters)
#     for instance in instances:
#         print('Instance: ' + instance.id)


# ec2 = boto3.client('ec2')
# response = ec2.describe_instances()
# print(response)
