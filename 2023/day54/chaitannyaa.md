# Day 54: Understanding Infrastructure as Code and Configuration Management

## What's the difference bhaiyya?

When it comes to the cloud, Infrastructure as Code (IaC) and Configuration Management (CM) are inseparable. With IaC, a descriptive model is used for infrastructure management. To name a few examples of infrastructure: networks, virtual computers, and load balancers. Using an IaC model always results in the same setting.

Throughout the lifecycle of a product, Configuration Management (CM) ensures that the performance, functional and physical inputs, requirements, design, and operations of that product remain consistent.

# Task-01

# Read more about IaC and Config. Management Tools

## IaC
Infrastructure-as-Code is used to automatically create any service or system in the cloud or on-prem with code. The code is typically a provisioning language, like JSON or YAML. However, that's changing rapidly with HashiCorp Configuration Language (HCL), which is a much easier and human-readable language compared to JSON and YAML to write infrastructure code.

## Config. Management
Configuration could consist of starting services, installing dependencies, installing applications, running updates, and much more, so it was a lot of manual effort. A few companies saw this problem and decided to make a type of tool to automate these tasks. The tool was Configuration Management.

Configuration Management is a way to configure servers. 

The configuration could be:

- Installing applications
- Ensuring services are stopped or started
- Installing updates
- Opening up ports

# Give differences on both with suitable examples

The main difference between Infrastructure as Code (IaC) and Configuration Management (CM) is that IaC focuses on managing and provisioning infrastructure through code, while CM focuses on automating the configuration and management of software applications, operating systems, and servers.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/45d4e018-b88b-4da7-be47-8c4c554512fb)

- Infrastructure provisioning tool Terraform is responsible for providing the network and servers
- Configuration management tool Ansible configures applications inside servers provisioned by Terraform.

# What are most common IaC and Config management Tools?

Let's say you're a startup and you're primarily using Serverless and Container technologies to deploy apps. Realistically, you don't need Configuration Management. You just need an automated way to create the Serverless service or the containers. Maybe you use an IaC tool to create a Lambda Function, for example.

On the flip side, maybe you're an organization like AWS that has a pretty important job; provisioning and configuring servers. Behind the AWS UI is a server running on a virtualized platform, and that server needs to be configured with the dependencies that are needed to run AWS. If you're at a company where bare metal or virtualized servers are still very much the way business is done, ConfigMgmt makes sense.

## Most Commonly used IaC and Config Management Tools:

### IaC Tools: 

a) Terraform: A most popular tool that supports multiple cloud providers and enables infrastructure provisioning using declarative code. 

b) AWS CloudFormation: Specific to Amazon Web Services (AWS), it allows infrastructure provisioning using JSON or YAML templates. 

c) Azure Resource Manager: Microsoft Azure's native IaC tool that uses JSON templates for infrastructure provisioning.

### Configuration Management Tools: 

a) Ansible: An open-source automation tool that uses a simple, human-readable language to manage configurations across servers. 

b) Puppet: A powerful tool for managing complex infrastructures, allowing centralized management and configuration enforcement. 

c) Chef: Another popular configuration management tool that automates infrastructure management using a domain-specific language (DSL).


Write a blog on this topic in the most creative way and post it on linkedIn :)

https://www.linkedin.com/posts/chaitannyaa-gaikwad-b16965115_day54-90daysofdevops-challenge-tws-activity-7068214744188432384--C-u?utm_source=share&utm_medium=member_desktop

### Happy learning:)

# Day 54 task is complete !
