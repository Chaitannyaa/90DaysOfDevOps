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
  vpc_id     = aws_vpc.my_vpc.id
  cidr_block = "10.0.1.0/24"
}

resource "aws_subnet" "private_subnet" {
  vpc_id     = aws_vpc.my_vpc.id
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
  subnet_id      = aws_subnet.public_subnet.id
  route_table_id = aws_route_table.public_route_table.id
}

resource "aws_security_group" "ec2_security_group" {
  name        = "AllowSSH"
  description = "Allow SSH access from anywhere"
  vpc_id      = aws_vpc.my_vpc.id
  
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "web_server" {
  ami                    = "ami-0557a15b87f6559cf"
  instance_type          = "t2.micro"
  subnet_id              = aws_subnet.public_subnet.id
  vpc_security_group_ids = [aws_security_group.ec2_security_group.id]
  tags = { Name = "Apache2 Web-server" }
  user_data              = <<-EOF
    #!/bin/bash
    sudo apt-get update
    sudo apt-get install -y apache2
    echo '<!DOCTYPE html>
    <html>
    <head>
      <style>
        body {
          background-color: #FFA500;
          color: white;
          display: flex;
          justify-content: center;
          align-items: center;
          height: 100vh;
          margin: 0;
          padding: 0;
        }
        h1 {
          font-size: 48px;
        }
        p {
          font-size: 24px;
        }
      </style>
    </head>
    <body>
      <div>
        <h1>Welcome to my website!</h1>
        <p>Hosted using Apache2 Web Server</p>
      </div>
    </body>
    </html>' | sudo tee /var/www/html/index.html
    sudo systemctl enable apache2
    sudo systemctl start apache2
  EOF
}

resource "aws_eip" "my_eip" {
  instance = aws_instance.web_server.id
}

resource "aws_eip_association" "eip_association" {
  instance_id   = aws_instance.web_server.id
  allocation_id = aws_eip.my_eip.id
}
```

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/81f667ac-8fea-4909-b6c0-8c1b13ab4f29)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/e35b116e-9bf5-45fc-9ad1-c1595e495ea7)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/9d2a0092-f4c2-426e-a374-e7acb7046a3f)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/e4debcce-ac87-4e1e-ace2-ea5138b5270e)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/371f569a-8a35-4acc-8c2c-f42e1d734acc)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/7ec6d12d-55df-4183-914a-8d579a95430a)

![csadca](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/d5e80e00-dc49-496d-af41-11a8bbfa1416)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/4adb0672-65e6-4a9d-a225-f8f4ca36638e)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/b2bc7305-4c96-488a-b7f7-f3259a85d264)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/63628f83-7076-40fe-b559-891088898275)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/debaaa77-2497-4c0e-92e9-0e2b282dbfcf)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/d009bbba-b3a9-43c9-a407-cc97c49b5a2b)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/d6c45840-dd17-4cc7-8b20-a32722c2da1f)


- Open the website URL in a browser to verify that the website is hosted successfully.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/930a580b-080a-4862-8e47-bc04cc36c8b3)


**Happy Terraforming:)**

# Day 66 task is complete!
