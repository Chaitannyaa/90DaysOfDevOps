
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

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/df42b4b3-cd72-4cb9-9342-42c265baeda1)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/286062ef-11d6-4a3a-ab4e-79ad61180be6)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/91d7bd33-f5b0-4a16-9738-4ccf370fe600)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/48dee429-bf67-47c2-89c1-ef5957686346)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/25f1c14f-fc53-4387-8585-cbbb65b5082f)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/be607b87-b785-4b57-8849-cfcd2a55de4b)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/fcb4c056-50db-4c69-8de8-7619af514c21)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/c89427fd-e9d7-4f33-8ca1-698e23b6c53f)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/467ae9c8-6b76-4f13-95b9-13a7e294eb94)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/d2f025c1-d11e-4589-8a2f-b4fd96d4d8f7)

- Create 3 Instances using Launch Template, there must be an option that shows number of instances to be launched ,can you find it? :)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/74ead58c-48ee-494a-8923-9144f7d10207)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/4aea109f-57a3-4e77-919f-5d80014e05f4)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/21986681-1918-438c-a79d-dbeb2ef2d5a7)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/3a491eec-1ed4-4418-9667-0ee7a5c725a6)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/0a5af8dd-7712-40ea-9c86-cee589ef0306)

- You can go one step ahead and create an auto-scaling group, sounds tough? 

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/fc28cff5-3c02-41be-ab76-85a431ea91f2)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/de57e3a7-80ad-4820-9ca5-78ec065d6192)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/50468a1b-e3f8-4871-8c47-02b434008877)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/8bed3645-1162-4895-b00e-e32b868a4e64)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/7b05a3fb-59d7-4456-b392-4f193af5aa1d)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/fb9b7be7-8707-4710-8cf9-643aaf6349da)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/364bcad0-4ed2-44a0-834e-f8dd6f0a681a)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/84bf845e-638e-495c-98b5-52b4492862b5)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/87923d0f-fb39-4b3f-9821-4ac10921985d)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/cc84b41f-f79a-4ef0-8c8e-838c6f03385e)

## Now increase the CPU utilization of current running instance to verify ASG works fine and scale-out works

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/475217ab-9fc3-4546-ac91-105be0289e19)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/dce521d2-9825-4d25-a995-7e1726dec28c)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/ab9d4c19-756b-4b96-bbcf-b583e0415530)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/0dd85ee0-14ad-4be5-b72f-10df0903f622)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/7e35a970-7eb0-4c00-8a27-39216f3e5d73)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/e4473de2-7fd4-4687-bf61-76fcdcd02542)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/975aba8f-0218-4c56-82b6-b329ea4c5a17)

## Lets reduce CPU load and verify scale-in works

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/94b9671e-8dd6-4bf7-b9ab-d90b05a70911)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/742abba8-c99f-49b8-9c1f-daf62ca50409)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/b3a76a18-511f-412b-a714-f7b57df64c5f)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/13313ede-6064-4c63-9ff0-fabc33037f18)

## if you delete ASG then all the instances will be wiped-out

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/d40b087d-47a4-49ab-9b19-56481f7c90df)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/0b1d79fb-f02d-42c5-acf1-12756886e947)

Check out [this](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html#create-launch-template-for-auto-scaling)!

Happy Learning :)
# Day40 task is complete! 
