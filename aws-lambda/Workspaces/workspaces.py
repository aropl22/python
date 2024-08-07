#!/usr/bin/python3

import boto3


'''
############# Description ###########
response = client.create_workspaces(
    Workspaces=[
        {
            'DirectoryId': 'string',
            'UserName': 'string',
            'BundleId': 'string',
            'VolumeEncryptionKey': 'string',
            'UserVolumeEncryptionEnabled': True|False,
            'RootVolumeEncryptionEnabled': True|False,
            'WorkspaceProperties': {
                'RunningMode': 'AUTO_STOP'|'ALWAYS_ON',
                'RunningModeAutoStopTimeoutInMinutes': 123,
                'RootVolumeSizeGib': 123,
                'UserVolumeSizeGib': 123,
                'ComputeTypeName': 'VALUE'|'STANDARD'|'PERFORMANCE'|'POWER'|'GRAPHICS'|'POWERPRO'|'GRAPHICSPRO'
            },
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        },
    ]
)
'''

###################### END Description ####################


def lambda_handler(event, context):

    users = ('test1','test2');
    directoryID = 'd-90071d506c';
    bundleID = 'wsb-fcm454pk4d';
    client_TAG = 'C1';
    service_TAG = 'WS-C1'

    client = boto3.client('ds')
    response = client.describe_directories(DirectoryIds=[directoryID])

    if response['DirectoryDescriptions'][0]['Stage'] == 'Active':
        print ('AD Connector State: '+response['DirectoryDescriptions'][0]['Stage'])
        create_workspaces(users,directoryID,client_TAG,service_TAG,bundleID)
    else:
        print ('ERROR AD Connector State: '+response['DirectoryDescriptions'][0]['Stage'])

def create_workspaces(users,directoryID,client_TAG,service_TAG,bundleID):

    client = boto3.client('workspaces')

    for user in users:
        print ('Configuring workspace for user: '+user)
        Osi60workspace = client.create_workspaces(
            Workspaces=[
            {
            'DirectoryId': directoryID,
            'UserName': user,
            'BundleId': bundleID,
            #'VolumeEncryptionKey': 'string',
            'UserVolumeEncryptionEnabled': False,
            'RootVolumeEncryptionEnabled': False,
            'WorkspaceProperties': {
                'RunningMode': 'AUTO_STOP',
                'RunningModeAutoStopTimeoutInMinutes': 60,
                'RootVolumeSizeGib': 80,
                'UserVolumeSizeGib': 10,
                'ComputeTypeName': 'STANDARD'
            },
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'W-'+user
                },
                {
                    'Key': 'Client',
                    'Value': client_TAG
                },
                {
                    'Key': 'Type',
                    'Value': 'DR-WS'
                },
		{
                    'Key': 'Stack',
                    'Value': 'DR'
                },
		{
                    'Key': 'Service',
                    'Value': service_TAG
                },
            ]
        },
    ]
    )
    #print (user)


    if not Osi60workspace['FailedRequests']:
    # empty dictionaries evaluate to false!!!
        print ('User: '+Osi60workspace['PendingRequests'][0]['UserName']+' WorkspaceID: '+Osi60workspace['PendingRequests'][0]['WorkspaceId']+' State: '+Osi60workspace['PendingRequests'][0]['State'])
    else:
        print ('User: '+user+' Error Code : '+Osi60workspace['FailedRequests'][0]['ErrorCode']+' '+Osi60workspace['FailedRequests'][0]['ErrorMessage'])

if __name__ == "__main__":
        lambda_handler({}, {})