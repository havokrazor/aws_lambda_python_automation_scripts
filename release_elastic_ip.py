# This Lambda function releases all Elastic IPs that are not associated with any EC2 instance.
# It uses the Boto3 library to interact with AWS EC2 service.

import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    # Get the list of all Elastic IPs
    response_addresses = ec2.describe_addresses()
    # Loop through the addresses and release the ones that are not associated with any instance
    for address in response_addresses['Addresses']:
        if 'InstanceId' not in address:
            print(f"Releasing Elastic IP : {address['PublicIp']}")
            try:
                ec2.release_address(AllocationId=address['AllocationId'])
                print(f"Elastic IP {address['PublicIp']} released successfully.")
            except Exception as e:
                # Handle the exception if the release fails , the str(e) will give the error message
                print(f"Error releasing Elastic IP {address['PublicIp']} : {str(e)}")
        else:
            print(f"Elastic IP {address['PublicIp']} is associated with instance {address['InstanceId']}")
            

