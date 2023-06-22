# Day 70 - Terraform Modules

- Modules are containers for multiple resources that are used together. A module consists of a collection of .tf and/or .tf.json files kept together in a directory
- A module can call other modules, which lets you include the child module's resources into the configuration in a concise way. 
- Modules can also be called multiple times, either within the same configuration or in separate configurations, allowing resource configurations to be packaged and re-used.

## Task-01

- Write about different modules Terraform.

- Difference between Root Module and Child Module.

- Is modules and Namespaces are same? Justify your answer for both Yes/No

### Let's use modules to create resources on AWS environment and Docker--->

```sh
# Creating a AWS EC2 Instance
resource "aws_instance" "server-instance" {
  # Define number of instance
  instance_count = var.number_of_instances
 
  # Instance Configuration
  ami                    = var.ami
  instance_type          = var.instance_type
  subnet_id              = var.subnet_id
  vpc_security_group_ids = var.security_group
 
  # Instance Tagsid
  tags = {
    Name = "${var.instance_name}"
  }
}
```

```sh
# Server Module Variables
variable "number_of_instances" {
  description = "Number of Instances to Create"
  type        = number
  default     = 1
}
 
variable "instance_name" {
  description = "Instance Name"
}
 
variable "ami" {
  description = "AMI ID"
  default     = "ami-xxxx"
}
 
variable "instance_type" {
  description = "Instance Type"
}
 
variable "subnet_id" {
  description = "Subnet ID"
}
 
variable "security_group" {
  description = "Security Group"
  type        = list(any)
}
```

```sh
# Server Module Output
output "server_id" {
  description = "Server ID"
  value       = aws_instance.server-instance.id
}
```


**Happy learning :)**
