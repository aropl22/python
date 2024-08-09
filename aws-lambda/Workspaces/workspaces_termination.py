#!/usr/bin/python3
#!/usr/bin/python3

import boto3

def lambda_handler(event, context):

    workspaceID = 'ws-31d93wsky'

    client = boto3.client('workspaces')
    workspacesIDs = client.describe_workspaces()
    print(workspacesIDs)
    print (range(len(workspacesIDs['Workspaces'])))
    for i in range(len(workspacesIDs['Workspaces'])):
        print ('Terminating '+workspacesIDs['Workspaces'][i]['WorkspaceId'])
        client.terminate_workspaces(
        TerminateWorkspaceRequests=[
        {
            'WorkspaceId': workspacesIDs['Workspaces'][i]['WorkspaceId']
        },
        ]
        )
        print('Terminating workspace '+workspacesIDs['Workspaces'][i]['WorkspaceId'])
        
if __name__ == "__main__":
        lambda_handler({}, {})