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



#---
import boto3

def get_target_group_health(target_group_arn, region_name):
    """
    Get information about the health of targets registered with the specified target group.

    :param target_group_arn: ARN of the target group.
    :param region_name: AWS region name where the target group exists.
    :return: Dictionary containing information about healthy and unhealthy targets.
    """
    elbv2_client = boto3.client('elbv2', region_name=region_name)

    # Get target health information
    response = elbv2_client.describe_target_health(TargetGroupArn=target_group_arn)

    healthy_targets = []
    unhealthy_targets = []

    # Process target health information
    for target_health in response['TargetHealthDescriptions']:
        target_id = target_health['Target']['Id']
        target_health_state = target_health['TargetHealth']['State']

        if target_health_state == 'healthy':
            healthy_targets.append(target_id)
        else:
            unhealthy_targets.append(target_id)

    return {
        'healthy': healthy_targets,
        'unhealthy': unhealthy_targets
    }

# Example usage:
target_group_arn = 'your_target_group_arn'
region_name = 'your_region_name'
target_health_info = get_target_group_health(target_group_arn, region_name)
print("Healthy targets:", target_health_info['healthy'])
print("Unhealthy targets:", target_health_info['unhealthy'])
