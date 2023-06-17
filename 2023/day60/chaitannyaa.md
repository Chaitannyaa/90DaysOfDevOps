# Day 60 - Terraform🔥
Hello Learners , you guys are doing every task by creating an ec2 instance (mostly). Today let’s automate this process . How to do it ? Well Terraform is the solution .

## What is Terraform?
   
- Terraform is an infrastructure as code (IaC) tool that allows you to create, manage, and update infrastructure resources such as virtual machines, networks, and storage in a repeatable, scalable, and automated way.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/ac524856-7b80-4c0e-9262-f9e07e0aeeda)

## Task 1:

Install Terraform on your system
Refer this [link](https://phoenixnap.com/kb/how-to-install-terraform) for installation 

## Task 2: Answer below questions

- Why do we use Terraform?

Terraform developed by HashiCorp, is an open-source infrastructure provisioning and management tool that allows you to define and manage your infrastructure as code. Terraform streamlines infrastructure provisioning, enhances scalability and promotes consistency through the power of Infrastructure as Code.

**Here are some reasons why Terraform has gained popularity among engineers and DevOps teams:**

**Declarative Language:** Terraform uses a declarative language to define infrastructure as code, making it human-readable and version-control friendly. This approach eliminates manual provisioning and configuration steps, reducing human error and enhancing reproducibility.

**Cloud-Agnostic:** Terraform supports multiple cloud providers, including AWS, Azure, Google Cloud Platform, and more. This allows you to create and manage infrastructure across different clouds using a consistent workflow, simplifying multi-cloud deployments and migrations.

**Infrastructure Lifecycle Management:** Terraform handles the entire lifecycle of infrastructure, from provisioning to scaling and even destruction. With Terraform, you can easily manage infrastructure changes, enforce best practices, and enable efficient collaboration among teams.

- What is Infrastructure as Code (IaC)?

Infrastructure as Code (IaC) is an approach that involves managing infrastructure using machine-readable configuration files, rather than manual processes. By treating infrastructure as code, IaC enables automation, version control, and collaboration, resulting in faster and more reliable deployments.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/1abb36e6-cd76-4918-a7bb-d581446f7936)

**Below is a sample Terraform configuration file that demonstrates how to provision an EC2 instance with a web server using Terraform from code-->**

```sh
#main.tf

provider "aws" {
  region = "us-east-1" 
}

resource "aws_instance" "mywebserver" {
  ami           = "ami-0c94855ba95c71c99"  # Update with your desired AMI ID
  instance_type = "t2.micro"  # Update with your desired instance type
  key_name = "your-key-pair"  # Update with your EC2 key pair name
  
  tags = {
    Name = "web-server-instance"
  }

  user_data = <<-EOF
    #!/bin/bash
    sudo apt update
    sudo apt install -y apache2
    sudo systemctl enable apache2
    sudo systemctl start apache2
  EOF
}

output "public_ip" {
  value       = aws_instance.mywebserver.public_ip
  description = "Public IP address of the EC2 instance"
}
```

In this terraform script/ configuration file, we're creating an AWS EC2 instance and configuring it as a web server. Here's a breakdown of the key components:

- The provider block specifies the AWS region where the EC2 instance will be launched. You can update the region attribute with your preferred region.

- The resource block of type aws_instance defines the EC2 instance. It specifies the Amazon Machine Image (AMI) ID, instance type, tags, and other configuration details.

- The user_data section is a Bash script that runs when the instance is launched. In this case, it updates the package repositories, installs Apache HTTP Server, and starts the service.

- The output block defines an output variable to display the public IP address of the created EC2 instance.

Once you have the main.tf file ready, you can run `terraform init`, `terraform plan`, and `terraform apply` to provision the EC2 instance with the web server ready.

- What is a Resource?

In Terraform, a resource is a fundamental building block used to represent and manage infrastructure objects within a specific provider, such as AWS, Azure, or Google Cloud Platform.

Resources are defined in Terraform configuration files (.tf files) and are the core elements responsible for provisioning, modifying, and destroying infrastructure components. A resource in Terraform can represent various entities, such as virtual machines, databases, networks, storage buckets, security groups, load balancers, and more. Each resource has a specific set of attributes that define its properties and configuration.

For example, an EC2 instance resource may have attributes like ami (Amazon Machine Image), instance_type, subnet_id, and tags.

```sh
resource "aws_instance" "appserver" {
  ami           = "ami-12345678"   # your desired AMI ID
  instance_type = "t2.micro"
  subnet_id     = "subnet-12345678"   # your desired subnet ID

  tags = {
    Name        = "appInstance"
    Environment = "Production"
  }
}
```

