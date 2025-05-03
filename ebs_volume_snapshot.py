import boto3
from datetime import datetime, timezone


def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    today = datetime.now(timezone.utc).date()

    # List all of the active ec2 instances

    instance_response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values':['running']}])
    
    # Get all the volume Ids attached to the active instances

    volume_ids = set()

    for reservation in instance_response['Reservations']:
        for instance in reservation['Instances']:
            for block_device in instance.get('BlockDeviceMappings', []):
                if 'Ebs' in block_device:
                    volume_ids.add(block_device["Ebs"]["VolumeId"])
    
    # For each volume , check if the snapshot exists today and if not, create it

    for volume_id in volume_ids:
        snapshot = ec2.describe_snapshots(Filters=[{'Name': 'volume-id', 'Values': [volume_id]}], OwnerIds=['self'])["Snapshots"]
        if snapshot:
            for snap in snapshot:
                if snap["StartTime"].date() == today:
                    print(f'Snapshot {snap["SnapshotId"]} already exists for the volume {volume_id} today.')
                    break
            else:
                #create a new snapshot if it does not exist today
                instance_response = ec2.create_snapshot(VolumeId=volume_id, Description=f"Snapshot of {volume_id} taken on {today}")
                print(f'Created a snapshot {instance_response["SnapshotId"]} for volume {volume_id} today.')

    