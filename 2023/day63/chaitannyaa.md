# Day 63 - Terraform Variables

Variables in Terraform are quite important, as you need to hold values of names of instance, configs, etc.

We can create a `variables.tf` file which will hold all the variables.

```sh
variable "filename" {
default = "path/to/file/demo-var.txt"
}
```

```sh
variable "content" {
default = "This is coming from a variable which was updated"
}
```

These variables can be accessed by var object in `main.tf`

## Task-01: Create a local file using Terraform

Hint:

```sh
resource "local_file" "devops" {
filename = var.filename
content = var.content
}
```

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/3e707ff9-9e16-4849-bd7b-fb1140415133)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/d42be9d6-bf58-40e9-8d3e-101e81001848)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/45c7afe6-beda-4db0-84aa-a896b580974c)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/1f2d2707-b77c-4ef9-8fcd-fb48e1feab83)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/ced41db9-1cef-4b85-91bf-7daeb7407b8b)

![cghvjh](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/2e9df2a7-def2-4d9f-84b0-ae849a2a1635)

## Data Types in Terraform

## Map

In Terraform, the map type is used to represent a collection of key-value pairs. It allows you to store and manipulate data in a structured way. A map is similar to a dictionary or hash table in other programming languages.

Here's an example of defining a map variable in Terraform:

```sh
variable "file_contents" {
type = map
default = {
"statement1" = "this is cool"
"statement2" = "this is cooler"
}
}
```
**Let's use `map type` to create files--->**

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/66412356-8110-4707-a5d4-456a8ac43771)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/69616dcf-7732-4ddd-bdc4-3e0d25d35d07)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/62a32936-dc5f-4a68-bdee-ca62a5e17326)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/0ea30850-7239-4d37-be4a-fdb765a7692c)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/7484d201-943a-42d4-84db-04a0ebda76a0)

![dswqadea](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/db54ce4d-ccd0-4f49-9995-5f72ef0a0204)

## Task-02: Use terraform to demonstrate usage of List, Set and Object datatypes

**Let's use `type - list` to create files--->**

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/e50f7dc8-897e-45f3-98ea-ac85fd6bde14)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/dc36da2a-2adb-4915-ad59-917cb7c890f6)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/f8492f59-86fd-40dc-9823-cd068f670061)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/e275e244-3f77-4979-8fa1-3528d499fc00)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/c3c76083-dc67-4411-8924-2a1a4de09471)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/37922f28-d4ee-4c23-ae66-94969994e6f9)

**Let's use `type - set` to create files--->**

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/bf464904-2015-4993-9e39-38716fecb71f)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/0c4cc435-c16b-46c0-9274-dd27644cd3b2)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/8a93fe54-c185-46b7-81e0-d382fcae954d)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/895a1158-ae24-41d6-8e6e-6e1e914f519d)

![vdfvs](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/24d146b6-0de3-4723-8e2a-95c02699d672)

**Let's use `type - Object` to create files--->**

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/906293f4-2030-4493-b18d-646c57ec1076)

```sh
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }
  required_version = "~> 1.3.9"
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_security_group" "main" {
  name_prefix = "${var.aws_ec2_object.name}-sg"
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

resource "aws_instance" "ec2" {
  count = var.aws_ec2_object.instances

  ami           = var.aws_ec2_object.ami
  instance_type = var.aws_ec2_object.instance_type
  key_name      = element(var.aws_ec2_object.keys, count.index)
  vpc_security_group_ids = [aws_security_group.main.id]

  tags = {
    Name = "${var.aws_ec2_object.name}-${count.index+1}"
  }
}
```

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/f68990ef-56ef-47af-ac4b-fd36fc1a9659)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/4d6fddb5-2c8c-44ac-9646-6a3c74244577)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/62280152-8ae9-4259-a42b-6bc860f28af8)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/4bbe7475-4523-40d8-8578-fe11544ac169)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/3b7d165f-3ed6-4549-9585-b29d6e6badb8)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/9350fb2c-7233-4093-8f3f-c03ba800efc6)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/7ada7635-4737-499e-8fa6-2358128bddf8)

**Use of `terraform refresh`**

To refresh the state by your configuration file, reloads the variables

terraform refresh is used to update the state file with the real-world state of the resources that are already managed by Terraform.

When a Terraform configuration is applied using terraform apply or terraform plan, the state file is updated with the latest state of the resources. However, it's possible for the state file to become out of sync with the real-world state of the resources being managed. For example, if a resource is manually edited, created, or destroyed outside of Terraform, the state file will no longer accurately reflect the true state of the resource.

terraform refresh can be used to remedy this issue. This command refreshes the state file from the real-world state of the resources, ensuring that the state file accurately reflects the current state of the resources.

It's a good practice to run terraform refresh before running terraform plan to ensure that the Terraform state file is up to date with the real-world resources. This helps avoid any potential problems that might arise from applying a configuration based on stale or inaccurate state information.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/667c2ea7-a836-4e1e-bd77-0f5eb0741a49)

**Happy Learning :)**

# Day 63 task is complete!
