# Day 41: Setting up an Application Load Balancer with AWS EC2 🚀 ☁

![LB2](https://user-images.githubusercontent.com/115981550/218145297-d55fe812-32b7-4242-a4f8-eb66312caa2c.png)

## What is Load Balancing?
Load balancing is the distribution of workloads across multiple servers to ensure consistent and optimal resource utilization. It is an essential aspect of any large-scale and scalable computing system, as it helps you to improve the reliability and performance of your applications.

## Elastic Load Balancing:
**Elastic Load Balancing (ELB)** is a service provided by Amazon Web Services (AWS) that automatically distributes incoming traffic across multiple EC2 instances. ELB provides three types of load balancers:

Read more from [here](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)

1) **Application Load Balancer (ALB)** - _operates at layer 7 of the OSI model and is ideal for applications that require advanced routing and microservices._

- Read more from [here](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)


2) **Network Load Balancer (NLB)** - _operates at layer 4 of the OSI model and is ideal for applications that require high throughput and low latency._

- Read more from [here](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html)


3) **Classic Load Balancer (CLB)** - _operates at layer 4 of the OSI model and is ideal for applications that require basic load balancing features._
- Read more [here](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/introduction.html)

## 🎯 Today's Tasks:

### Task 1:
- launch 2 EC2 instances with an Ubuntu AMI and use User Data to install the Apache Web Server.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/4ded3676-8090-4767-97cd-5e93a0e0b223)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/c82d5b5c-b349-4580-9616-4a1f5aeb883a)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/071f3899-169a-4654-98fc-06497553c107)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/d9f4882e-1895-46a4-a7ff-0631b4de55bd)

- Modify the index.html file to include your name so that when your Apache server is hosted, it will display your name also do it for 2nd instance which include " TrainWithShubham Community is Super Aweasome :) ".

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/91335e9d-58db-49e8-9487-40d74c526d5e)

- Open your web browser and access HostIP:80 for both ec2 instances

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/5de81016-9a1d-4e65-80db-082b6f0972b9)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/ab486585-fa8a-4ed9-a409-318209566e25)

### Task 2:
- Create an Application Load Balancer (ALB) in EC2 using the AWS Management Console.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/99dfbafa-f3a3-4841-8bd0-cb1ebb32dcdc)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/66e53b7d-0c18-41c9-8ad0-681d6a7ffbc9)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/8eb8e3d0-6af8-4f97-ad45-0690d05f65ca)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/10dba111-dce3-4152-8ef5-844001ed5c12)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/3e64df43-c1a8-4fe7-9352-fe05cbd9a835)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/921c7ad9-de6a-42fb-9c78-fafe7006d02b)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/53095d47-823e-4785-ba80-be6fb7a373ad)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/5568c331-c749-4cbd-9e00-cd00334889c4)

- Add EC2 instances which you launch in task-1 to the ALB as target groups.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/921c7ad9-de6a-42fb-9c78-fafe7006d02b)

- Verify that the ALB is working properly by checking the health status of the target instances and testing the load balancing capabilities.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/310be106-7c8a-46a9-a0e6-65b27e648eb1)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/704d0f06-6fd7-441e-a762-49bb70adad30)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/26ceea51-c1ff-48f1-918f-d38f899c32e3)

![LoadBalancer](https://user-images.githubusercontent.com/115981550/218143557-26ec33ce-99a7-4db6-a46f-1cf48ed77ae0.png)

Happy Learning! 😃

# Day41 task is complete!
