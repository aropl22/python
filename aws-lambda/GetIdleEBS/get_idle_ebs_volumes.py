import boto3
import json

def get_idle_ebs_volumes(ec2_client):
    # Retrieve all EBS volumes
    response = ec2_client.describe_volumes()

    # List to store idle (unattached) volumes
    idle_volumes = []

    for volume in response['Volumes']:
        # Check if the volume is unattached
        if not volume['Attachments']:
            volume_id = volume['VolumeId']
            volume_size = volume['Size']
            volume_state = volume['State']
            creation_time = volume['CreateTime']

            idle_volumes.append({
                'VolumeId': volume_id,
                'Size (GiB)': volume_size,
                'State': volume_state,
                'CreationTime': str(creation_time)  # Convert datetime to string for JSON serialization
            })

    return idle_volumes


def lambda_handler(event, context):
    # Create an EC2 client using the default session in the Lambda environment
    ec2_client = boto3.client('ec2')

    idle_volumes = get_idle_ebs_volumes(ec2_client)

    if idle_volumes:
        print("Idle EBS Volumes:")
        for volume in idle_volumes:
            print(f"VolumeId: {volume['VolumeId']}, Size: {volume['Size (GiB)']} GiB, State: {volume['State']}, CreationTime: {volume['CreationTime']}")
        return {
            "statusCode": 200,
            "body": json.dumps(idle_volumes)  # Serialize list to JSON
        }
    else:
        print("No idle EBS volumes found.")
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "No idle EBS volumes found."})  # Return a JSON response
        }


# Example of Lambda event for local testing
if __name__ == "__main__":
    lambda_handler({}, {})

