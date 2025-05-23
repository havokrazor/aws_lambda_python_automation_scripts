# AWS Automation Scripts

1. Automated EC2 Instance Backup & Termination
Task: Identify EC2 instances with a specific tag (e.g., Backup: True), create AMIs of those instances, and terminate them if they have not been used in X days.

Tools: boto3, datetime, tag filters

2. Unused Elastic IP Cleanup
Task: Identify Elastic IPs that are not associated with any running instance and release them.

Why?: Avoid unnecessary charges.

3. S3 Bucket Cleanup
Task: Find and delete S3 buckets that are older than X days and not in use (e.g., no new files in the last 30 days).

Bonus: Add a “dry run” option before deletion.

4. Automated IAM User Audit
Task: Generate a report of all IAM users, their last login, attached policies, and whether MFA is enabled.

Optional: Disable users who haven’t logged in for X days.

5. CloudWatch Alarm Creator
Task: Automatically create CloudWatch alarms for CPU and memory utilization for all running EC2 instances.

Bonus: Send notifications to an SNS topic.

6. Lambda Function Deployment Script
Task: Write a script that packages Python code, creates a Lambda function, and updates its code on changes.

Useful For: Continuous deployment of serverless functions.

7. Auto-Scale Group Health Check
Task: Check if instances in an ASG are unhealthy and replace them.

Bonus: Integrate with SNS for alerts.

8. RDS Snapshot and Cleanup
Task: Take automated snapshots of RDS instances, and delete old snapshots older than N days.

9. Security Group Rules Audit
Task: Find all security groups with wide-open rules (e.g., 0.0.0.0/0 on port 22 or 3389) and report them.

Bonus: Remove unsafe rules automatically if configured.

10. Tag Enforcement Script
Task: Enforce that all EC2 instances, volumes, and buckets have certain required tags (Environment, Owner, etc.). Alert or terminate non-compliant resources.

11. Automated Docker Image Builder & ECR Pusher
Task: Build Docker images using Python and push them to Amazon ECR.

12. Infrastructure Drift Detector
Task: Compare deployed EC2 instances or IAM policies with a YAML/JSON configuration and report drift.

13. Terraform Plan Executor Wrapper
Task: Create a Python wrapper around Terraform commands to handle plan, apply, and destroy automatically with logging.