- What is a Provider?

In Terraform, a provider is a plugin that acts as an interface between Terraform and a specific cloud provider, infrastructure platform, or service. Providers enable Terraform to interact with and manage resources within the target platform.

Each cloud provider or service typically has its provider plugin, developed and maintained either by the provider itself or by the open-source community. Examples of popular providers include AWS, Azure, Google Cloud Platform, and many others.

**AWS provider in Terraform:**

```sh
provider "aws" {
  region = "us-east-1"  # Update with your desired AWS region
  access_key = "YOUR_AWS_ACCESS_KEY"
  secret_access_key = "YOUR_AWS_SECRET_ACCESS_KEY"
}
```

In this example, we're configuring the AWS provider. The provider block specifies the provider name as "aws"

**Google Cloud Provider in Terraform:**

```sh
provider "google" {
  project     = "YOUR_GCP_PROJECT_ID"
  credentials = file("path/to/your/gcp/credentials.json")
}
```

In this example, we're configuring the Google Cloud provider Google. The required attributes include project (your GCP project ID) and credentials (the path to your GCP service account credentials JSON file).

- What is a State file in Terraform & its importance?

The state file in Terraform serves as a record of the infrastructure managed by Terraform. It keeps track of the relationships between resources, their attributes, and their current state.

Terraform is a stateful application. This means that it keeps track of everything it builds in your cloud environments so that if you need to change something or delete something later, Terraform will know what it built, and it can go back and make those changes for you.

By default, when you run terraform apply inside a folder /ubuntu/project, it will create the file /ubuntu/project/terraform.tfstate.

**The state file plays a pivotal role in Terraform's workflow and provides several key benefits:**

**Infrastructure Tracking:** The state file acts as a source of truth for the infrastructure managed by Terraform. It allows you to view the current state, track changes over time, and collaborate effectively across teams.

**Resource Dependencies:** By maintaining a state file, Terraform understands the dependencies between resources. It ensures that resources are created, updated, or destroyed in the correct order, preventing potential issues.

**Safeguarding Infrastructure:** The state file contains sensitive information like resource IDs and connection details. Storing it securely and managing access helps protect the infrastructure from unauthorized changes.

- What is Desired and Current State?

In Terraform, the desired state refers to the state that you define in your Terraform configuration files. It represents the infrastructure configuration you want to achieve. The desired state describes the resources you want to create, their properties, and their relationships.

On the other hand, the current state represents the actual state of the infrastructure as recorded in the state file. It reflects the current state of the resources managed by Terraform, including any changes that have been made since the last Terraform operation. The current state is determined by comparing the desired state with the state file.

By understanding the desired and current state, Terraform enables you to make infrastructure changes in a predictable and controlled manner.

**Let’s see if you provisioned the ec2 instance with t2.micro instance type using the below code--->**

```sh
provider "aws" {
    region = "us-east-1"
    access_key = "<access_key>"
    secret_key = "<secret_key>"
}
resource "aws_instance" "Ubuntu" {
  ami           = "ami-0ca285d4c2cda3300"
  instance_type = "t2.micro"
}
```

**Now let’s modify the instance_type to t2.medium**

```sh
provider "aws" {
    region = "us-east-1"
    access_key = "<access_key>"
    secret_key = "<secret_key>"
}
resource "aws_instance" "Ubuntu" {
  ami           = "ami-0ca285d4c2cda3300"
  instance_type = "t2.medium"
}
```

**Run the terraform plan**

Terraform will detect the changes between the desired state (t2.medium) and the current state (t2.micro)

```sh
# aws_instance.Ubuntu will be updated in-place
  ~ resource "aws_instance" "Ubuntu" {
        id                                   = "i-0a84f30f5656d7800"
      ~ instance_type                        = "t2.micro" -> "t2.medium"
        tags                                 = {
            "Name" = "terraform"
        }
        # (28 unchanged attributes hidden)# (6 unchanged blocks hidden)
    }Plan: 0 to add, 1 to change, 0 to destroy.
```

You can modify your desired state to reflect the desired infrastructure changes, and Terraform will automatically apply those changes while ensuring that the infrastructure converges to the desired state.

**Summary:**

Terraform empowers organizations to embrace Infrastructure as Code, delivering numerous benefits such as automation, scalability, and reproducibility. Understanding the importance of the state file and the relationship between the desired and current state is essential for harnessing the full potential of Terraform.

By leveraging the power of Terraform's desired versus current state comparison, you can confidently manage infrastructure changes, ensure consistency, and build a robust and resilient infrastructure environment.

# Day 60 task is complete!

**Happy Learning:)**
