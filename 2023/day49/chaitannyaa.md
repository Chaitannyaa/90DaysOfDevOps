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

To upgrade or downgrade a system with zero downtime, you can use strategies such as rolling deployments, blue-green deployments, or canary deployments. These approaches involve gradually shifting traffic or deploying updates in a controlled manner to minimize or eliminate downtime.

- What is infrastructure as code and how do you use it? 

Infrastructure as Code (IaC) is the practice of defining and managing infrastructure resources using code. Tools like AWS CloudFormation, Terraform, and AWS CDK enable you to write infrastructure as code to provision and manage AWS resources programmatically, enabling consistent, repeatable, and version-controlled infrastructure deployments.

- What is a load balancer? Give scenarios of each kind of balancer based on your experience. 

A load balancer distributes incoming traffic across multiple targets, such as EC2 instances, to improve application availability and scalability. In AWS, there are three types of load balancers:

Classic Load Balancer (CLB): Used for applications that require TCP/SSL balancing.

Application Load Balancer (ALB): Ideal for HTTP/HTTPS traffic and provides advanced routing capabilities.

Network Load Balancer (NLB): Suited for handling TCP/UDP traffic at ultra-high levels.

Gateway Load Balancer (GLB): It gives you one gateway for distributing traffic across multiple virtual appliances while scaling them up or down, based on demand. 

- What is CloudFormation and why is it used for?

AWS CloudFormation is a service that allows you to model and provision AWS resources using templates. It enables you to automate the creation and management of your infrastructure, making it easier to deploy and update resources in a consistent and repeatable manner.

- Difference between AWS CloudFormation and AWS Elastic Beanstalk?

AWS CloudFormation is a service for infrastructure as code, allowing you to create and manage AWS resources programmatically. It provides a way to define the entire infrastructure stack using a template. 

In contrast, AWS Elastic Beanstalk is a platform as a service (PaaS) offering that abstracts away the infrastructure details and simplifies the deployment and management of applications.

- What are the kinds of security attacks that can occur on the cloud? And how can we minimize them?

Some types of security attacks on the cloud include DDoS attacks, data breaches, and unauthorized access. 

To minimize these attacks, you can implement measures such as using strong access controls and permissions, encrypting sensitive data, implementing network security measures like firewalls, and regularly monitoring and auditing your cloud environment.

- Can we recover the EC2 instance when we have lost the key?

Yes, 
1. Replace the Key Pair:
If you have lost the key pair but still have administrative access to the AWS account, you can create a new key pair and associate it with the EC2 instance. This method involves stopping the instance, detaching the root volume, attaching it to a different running instance, modifying the authorized_keys file on the root volume, and then reattaching the volume back to the original instance. This process allows you to add a new public key to the authorized_keys file, which grants you access to the instance with the new key pair.

2. Use a Custom AMI or Snapshot:
If you have created a custom Amazon Machine Image (AMI) or have a snapshot of the instance's root volume, you can launch a new instance from that AMI or snapshot. During the launch process, you can specify a new key pair. This effectively creates a new instance with the desired key pair, allowing you to access the new instance without relying on the lost key pair.

3. Contact AWS Support:
If you have exhausted all other options and cannot regain access to the instance, you can contact AWS Support for assistance. 

- What is a gateway?

A gateway is a device or software component that serves as an entry or exit point between two networks or different systems. It facilitates the flow of data packets between networks, allowing them to communicate with each other.

Here are two common types of gateways:

Network Gateway: A network gateway, often referred to as a router or default gateway, is a device that connects two or more networks with different network protocols. It acts as an intermediary between these networks, forwarding data packets between them based on their destination IP addresses. Network gateways enable communication between devices on different subnets or networks, enabling data transmission and routing decisions.

Application Gateway: An application gateway, also known as an application-level gateway or proxy, operates at the application layer of the network stack. It acts as an intermediary for specific application protocols, such as HTTP, HTTPS, FTP, or SMTP. Application gateways often provide additional features like load balancing, SSL/TLS termination, caching, firewalling, and content filtering, enhancing security and performance for the applications they proxy.

Gateways are essential components for network connectivity and communication. They can be physical devices like routers or software-based solutions running on servers.

- What is the difference between the Amazon Rds, Dynamodb, and Redshift?

Amazon RDS (Relational Database Service):
Amazon RDS is a managed database service that simplifies the deployment, management, and scaling of relational databases. It supports popular database engines such as MySQL, PostgreSQL, Oracle, SQL Server, and Amazon Aurora.

DynamoDB:
DynamoDB is a fully managed NoSQL database service provided by AWS. It offers seamless scalability, high performance, and automatic replication across multiple regions.

Amazon Redshift:
Amazon Redshift is a fully managed data warehousing service designed for large-scale analytics and reporting. It is optimized for handling massive volumes of structured data and performing complex queries.

- Do you prefer to host a website on S3? What's the reason if your answer is either yes or no?

Yes, hosting a website on S3 is often preferred due to its simplicity, scalability, and cost-effectiveness. S3 provides a highly available and durable storage solution for static website files, and it can be easily configured with AWS CloudFront to improve performance through caching and content delivery network (CDN) capabilities. Additionally, S3's pay-as-you-go pricing model can be more cost-effective compared to traditional web hosting options.

Let's share your answer on LinkedIn in best possible way thinking you are in a interview table.

Happy Learning !! :)

# Day 49 task is complete!
