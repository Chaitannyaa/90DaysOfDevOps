# Day 68 - Scaling infrastructure with Terraform 🚀

## Understanding Scaling
Scaling is the process of adding or removing resources to match the changing demands of your application. As your application grows, you will need to add more resources to handle the increased load. And as the load decreases, you can remove the extra resources to save costs.

Terraform makes it easy to scale your infrastructure by providing a declarative way to define your resources. You can define the number of resources you need and Terraform apply will create or destroy the resources as per our need.

## Task 1: Create an Auto Scaling Group
Auto Scaling Groups are used to automatically add or remove EC2 instances based on the current demand. Follow these steps to create an 

Auto Scaling Group:

- In your main.tf file, add the following code to create an Auto Scaling Group:

```sh
provider "aws" {
  region = "us-east-1"
}

resource "aws_launch_configuration" "web_server_lc" {
  name_prefix              = "web-server-lc-"
  name                     = "web-server"
  image_id                 = "ami-053b0d53c279acc90"
  instance_type            = "t2.micro"
  security_groups          = ["sg-0277e2f4d375c8965"]
  associate_public_ip_address = true

  user_data = <<-EOF
              #!/bin/bash
              echo '<!DOCTYPE html>
              <html>
              <head>
                <style>
                  body {
                    background-color: #000080;
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
                  <h1>You are doing Great! </h1>
                  <p>Auto scaling using Terraform (HTTP server)</p>
                </div>
              </body>
              </html>' > index.html
              nohup python3 -m http.server 8000 &
              EOF
}

resource "aws_autoscaling_group" "web_server_asg" {
  name                 = "web-server-asg"
  launch_configuration = aws_launch_configuration.web_server_lc.name
  min_size             = 1
  max_size             = 3
  desired_capacity     = 1
  health_check_type    = "EC2"
  target_group_arns    = [aws_lb_target_group.web_server_tg.arn]
  vpc_zone_identifier  = [aws_subnet.public_subnet_1a.id, aws_subnet.public_subnet_1b.id]
}

resource "aws_elb" "web_server_lb" {
  name              = "web-server-lb"
  internal          = false
  security_groups   = ["sg-0277e2f4d375c8965"]
  subnets           = [
    "subnet-0fb1b21f41c1408e2",
    "subnet-07d528f8595558d7e"
  ]
}

resource "aws_lb_target_group" "web_server_tg" {
  name        = "web-server-target-group"
  port        = 8000
  protocol    = "HTTP"
  target_type = "instance"
  vpc_id      = "vpc-04d61d6f66d196f03"
  health_check {
    path = "/"
  }
}
```

- Run terraform apply to create the Auto Scaling Group.


## Task 2: Test up scaling - down scaling

- Edit your main.tf with increased desired capacity to 2 then apply it.

- Wait a few minutes for the new instance to be launched.

- Go to the EC2 Instances service and verify that the new instances have been launched.

- Decrease the "Desired Capacity" to 1 and wait a few minutes for the extra instances to be terminated.

- Go to the EC2 Instances service and verify that the extra instances have been terminated.

Congratulations🎊🎉 You have successfully scaled your infrastructure with Terraform.

Happy Learning :)
