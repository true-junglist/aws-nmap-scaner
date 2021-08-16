import boto3
from botocore.exceptions import ClientError

id = 'i-06edd4f2a87e541a8'
action = 'ON'
region = 'eu-west-1'

ec2 = boto3.client('ec2', region)



if action == 'ON':
    # Do a dryrun first to verify permissions
    try:
        ec2.start_instances(InstanceIds=[id], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise

    # Dry run succeeded, run start_instances without dryrun
    try:
        response = ec2.start_instances(InstanceIds=[id], DryRun=False)
        # print(response)
    except ClientError as e:
        print(e)
else:
    # Do a dryrun first to verify permissions
    try:
        ec2.stop_instances(InstanceIds=[id], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise

    # Dry run succeeded, call stop_instances without dryrun
    try:
        response = ec2.stop_instances(InstanceIds=[id], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)

def get_public_ip(instance_id):
    ec2_client = boto3.client("ec2", region)
    reservations = ec2_client.describe_instances(InstanceIds=[instance_id]).get("Reservations")

    for reservation in reservations:
        for instance in reservation['Instances']:
            print(instance.get("PublicIpAddress"))
get_public_ip(id)