import boto3
import boto3.utils

client = boto3.client('ec2', region_name='eu-west-1')
# client = boto3.client('ec2')

response = client.describe_instances(
    MaxResults=20,
)

for r in response['Reservations']:
    for i in r['Instances']:
        tag_values_list = []
        for tags in i['Tags']:
            for key, value in tags.items():
                tag_values_list.append(value)
                print('id:', i['InstanceId'], 'zone:', i['Placement']['AvailabilityZone'], 'state:', i['State']['Name'],
                      i['PublicIpAddress'],
                      'tags:',
                      tag_values_list)

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
