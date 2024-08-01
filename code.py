import boto3
from datetime import datetime, timedelta

def monitor_ec2_cpu_utilization(instance_id):
    cloudwatch = boto3.client('cloudwatch')

    response = cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': instance_id
            },
        ],
        Statistics=['Average'],
        StartTime=datetime.utcnow() - timedelta(minutes=5),
        EndTime=datetime.utcnow(),
        Period=60
    )

    cpu_utilization = response['Datapoints'][0]['Average']
    print(f"CPU utilization for instance {instance_id}: {cpu_utilization}%")

if __name__ == "__main__":
    instance_id = "your_instance_id"  # Replace with your instance ID
    monitor_ec2_cpu_utilization(instance_id)
