import boto3
from collections import defaultdict


# List all regions
client = boto3.client('ec2')
regions = [region['RegionName'] for region in client.describe_regions()['Regions']]


"""
A function for retrieving basic information from the running EC2 instances.
"""
def running_in_region(region):
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

for r in regions:
    running_in_region(r)