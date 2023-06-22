# Day 69 - Meta-Arguments in Terraform

## What are meta-arguments and its use in Terraform.

When working with Terraform, you'll often come across situations where you need to provide additional configuration or define behaviors for your resources. This is where meta-arguments come into play. Meta-arguments are special attributes that can be used to control the behavior of resources and modules in Terraform. In this guide, we'll explore some commonly used meta-arguments with code snippets and examples.

### 1. `depends_on`

The `depends_on` meta-argument is used to specify explicit dependencies between resources. It allows you to define the order in which resources are created or updated. This is useful when you have resources that rely on each other or when you need to ensure a specific execution order.

```terraform
resource "aws_instance" "web" {
  # Resource configuration...

  depends_on = [aws_security_group.web_sg]
}

resource "aws_security_group" "web_sg" {
  # Resource configuration...
}
```

In this example, the `web` instance depends on the `web_sg` security group. Terraform will ensure that the security group is created or updated before creating or updating the instance.

### 2. `count`

The `count` meta-argument allows you to create multiple instances of a resource based on a count value. It is commonly used when you need to provision multiple resources with similar configurations, such as multiple EC2 instances or multiple subnets.

```terraform
resource "aws_instance" "web" {
  count = 3

  # Resource configuration...
  tags = {
    Name = "web-${count.index}"
  }
}
```

In this example, three EC2 instances will be created, and the `count.index` variable is used to assign unique names to each instance.

### 3. `for_each`

Similar to `count`, the `for_each` meta-argument allows you to create multiple instances of a resource, but it uses a map or set of values instead of a count. It is useful when you have a dynamic list of configurations or when you want to iterate over a collection of resources.

```terraform
variable "regions" {
  type    = set(string)
  default = ["us-west-1", "us-east-1"]
}

resource "aws_instance" "web" {
  for_each = var.regions

  # Resource configuration...
  tags = {
    Name        = "web-server"
    Environment = each.key
  }
}
```

In this example, an EC2 instance will be created for each region specified in the `regions` variable. The `each.key` variable provides the current iteration key, which is used to assign the environment tag.

### 4. `provider`

The `provider` meta-argument is used to define the provider configuration for a resource. It allows you to specify which provider should be used to manage the resource.

```terraform
resource "aws_s3_bucket" "example" {
  provider = aws.my_custom_provider

  # Resource configuration...
}
```

In this example, the `example` S3 bucket resource is associated with a custom provider named `aws.my_custom_provider`.

### 5. `lifecycle`

The `lifecycle` meta-argument provides advanced control over resource lifecycle management. It allows you to configure behaviors such as preventing resource deletion, controlling resource replacement, and managing resource updates.

```terraform
resource "aws_instance" "web" {
  lifecycle {
    prevent_destroy = true
  }

  # Resource configuration...
}
```

In this example, the `web` instance is protected from being destroyed accidentally due to the `prevent_destroy` setting.

**Understanding and utilizing these meta-arguments will help you control the behavior and dependencies of your resources effectively.**


## Task - Demonstrate the use of Count and for_each.

When you define a resource block in Terraform, by default, this specifies one resource that will be created. To manage several same resources with similiar configurations, you can use either count or for_each, which removes the need to write a separate block of code for each one. Using these options reduces overhead and makes your code neat and clean.

'count' is known as a ‘meta-argument’ defined by the Terraform language. Meta-arguments help achieve certain requirements within the resource block.

## Count

The 'count' meta-argument accepts a whole number and creates the number of instances of the resource specified.

When each instance is created, it has its own distinct infrastructure object associated with it, so each can be managed separately. When the configuration is applied, each object can be created, destroyed, or updated as appropriate.

```sh
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "server" {
  count = 3
  ami = "ami-053b0d53c279acc90"
  instance_type = "t2.micro"
  tags = {
    Name = "Instance - ${count.index}"
  }
}
```

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/dbd94983-93f4-4784-a270-278fe09bfcdc)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/d814bef0-eddb-42e0-adc9-66a98bb3297c)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/73793d5e-8280-49f0-9119-41efdc8696a0)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/839846bd-3b68-4c4d-a3e3-3dfc1cfa8551)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/1b8a5ac7-447e-4d63-9def-84d5312a115d)


## for_each

Like the count argument, the for_each meta-argument creates multiple instances of a module or resource block. However, instead of specifying the number of resources, the for_each meta-argument accepts a map or a set of strings. This is useful when multiple resources are required that have different values. Consider our Active directory groups example, with each group requiring a different owner.

```sh
provider "aws" {
  region = "us-east-1"
}

locals {
  ami_ids = toset([
    "ami-0b0dcb5067f052a63",  
    "ami-08c40ec9ead489470", 
    ])
}

resource "aws_instance" "server" {
  for_each = local.ami_ids
  ami = each.key
  instance_type = "t2.micro"
  tags = {
    Name = "Server ${each.key}"
  }
}
```

### Multiple key value iteration

```sh
locals {
  ami_ids = {
    "Amazon_linux" :"ami-022e1a32d3f742bd8",
    "Ubuntu": "ami-053b0d53c279acc90",
  }
}

resource "aws_instance" "server" {
  for_each = local.ami_ids
  ami = each.value
  instance_type = "t2.micro"
  tags = {
    Name = "${each.key} - Instance"
  }
}
```

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/ed69982b-746c-4101-86d6-307714371917)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/d9a0ec0b-c570-4367-b92f-3d9da265c6f9)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/1027c950-63b5-43ee-bb53-0171ef3a4b32)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/b051ac73-7911-409d-989d-ecad6994ee36)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/48f9b917-0d06-4dc3-a517-c41a59e2c47c)

**Happy learning :)**

# Day 69 task is complete!

