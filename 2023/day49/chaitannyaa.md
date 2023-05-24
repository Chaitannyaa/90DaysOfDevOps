# Day 49 - INTERVIEW QUESTIONS ON AWS

Hey people, we have listened to your suggestions and we are looking forward to get more! 
As you people have asked to put more interview based questions as part of Daily Task, So here it it :)

## INTERVIEW QUESTIONS:
- Name 5 aws services you have used and what's the use cases?

a) AWS IAM: AWS IAM (Identity and Access Management) is a service provided by Amazon Web Services (AWS) that enables you to manage access to AWS resources securely. IAM allows you to create and manage users, groups, and roles, as well as control their permissions to access various AWS services and resources.

b) Amazon EC2 (Elastic Compute Cloud): It provides resizable compute capacity in the cloud and allows users to launch virtual machines (instances) to run their applications. It is widely used for hosting websites, running applications, and performing various computing tasks.

c) AWS Lambda: It is a serverless computing service that allows you to run your code without provisioning or managing servers. It is commonly used for event-driven applications, data processing, and executing code in response to triggers.

d) Amazon RDS (Relational Database Service): It is a managed database service that makes it easy to set up, operate, and scale a relational database in the cloud. It is used for hosting and managing relational databases like MySQL, PostgreSQL, Oracle, and SQL Server.

e) Amazon CloudWatch: It is a monitoring and observability service that provides data and actionable insights for AWS resources and applications. It is used for monitoring performance, setting alarms, collecting and analyzing logs, and gaining visibility into the operational health of the system.

f) Amazon S3 (Simple Storage Service): It is a scalable object storage service used for storing and retrieving data. It is commonly used for hosting static websites, storing backups, sharing files, and serving as a content delivery network (CDN).

- What are the tools used to send logs to the cloud environment? 

There are several tools and services available to send logs to the cloud environment. Here are some commonly used options:

AWS CloudWatch Logs: AWS CloudWatch Logs is a fully managed log management service provided by AWS. It allows you to collect, monitor, and store log data from various sources, including AWS services and your applications. You can send logs directly to CloudWatch Logs using the AWS CLI, SDKs, or the CloudWatch Logs API.

AWS CloudWatch Agent: The CloudWatch Agent is a lightweight software that can be installed on your EC2 instances or on-premises servers. It enables you to collect system-level metrics and logs from your instances and send them to CloudWatch Logs. The agent supports both Windows and Linux environments.

Logstash: Logstash is an open-source data processing pipeline tool that can collect, transform, and send logs to various destinations, including cloud-based services. With Logstash, you can ingest logs from multiple sources, apply filters, and forward them to services like Elasticsearch or Amazon S3.

- What are IAM Roles? How do you create /manage them? 

IAM Roles in AWS are a way to grant permissions to entities such as AWS services, users, or applications to access AWS resources securely. 
Unlike IAM users, roles are not associated with specific individuals but are to access resources.

Creating and managing IAM Roles:

### Creating a Role:

Open the IAM service---->Choose "Roles" and click on "Create role"--->configure the role details, including specifying permissions through policies--->You can either select from the existing policies or create custom policies based on your requirements--->Review and create the role.

### Assigning the Role:

After creating the role, you can assign it to entities that need to assume the role and access AWS resources.

### Managing Role Permissions:

To manage role permissions, you can modify the attached policies or add/remove policies as needed.
You can also change the trusted entities that are allowed to assume the role.
Regularly review and update role permissions to ensure they align with the required access levels and security best practices.

- How to upgrade or downgrade a system with zero downtime? 
- What is infrastructure as code and how do you use it? 
- What is a load balancer? Give scenarios of each kind of balancer based on your experience. 
- What is CloudFormation and why is it used for?
- Difference between AWS CloudFormation and AWS Elastic Beanstalk?
- What are the kinds of security attacks that can occur on the cloud? And how can we minimize them?
- Can we recover the EC2 instance when we have lost the key?
- What is a gateway?
- What is the difference between the Amazon Rds, Dynamodb, and Redshift?
- Do you prefer to host a website on S3? What's the reason if your answer is either yes or no?


Let's share your answer on LinkedIn in best possible way thinking you are in a interview table. 
Happy Learning !! :)
