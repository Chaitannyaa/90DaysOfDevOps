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
  name                     = "web-server"
  image_id                 = "ami-053b0d53c279acc90"
  instance_type            = "t2.micro"
  security_groups          = ["sg-0277e2f4d375c8965"]
  associate_public_ip_address = true
  
  user_data = <<-EOF
              #!/bin/bash

              INSTANCE_ID=$(curl -s http://169.254.169.254/latest/meta-data/instance-id)

              echo '<!DOCTYPE html>
              <html>
              <head>
                <title>Instance ID Retrieval</title>
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
                  <p>Instance ID: '$INSTANCE_ID'</p>
                </div>
              </body>
              </html> > index.html
              sudo python3 -m http.server 80 &
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
  vpc_zone_identifier  = ["subnet-0fb1b21f41c1408e2", "subnet-07d528f8595558d7e"]

  tag {
    key                 = "Name"
    value               = "Web_Servers"
    propagate_at_launch = true
  }
}

resource "aws_alb" "web_server_lb" {
  name            = "web-server-lb"
  internal        = false
  security_groups = ["sg-0277e2f4d375c8965"]
  subnets         = [
    "subnet-0fb1b21f41c1408e2",
    "subnet-07d528f8595558d7e"
  ]
}

resource "aws_lb_listener" "web_server_listener" {
  load_balancer_arn = aws_alb.web_server_lb.arn
  port              = 80
  protocol          = "HTTP"

  default_action {
    type  = "forward"
    target_group_arn = aws_lb_target_group.web_server_tg.arn
  }
}

resource "aws_lb_target_group" "web_server_tg" {
  name        = "web-server-target-group"
  port        = 80
  protocol    = "HTTP"
  target_type = "instance"
  vpc_id      = "vpc-04d61d6f66d196f03"
  health_check {
    path = "/"
  }
}

output "alb_dns_name" {
  value = aws_alb.web_server_lb.dns_name
}
```

- Run terraform apply to create the Auto Scaling Group.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/6b01860b-6ae0-40de-a1aa-8c94475a6ea0)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/4f6081e9-1d65-44f1-8f1c-09cb9a8ca4bf)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/ce9c9ea6-ffe2-4083-967c-30e0ea9a9ddd)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/2a94fb53-99e0-4cf3-a021-f6a937ea3a87)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/e0ead829-0bd6-453e-a1de-6eff42080b0a)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/abd69f5c-1476-4bf8-8797-464910a0c950)

## Task 2: Test up scaling - down scaling

- Edit your main.tf with increased desired capacity to 2 then apply it.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/8ca913ce-aa93-4234-b613-874e13c2a0e4)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/ff65c5c9-bbeb-4a2c-861e-f58e1c753000)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/988a3bf6-1544-49b6-8b11-f866130fb090)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/dd0c15e0-544b-4d35-94e0-b623eda4653c)

- Wait a few minutes for the new instance to be launched.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/05a37f09-fff1-45f2-a1de-f917a0958662)

- Go to the EC2 Instances service and verify that the new instances have been launched.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/5f3167ae-fcae-418f-b3eb-1592a6a557c0)

- Access you load balancer url to check its fuctionality to distribute the traffic across those 2 web servers.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/3ae8128d-6e68-4749-9854-4818c8a7612e)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/2cd4c7a7-0ab6-40e4-af01-ba6a4f623e19)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/c8c5e962-66b7-459f-8af6-c32a03506d9b)

- Decrease the "Desired Capacity" to 1 and wait a few minutes for the extra instances to be terminated.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/6a1236b4-7d4d-4321-890c-0382e56e3e1e)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/22755f91-6ba6-4b2b-89cc-c90a3abe5491)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/21f95e78-0806-4cf4-848b-2b2a18d8c079)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/073736d6-fb37-4d48-96b6-4d13932153bc)

- Go to the EC2 Instances service and verify that the extra instances have been terminated.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/82f3b97f-712c-45d8-85fc-5023937b6f3a)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/a0963e78-3caf-4cce-8890-1b0293ec6d91)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/e269a530-46b2-4949-901f-74b6ddccf30d)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/43906bac-f03d-4856-8e47-ead761370fe7)

Congratulations🎊🎉 You have successfully scaled up and down your infrastructure with Terraform.

**Happy Learning :)**

# Day 68 task is complete!
