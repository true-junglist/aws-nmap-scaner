#coding=utf-8
import nmap
import json
import boto3
import boto3.utils


# class Port(object):
#     """docstring for Port"""
#     def __init__(self, ip):
#         self.state = 'unscan' #未扫描
#         self.ip = ip
#         self.report = ''
#
#     def port_scan(self,):
#         host = self.ip
#         nm = nmap.PortScanner()
#         self.state = 'scanning'
#         try:
#             nm.scan(host) #arguments='-T5 -p 1-65535 -sV -sT -Pn --host-timeout 3600'
#             ports = nm[host]['tcp'].keys()
#             report_list = []
#             for port in ports:
#                 report = {}
#                 state = nm[host]['tcp'][port]['state']
#                 service = nm[host]['tcp'][port]['name']
#                 product = nm[host]['tcp'][port]['product']
#                 report['port'] = port
#                 report['state'] = state
#                 report['service'] = service
#                 report['product'] = product
#                 if state == 'open':
#                     report_list.append(report)
#             print (report_list)
#             self.state = 'scanned'
#             self.report = json.dumps(report_list)
#             return json.dumps(report_list)
#         except Exception as e:
#             print (e)

# for host in nm.all_hosts():
ip = '34.246.131.34'


# initialize the port scanner
nmScan = nmap.command_line('nmap -oX - -p 22-443 -sV 127.0.0.1')

# scan localhost for ports in range 21-443
# nmScan.scan(ip, '21-443')
print(nmScan['scan'])
# run a loop to print all the found result about the ports
# for host in nmScan.all_hosts():
#     print('Host : %s (%s)' % (host, nmScan[host].hostname()))
#     print('State : %s' % nmScan[host].state())
#     for proto in nmScan[host].all_protocols():
#         print('----------')
#         print('Protocol : %s' % proto)
#
#         lport = nmScan[host][proto].keys()
#         lport.sort()
#         for port in lport:
#             print('port : %s\tstate : %s' % (port, nmScan[host][proto][port]['state'])



# client = boto3.client('ec2', region_name='eu-west-1')
# client = boto3.client('ec2')

# response = client.describe_instances(MaxResults=20,)
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

def create_conn(aws_access_key, aws_secret_key, ec2_region):
    conn = boto3.client('ec2', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=ec2_region)
    return conn

def handler(context, inputs):
    ec2 = boto3.resource('ec2')
    filters = [{
        'Name': 'instance-state-name',
        'Values': ['running']
    }]

    instances = ec2.instances.filter(Filters=filters)
    for instance in instances:
        print('Instance: ' + instance.id)