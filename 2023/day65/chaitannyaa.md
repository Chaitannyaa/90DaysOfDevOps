# Day 65 - Working with Terraform Resources 🚀

## Understanding Terraform Resources

A resource in Terraform represents a component of your infrastructure, such as a physical server, a virtual machine, a DNS record, or an S3 bucket. Resources have attributes that define their properties and behaviors, such as the size and location of a virtual machine or the domain name of a DNS record.

When you define a resource in Terraform, you specify the type of resource, a unique name for the resource, and the attributes that define the resource. Terraform uses the resource block to define resources in your Terraform configuration.

## Task 1: Create a security group

To allow traffic to the EC2 instance, you need to create a security group. Follow these steps:

In your main.tf file, add the following code to create a security group:

```sh
resource "aws_security_group" "web_server" {
  name_prefix = "web-server-sg"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```
![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/6a178ad9-76bd-4d1d-86af-53bad72ae253)

- Run terraform init to initialize the Terraform project.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/174f675a-39ff-497e-aaf6-06b6a3442caa)

- Run terraform apply to create the security group.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/9a46d1ef-6a78-4fca-accd-8acbad6cb01f)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/5bdfe196-41fa-44da-bb96-9941da58f18f)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/f30d6ce8-4f92-4681-bb9c-13d471c5b223)

## Task 2: Create an EC2 instance

- In your main.tf file, add the following code to create an EC2 instance:

```sh
resource "aws_instance" "web_server" {
  ami           = "ami-0557a15b87f6559cf"
  instance_type = "t2.micro"
  key_name      = "my-key-pair"
  security_groups = [
    aws_security_group.web_server.name
  ]

  user_data = <<-EOF
              #!/bin/bash
              echo "<html><body><h1>Welcome to my website!</h1></body></html>" > index.html
              nohup python -m SimpleHTTPServer 80 &
              EOF
}
```
Note: Replace the ami and key_name values with your own. You can find a list of available AMIs in the AWS documentation.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/e3041c05-3888-42f3-9509-f3a184544451)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/a558a4e3-cbb8-4418-9ec2-ed729112df60)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/9029f356-4493-4e6c-a685-89cd7325a7e7)

```sh
terraform {
  required_providers {
    aws = { source  = "hashicorp/aws"}
  }
}
provider "aws" {
  region = "us-east-1"
}

resource "aws_security_group" "web_server" {
  name_prefix = "web-server-sg"
  tags = { Name = "SG_Web_server" }
  ingress {
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "web_server" {
  ami                    = "ami-0557a15b87f6559cf"
  instance_type          = "t2.micro"
  key_name               = "ssh"
  vpc_security_group_ids = [aws_security_group.web_server.id]
  tags                   = { Name = "Python_Web_server" }

  user_data = <<-EOF
    #!/bin/bash
    echo '<!DOCTYPE html>
    <html>
    <head>
      <style>
        body {
          background-color: #87CEEB;
          color: white;
          display: flex;
          justify-content: center;
          align-items: center;
          height: 100vh;
          margin: 0;
          padding: 0;
        }

        h1, p {
          font-size: 24px;
        }
      </style>
    </head>
    <body>
      <div>
        <h1>Welcome to my website!</h1>
        <p>Hosted using Python HTTP server</p>
      </div>
    </body>
    </html>' > index.html
    nohup python -m http.server 8000 &
    EOF
}
```
![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/5f819ca3-e2a6-4bd2-b65c-7d43ddad7be2)

- Run terraform apply to create the EC2 instance.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/74b5479c-336e-4e30-a17b-1232f57126ae)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/79c89a2c-f7f6-461d-a984-1f1bcb80965b)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/5e47992a-641a-47cb-b84d-8c7aa734befb)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/fa983ffc-d155-43f7-a6a8-76a7559cf506)


## Task 3: Access your website

- Your EC2 instance is up and running, you can access the website you just hosted on it.

![246646185-62a16c48-edd7-4efc-9d61-158bd15c6386](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/19edcdbb-1acb-4aba-a8bc-9c25b5485090)

Happy Terraforming!

# Day 65 task is complete!
