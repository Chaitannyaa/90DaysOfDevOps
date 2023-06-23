# Day 70 - Terraform Modules

- Modules are containers for multiple resources that are used together. A module consists of a collection of .tf and/or .tf.json files kept together in a directory

- A module can call other modules, which lets you include the child module's resources into the configuration in a concise way. 

- Modules can also be called multiple times, either within the same configuration or in separate configurations, allowing resource configurations to be packaged and re-used.

# What are different types of Terraform modules?

Terraform modules are an essential component of Terraform's design that allows you to organize and reuse your infrastructure code. They provide a way to encapsulate and package resources, configurations, and other related components, making it easier to manage complex infrastructure setups and promote code reusability. 

**Different types of modules available in Terraform:**

1. **Root Modules**: The root module refers to the main configuration file that serves as the entry point for your Terraform project. It typically contains the top-level resources and acts as the foundation for your infrastructure. Root modules can include child modules or directly define resources.

```sh
module "networking" {
  source = "./modules/networking"
}

module "webserver" {
  source = "./modules/webserver"
  vpc_id = module.networking.vpc_id
}
```

2. **Child Modules**: Child modules are modules called and used within other modules or the root module. They allow you to encapsulate specific configurations or sets of resources, promoting modularity and code organization.

```sh
resource "aws_vpc" "main" {
  # ...
}

output "vpc_id" {
  value = aws_vpc.main.id 
}
```

3. **Provider Modules**: Provider modules are specialized modules that focus on configuring and managing specific infrastructure providers, such as AWS, Azure, Google Cloud, or Docker. They abstract the complexities of provider-specific APIs and enable consistent management of resources across different providers.

```sh
provider "aws" {
  region = "us-east-1"
}

module "ec2" {
  source = "github.com/terraform-aws-modules/terraform-aws-ec2-instance"
}
```

4. **Community Modules**: Community modules are pre-built modules created by the Terraform community and shared through platforms like the Terraform Registry, GitHub, or other online repositories.

```sh
module "s3_bucket" {
  source = "terraform-aws-modules/s3-bucket/aws"
  # ... 
}
```

5. **Composite Modules**: Composite modules, also known as composition modules, are modules that are built by combining and reusing other modules. They provide a way to compose complex infrastructure setups by assembling and configuring multiple modules together.

```sh
module "vpc" {
  source = "terraform-aws-modules/vpc/aws"
}

module "ec2" {
  source = "terraform-aws-modules/ec2-instance/aws"

  vpc_security_group_ids = [module.vpc.default_security_group_id]
}
```

6. **Data Modules**: Data modules in Terraform are used to retrieve and access external data or resources that are not directly managed by Terraform itself. These modules facilitate integration with external systems, such as querying APIs, fetching data from databases, or reading from external configuration files. Data modules enable Terraform to interact with external information dynamically during the planning and execution phases.

```sh
data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"] 
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"] # Canonical
}

resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t2.micro"

  # ...
}
```
Remember to leverage community modules and the Terraform Registry to benefit from pre-built modules and collaborate with the wider Terraform community.

# Difference between Root Module and Child Module.

|  | Root Module| Child Module| 
|:--|:--|:--|
|Definition| The main configuration file that acts as the entry point for your Terraform code.| A module that is imported and used within another module (the root module or another child module).|
|Contains|Top-level resources and configuration.|A specific set of resources or configurations to promote modularity and reusability.|  
|Imports| Child modules| N/A|
|Filename| Usually `main.tf` or `root.tf`| Has `variables.tf`, `outputs.tf` and `main.tf` files|
|Hierarchy|Top of the module hierarchy|Nested below the root module|
|Role|Defines the overall infrastructure| Implements reusable functionality|
|Isolated Changes|Changes to a child module do not affect the root module |Changes to the root module may affect child modules|

Example:

**`main.tf` (root module)**
```sh
module "networking" {
  source = "./modules/networking"
}

module "webserver" {   
  source = "./modules/webserver"
  vpc_id = module.networking.vpc_id
}
```

**`main.tf` (networking module)**
```sh
resource "aws_vpc" "main" {
  # ... 
}
```

# Is modules and Namespaces are same? Justify your answer for both Yes/No

 # Modules vs Namespaces

| | Modules | Namespaces |
|:--|:--|:--| 
|Physical vs Logical| Physical groups of code|Logical groupings of code|
|File Structure|Have their own files|Code grouped using declarations|
|Changes|Changes are isolated|Changes can affect other code| 
|Reusability|Allow reusing code by importing|Allow reusing names within codebase|
|Method of code storage|physical isolation and encapsulation|logical grouping within the same codebase|
|Encapsulation|Encapsulate related code|Group related code logically|

Modules and namespaces are different concepts. Modules are actual reusable code units, while namespaces are logical groupings of code within the same codebase.

### Let's use module to create resources on AWS environment--->

**ec2_module/main.tf**
```sh
# Create an AWS EC2 Instance

resource "aws_instance" "server-instance" {
  count = var.number_of_instances

  ami                    = var.ami
  instance_type          = var.instance_type        
  subnet_id              = var.subnet_id
  vpc_security_group_ids = var.security_group       

  tags = {
    Name = "${var.instance_name}-${count.index + 1}"
  }
}

output "instance_id" {
  description = "Instance ID"
  value       = aws_instance.server-instance[*].id
}
```

**ec2_module/variables.tf**
```sh
# Server Module Variables
variable "number_of_instances" {
  description = "Number of Instances to Create"
  type        = number
  default     = 1
}
 
variable "instance_name" {
  description = "Instance Name"
  type        = string
  default     = "My_Ec2_Test"
}
 
variable "ami" {
  description = "AMI ID"
  type        = string
  default     = "ami-053b0d53c279acc90"
}
 
variable "instance_type" {
  description = "Instance Type"
  type        = string
  default     = "t2.micro"
}
 
variable "subnet_id" {
  description = "Subnet ID"
  type        = string
  default     = "subnet-0fb1b21f41c1408e2"
}
 
variable "security_group" {
  description = "Security Group"
  type        = list(string)
  default     = ["sg-0277e2f4d375c8965"]
}
```

**main.tf**
```sh
provider "aws" {      
  region = "us-east-1"
}

module "launch_ec2_instance" {
  source = "./ec2_module"
}

output "instance_id" {
  description = "Instance ID"
  value       = module.launch_ec2_instance.instance_id       
}
```
![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/78ce562a-30ac-4133-a403-40d5b197890b)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/d2a66f3d-e3ee-4689-98f5-21d772f4f3e3)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/e93d4592-9128-48cb-8c69-0921726b438d)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/9ee46947-654a-487e-b04d-e7a1ed983edf)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/694a52f8-c6d6-4628-ad1b-133682f060d1)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/65bcc339-9dd8-4e59-b9a4-1d1ed35093ea)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/a51bc872-25e8-493e-8c0b-28bca9ffae0e)


**Happy learning :)**

# Day70 task is complete!
