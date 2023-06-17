# Day 64 - Terraform with AWS

Provisioning on AWS is quite easy and straightforward with Terraform.

## Prerequisites

### AWS CLI installed 

The AWS Command Line Interface (AWS CLI) is a unified tool to manage your AWS services. With just one tool to download and configure, you can control multiple AWS services from the command line and automate them through scripts.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/4b50fee6-7d99-4210-98e7-2fc625c41e58)

### AWS IAM user 

IAM (Identity Access Management) AWS Identity and Access Management (IAM) is a web service that helps you securely control access to AWS resources. You use IAM to control who is authenticated (signed in) and authorized (has permissions) to use resources.

*In order to connect your AWS account and Terraform, you need the access keys and secret access keys exported to your machine.*

```sh
export AWS_ACCESS_KEY_ID=AKIA27CR22N3AKKD7QNS
export AWS_SECRET_ACCESS_KEY=Fgd76OEjTn12I40LIKWDjMVdyJuBMzEeeJ2TwLJp
```

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/337620d2-48ae-4781-9abc-352d07e5c8a9)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/c850de29-f68c-47c7-b0be-37390dac5cac)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/c76a1d8e-d0ec-47f7-a37d-633a956c3cb2)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/f7deef9c-c6a1-40d3-8aa2-7090d2b2b204)

### Install required providers

```sh
terraform {
 required_providers {
        aws = {
        source  = "hashicorp/aws"
        version = "~> 4.16"
}
}
        required_version = ">= 1.2.0"
}
```
Add the region where you want your instances to be

```sh
provider "aws" {
region = "us-east-1"
}
```

## Task: Provision an AWS EC2 instance using Terraform

Hint: 

```sh
resource "aws_instance" "aws_ec2_test" {
    count = 2
    ami = "ami-08c40ec9ead489470"
    instance_type = "t2.micro"
    tags = {
        Name = "TerraformTestServerInstance"
    }
}
```
![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/8dfae95f-42e7-4f7b-b713-a5f5da59f973)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/f8e3b27f-d067-4df4-b72f-003c4047003b)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/2a5bcbc7-8d20-4401-9648-3d3758fabdfe)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/2d6aea00-394c-4173-9981-ccb0fa507c8d)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/303d55dc-eef4-422b-8c9f-97676ff45df3)


**Happy Learning :)**

# Day 64 task is complete!

