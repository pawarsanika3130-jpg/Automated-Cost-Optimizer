import boto3
from datetime import datetime, timedelta

ec2 = boto3.client('ec2')
cloudwatch = boto3.client('cloudwatch')

CPU_THRESHOLD = 5


def lambda_handler(event, context):

    instances = ec2.describe_instances()

    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:

            instance_id = instance['InstanceId']
            state = instance['State']['Name']

            if state != 'running':
                continue

            metrics = cloudwatch.get_metric_statistics(
                Namespace='AWS/EC2',
                MetricName='CPUUtilization',
                Dimensions=[
                    {
                        'Name': 'InstanceId',
                        'Value': instance_id
                    }
                ],
                StartTime=datetime.utcnow() - timedelta(hours=1),
                EndTime=datetime.utcnow(),
                Period=3600,
                Statistics=['Average']
            )

            datapoints = metrics['Datapoints']

            if datapoints:

                avg_cpu = datapoints[0]['Average']

                print(
                    f"{instance_id} CPU Usage: {avg_cpu}%"
                )

                if avg_cpu < CPU_THRESHOLD:

                    print(
                        f"Stopping {instance_id}"
                    )

                    ec2.stop_instances(
                        InstanceIds=[instance_id]
                    )

    return {
        'statusCode': 200
    }
