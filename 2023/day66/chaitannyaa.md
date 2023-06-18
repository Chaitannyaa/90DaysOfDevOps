# Day 66 - Terraform Hands-on Project 

## Build Your Own AWS Infrastructure with Ease using Infrastructure as Code (IaC) Techniques(Interview Questions) ☁️

Today, we will explore to create multiple resources using Terraform.

## Let's get started--->

- Create a VPC (Virtual Private Cloud) with CIDR block 10.0.0.0/16

```sh
resource "aws_vpc" "my_vpc" {
  cidr_block = "10.0.0.0/16"
}
```
- Create a public subnet with CIDR block 10.0.1.0/24 in the above VPC.

```sh
resource "aws_subnet" "public_subnet" {
  vpc_id     = aws_vpc.my_vpc.id
  cidr_block = "10.0.1.0/24"
}
```
- Create a private subnet with CIDR block 10.0.2.0/24 in the above VPC.

```sh
resource "aws_subnet" "private_subnet" {
  vpc_id = aws_vpc.my_vpc.id
  cidr_block = "10.0.2.0/24"
}
```
- Create an Internet Gateway (IGW) and attach it to the VPC.

```sh
resource "aws_internet_gateway" "my_igw" {
  vpc_id = aws_vpc.my_vpc.id
}
```
- Create a route table for the public subnet and associate it with the public subnet. This route table should have a route to the Internet Gateway.

```sh
# Create Route Table for public subnet
resource "aws_route_table" "public_route_table" {
  vpc_id = aws_vpc.my_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.my_igw.id
  }
}

# Associate public subnet with public route table
resource "aws_route_table_association" "public_subnet_association" {
  subnet_id = aws_subnet.public_subnet.id
  route_table_id = aws_route_table.public_route_table.id
}
```
- Launch an EC2 instance in the public subnet with the following details:

```sh
AMI: ami-0557a15b87f6559cf
Instance type: t2.micro
Security group: Allow SSH access from anywhere
User data: Use a shell script to install Apache and host a simple website
```

```sh
# Create Security Group for EC2 instance
resource "aws_security_group" "ec2_security_group" {
  name = "AllowSSH"
  description = "Allow SSH access from anywhere"

  ingress {
    from_port = 22
    to_port = 22
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Create EC2 instance in public subnet
resource "aws_instance" "web_server" {
  ami = "ami-0557a15b87f6559cf"
  instance_type = "t2.micro"
  subnet_id = aws_subnet.public_subnet.id
  vpc_security_group_ids = [aws_security_group.ec2_security_group.id]
  user_data = <<-EOF
    #!/bin/bash
    sudo apt-get update
    sudo apt-get install -y apache2
    echo "<html><body><h1>Welcome to my website hosted on EC2 instance!</h1></body></html>" | sudo tee /var/www/html/index.html
    sudo systemctl enable apache2
    sudo systemctl start apache2
  EOF
}
```

- Create an Elastic IP and associate it with the EC2 instance.

```sh
# Create Elastic IP
resource "aws_eip" "my_eip" {
  instance = aws_instance.web_server.id
}

# Associate Elastic IP with EC2 instance
resource "aws_eip_association" "eip_association" {
  instance_id = aws_instance.web_server.id
  allocation_id = aws_eip.my_eip.id
}
```

##  This is how my configuration file [main.tf] looks like--->

```sh
provider "aws" {
  region = "us-east-1"
}

resource "aws_vpc" "my_vpc" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "public_subnet" {
  vpc_id = aws_vpc.my_vpc.id
  cidr_block = "10.0.1.0/24"
}

resource "aws_subnet" "private_subnet" {
  vpc_id = aws_vpc.my_vpc.id
  cidr_block = "10.0.2.0/24"
}

resource "aws_internet_gateway" "my_igw" {
  vpc_id = aws_vpc.my_vpc.id
}

resource "aws_route_table" "public_route_table" {
  vpc_id = aws_vpc.my_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.my_igw.id
  }
}

resource "aws_route_table_association" "public_subnet_association" {
  subnet_id = aws_subnet.public_subnet.id
  route_table_id = aws_route_table.public_route_table.id
}

resource "aws_security_group" "ec2_security_group" {
  name = "AllowSSH"
  description = "Allow SSH access from anywhere"

  ingress {
    from_port = 22
    to_port = 22
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "web_server" {
  ami = "ami-0557a15b87f6559cf"
  instance_type = "t2.micro"
  subnet_id = aws_subnet.public_subnet.id
  vpc_security_group_ids = [aws_security_group.ec2_security_group.id]
  user_data = <<-EOF
    #!/bin/bash
    sudo apt-get update
    sudo apt-get install -y apache2
    echo "<html><body><h1>Welcome to my website hosted on EC2 instance!</h1></body></html>" | sudo tee /var/www/html/index.html
    sudo systemctl enable apache2
    sudo systemctl start apache2
  EOF
}


resource "aws_eip" "my_eip" {
  instance = aws_instance.web_server.id
}

resource "aws_eip_association" "eip_association" {
  instance_id = aws_instance.web_server.id
  allocation_id = aws_eip.my_eip.id
}
```

- Open the website URL in a browser to verify that the website is hosted successfully.



Happy Terraforming:)
