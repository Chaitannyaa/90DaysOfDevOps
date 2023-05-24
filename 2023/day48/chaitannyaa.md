# Day-48 - ECS

Today will be a great learning for sure. I know many of you may not know about the term "ECS". As you know, 90 Days Of DevOps Challange is mostly about 'learning new' , let's learn then ;)

## What is ECS ? 
- ECS (Elastic Container Service) is a fully-managed container orchestration service provided by Amazon Web Services (AWS). It allows you to run and manage Docker containers on a cluster of virtual machines (EC2 instances) without having to manage the underlying infrastructure.

With ECS, you can easily deploy, manage, and scale your containerized applications using the AWS Management Console, the AWS CLI, or the API. ECS supports both "Fargate" and "EC2 launch types", which means you can run your containers on AWS-managed infrastructure or your own EC2 instances.

ECS also integrates with other AWS services, such as Elastic Load Balancing, Auto Scaling, and Amazon VPC, allowing you to build scalable and highly available applications. Additionally, ECS has support for Docker Compose and Kubernetes, making it easy to adopt existing container workflows.

Overall, ECS is a powerful and flexible container orchestration service that can help simplify the deployment and management of containerized applications in AWS.

## What is EKS ? 
- EKS stands for Amazon Elastic Kubernetes Service. It is a managed service provided by Amazon Web Services (AWS) for running and managing Kubernetes clusters.

EKS simplifies the process of setting up, operating, and scaling Kubernetes clusters on AWS infrastructure. It takes care of the underlying hardware and software required to run Kubernetes, allowing developers and DevOps teams to focus on deploying and managing their applications.

## Difference between EKS and ECS ?
- EKS (Elastic Kubernetes Service) and ECS (Elastic Container Service) are both container orchestration platforms provided by Amazon Web Services (AWS). While both platforms allow you to run containerized applications in the AWS cloud, there are some differences between the two.

**Architecture**:
ECS is based on a centralized architecture, where there is a control plane that manages the scheduling of containers on EC2 instances. On the other hand, EKS is based on a distributed architecture, where the Kubernetes control plane is distributed across multiple EC2 instances.

**Kubernetes Support**:
EKS is a fully managed Kubernetes service, meaning that it supports Kubernetes natively and allows you to run your Kubernetes workloads on AWS without having to manage the Kubernetes control plane. ECS, on the other hand, has its own orchestration engine and does not support Kubernetes natively.

**Scaling**:
EKS is designed to automatically scale your Kubernetes cluster based on demand, whereas ECS requires you to configure scaling policies for your tasks and services.

**Flexibility**:
EKS provides more flexibility than ECS in terms of container orchestration, as it allows you to customize and configure Kubernetes to meet your specific requirements. ECS is more restrictive in terms of the options available for container orchestration.

**Community**:
Kubernetes has a large and active open-source community, which means that EKS benefits from a wide range of community-driven development and support. ECS, on the other hand, has a smaller community and is largely driven by AWS itself.

In summary, EKS is a good choice if you want to use Kubernetes to manage your containerized workloads on AWS, while ECS is a good choice if you want a simpler, more managed platform for running your containerized applications.

# Task :
Set up ECS (Elastic Container Service) by setting up Nginx on ECS.

## step 1: Create a cluster for our deployments

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/21a6a90a-15db-4a31-a872-efd5920af0b5)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/7a55f4ac-aeae-4f32-ad78-f3b3f10e2d97)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/56913474-b5ed-43d1-b140-f1571171a7cb)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/3783dc81-17c1-424f-838e-98f9b0b479ef)

## step 2: Create an ECS Task Definition

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/4faa4191-58a4-4d80-b86d-6688a042c653)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/b98b7527-1968-4f52-9ae6-2aa39cee4451)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/7112f111-56b0-4eb2-86a4-9ecdf8b8ba5e)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/059c37b4-91be-424b-8ba0-d88f8c22e123)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/05b997ad-fc1f-4013-9d4c-2564c124ad37)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/ab446ab9-58c5-49ad-9ed5-d571c8b008ff)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/36a0426a-20c0-4020-b009-cc4a72e31502)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/c2dedcc7-674c-46e4-b2bd-2d62ebcf5eae)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/58a679c7-7172-4a0d-b215-4b23e86ab342)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/c0365c69-f682-4baa-a0ef-29b257ff315e)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/3b8cc8b5-510f-4fbf-ab9e-e80029c1a137)

## Step 3: Create an ECS Service

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/64ebf57d-55a4-4f1f-b11d-d9257321e1f0)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/3b9f009e-24df-4827-aa3f-bbf63b44389c)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/141dd60c-0f3b-4c40-a574-e68ae234b0cb)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/6e8ed63e-c731-4837-92cd-26b046353295)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/8c1edaaa-4acf-475e-923c-3ed9bb6df60b)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/49fefe07-7796-4ee6-b5f2-5c36940b930c)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/4739f71c-96de-4fa9-a9c3-3264b8f89704)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/2eaecac4-6f6a-4523-917c-81ea3a5b5829)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/7ffe7972-6f43-4e2a-9fa0-a6dd3b987d14)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/1b914a16-ac6b-4927-af5f-43c17d705b7b)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/55cafcaf-298f-4c7d-93c8-34fd26ff45a9)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/6f9aad2c-e3e6-4f86-85e1-c0eb8c85f05d)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/1e9a379a-f9d7-4732-8fd1-b17aeabc2268)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/66c06584-131f-49c3-96f0-b5b45188a53b)

That's all, we have deployed our application using ECS.

Happy Learning!

# Day 48 task is completed!


