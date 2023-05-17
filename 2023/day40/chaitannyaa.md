
# Day 40 AWS EC2 templates☁

![AWS](https://www.eginnovations.com/blog/wp-content/uploads/2021/09/Amazon-AWS-Cloud-Topimage-1.jpg)

## Automation in EC2:

Amazon Elastic Compute Cloud can give you secure, reliable, high-performance, and cost-effective computing infrastructure to meet demanding business needs.

### Automation in Amazon EC2 (Elastic Compute Cloud) involves using various tools and services to streamline and simplify the management and deployment of EC2 instances. Here are some key aspects of automation in EC2:

- Launch Templates: Launch templates allow you to create reusable configurations for EC2 instances, including instance type, storage, security groups, and more. They streamline the process of launching multiple instances with consistent settings.

- Amazon Machine Images (AMIs): AMIs provide a template for launching EC2 instances. You can create custom AMIs with pre-installed software, configurations, and data, allowing for faster and repeatable instance launches.

- Auto Scaling: Amazon EC2 Auto Scaling enables you to automatically adjust the number of EC2 instances in a fleet based on demand. It helps maintain application availability, optimize costs, and ensure efficient resource utilization.

## Launch an AWS EC2 using a template:

- You can make a launch template with the configuration information you need to start an instance. You can save launch parameters in launch templates so you don't have to type them in every time you start a new instance.
- For example, a launch template can have the AMI ID, instance type, and network settings that you usually use to launch instances. 
- You can tell the Amazon EC2 console to use a certain launch template when you start an instance.

Read more from [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html)

### Instance Types:

Amazon EC2 has a large number of instance types that are optimised for different uses. The different combinations of CPU, memory, storage and networking capacity in instance types give you the freedom to choose the right mix of resources for your apps. Each instance type comes with one or more instance sizes, so you can adjust your resources to meet the needs of the workload you want to run.

Read from [here](https://aws.amazon.com/ec2/instance-types/?trk=32f4fbd0-ffda-4695-a60c-8857fab7d0dd&sc_channel=ps&s_kwcid=AL!4422!3!536392685920!e!!g!!ec2%20instance%20types&ef_id=CjwKCAiA0JKfBhBIEiwAPhZXD_O1-3qZkRa-KScynbwjvHd3l4UHSTfKuigd5ZPukXoDXu-v3MtC7hoCafEQAvD_BwE:G:s&s_kwcid=AL!4422!3!536392685920!e!!g!!ec2%20instance%20types)

### AMI:

An Amazon Machine Image (AMI) is an image that AWS supports and keeps up to date. It contains the information needed to start an instance. When you launch an instance, you must choose an AMI. When you need multiple instances with the same configuration, you can launch them from a single AMI.
  

# Task1:

- Create a launch template with Amazon Linux 2 AMI and t2.micro instance type with Jenkins and Docker setup (You can use the Day 39 User data script for installing the required tools.

- Create 3 Instances using Launch Template, there must be an option that shows number of instances to be launched ,can you find it? :)

- You can go one step ahead and create an auto-scaling group, sounds tough? 

Check out [this](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html#create-launch-template-for-auto-scaling)!
    
Post your progress on Linkedin. 

Happy Learning :)
# Day40 task is complete! 
