import boto3

def get_instance_ips_from_asg(asg_name, region_name):
    """
    Get IP addresses of instances in the specified Auto Scaling Group.

    :param asg_name: Name of the Auto Scaling Group.
    :param region_name: AWS region name where the Auto Scaling Group exists.
    :return: List of IP addresses of instances in the Auto Scaling Group.
    """
    ec2_client = boto3.client('ec2', region_name=region_name)
    asg_client = boto3.client('autoscaling', region_name=region_name)

    # Get the instance IDs of instances in the Auto Scaling Group
    response = asg_client.describe_auto_scaling_groups(AutoScalingGroupNames=[asg_name])
    instance_ids = [instance['InstanceId'] for instance in response['AutoScalingGroups'][0]['Instances']]

    # Get the IP addresses of instances
    ips = []
    if instance_ids:
        response = ec2_client.describe_instances(InstanceIds=instance_ids)
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                ips.append(instance['PrivateIpAddress'])  # Change to 'PublicIpAddress' if you need public IPs

    return ips

# Example usage:
asg_name = 'your_asg_name'
region_name = 'your_region_name'
instance_ips = get_instance_ips_from_asg(asg_name, region_name)
print("Instance IP addresses:", instance_ips)
