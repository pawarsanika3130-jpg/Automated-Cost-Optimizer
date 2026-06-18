# Automated AWS Cost Optimizer

## Project Overview

Automated AWS Cost Optimizer is a serverless cloud automation project that helps reduce AWS infrastructure costs by automatically detecting and stopping underutilized Amazon EC2 instances.

The solution uses AWS Lambda, Amazon CloudWatch, Amazon EventBridge, and Python (boto3) to monitor EC2 CPU utilization and take automated actions when instances remain idle.

---

## Architecture

EventBridge triggers the Lambda function on a scheduled basis.

Lambda retrieves CPU utilization metrics from CloudWatch for all running EC2 instances.

If the average CPU utilization is below the configured threshold (5%), Lambda automatically stops the EC2 instance.

All execution logs are stored in CloudWatch Logs.

Optional SNS integration can send email notifications whenever an instance is stopped.

---

## AWS Services Used

* AWS Lambda
* Amazon EC2
* Amazon CloudWatch
* Amazon EventBridge
* AWS IAM
* Amazon SNS (Optional)

---

## Project Workflow

1. EventBridge triggers Lambda every hour.
2. Lambda retrieves running EC2 instances.
3. CloudWatch CPU metrics are analyzed.
4. If CPU utilization is below 5%, the instance is identified as idle.
5. Lambda automatically stops the EC2 instance.
6. CloudWatch stores execution logs.
7. Optional SNS notifications are sent to administrators.

---

## Features

* Automated EC2 cost optimization
* Serverless architecture
* CloudWatch metric monitoring
* Scheduled automation using EventBridge
* Automatic EC2 shutdown
* Optional email notifications using SNS
* Secure IAM-based permissions

---

## Prerequisites

* AWS Account
* IAM Role with EC2 and CloudWatch permissions
* Running EC2 instance
* Python 3.x
* boto3

---

## IAM Permissions

The Lambda function requires permissions to:

* Describe EC2 instances
* Stop EC2 instances
* Read CloudWatch metrics
* Create CloudWatch logs

Recommended Policies:

* AmazonEC2FullAccess
* CloudWatchLogsFullAccess

---

## Lambda Function

The Lambda function performs the following actions:

* Retrieves all running EC2 instances
* Fetches CPU utilization metrics
* Compares utilization against the threshold
* Stops idle instances automatically

---

## Example Output

i-03ea41e28f9d07265 CPU Usage: 0.80%

Stopping i-03ea41e28f9d07265

---

## Project Structure

Automated-Cost-Optimizer/

├── lambda_function.py

├── README.md

├── architecture-diagram.png

├── requirements.txt

└── screenshots/

```
├── lambda-success.png

├── cloudwatch-logs.png

├── ec2-instance.png

└── eventbridge-rule.png
```

---

## Results

* Automated monitoring of EC2 resources
* Reduced unnecessary cloud costs
* Eliminated manual intervention
* Demonstrated serverless automation using AWS services

---

## Future Enhancements

* Start instances automatically during business hours
* Tag-based instance management
* Slack notifications
* Cost reporting dashboard
* Multi-account support

---

## Author

Sanika Pawar

AWS Cloud & Python Enthusiast

