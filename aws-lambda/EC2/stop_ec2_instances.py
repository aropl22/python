import boto3
def lambda_handler(event, context):
    region = 'us-east-1'
    instances = ['i-0f835c139e85ed775','i-0ca2614109846ee6b','i-0daeede57f90bb386']
    ec2 = boto3.client('ec2', region_name=region)
    ec2.stop_instances(InstanceIds=instances)
    for instance in instances:
        print('Stopped instance ID: ', instance)