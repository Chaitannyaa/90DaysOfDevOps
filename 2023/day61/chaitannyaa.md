# Day 61- Terraform🔥

## Find purpose of following basic Terraform commands which you'll use often--->

1. `terraform init` - Initializes the Terraform working directory and downloads the necessary plugins. It's used to set up a new or existing Terraform configuration.

2. `terraform init -upgrade` - Upgrades the installed Terraform modules/plugins to the latest version which meets the declared version constraint in the configuration. 

3. `terraform plan` - Creates an execution plan that describes what Terraform will do when you execute the `terraform apply` command. It gives you a preview of the changes before they are applied to your infrastructure.

4. `terraform apply` - Applies the changes to your infrastructure according to the execution plan created by `terraform plan`.

5. `terraform validate` - Checks and verifies the syntax and integrity of the Terraform configuration files. It ensures that Terraform can interpret the configuration files correctly.

6. `terraform fmt` - Automatically updates and standardizes the formatting of your configuration files for better readability.

7. `terraform destroy` - Destroys all of the resources that were created by the `terraform apply` command, effectively removing the infrastructure from your provider. It is used to clean up all the resources created by the Terraform configuration.

## Regarding Terraform's competitors, some of the main ones are:

Terraform is a popular choice in the market, there are several competitors and alternatives available that offer similar functionality. Some of the notable competitors to Terraform are:

1. AWS CloudFormation: AWS CloudFormation is a service provided by Amazon Web Services (AWS) for provisioning and managing resources in an AWS environment. It allows users to define infrastructure as code using JSON or YAML templates and offers deep integration with other AWS services.

2. Azure Resource Manager (ARM) Templates: Azure Resource Manager is the deployment and management service provided by Microsoft Azure. ARM Templates enable users to define and deploy infrastructure and resources in Azure using JSON templates.

3. Google Cloud Deployment Manager: Google Cloud Deployment Manager is an infrastructure deployment service offered by Google Cloud Platform (GCP). It allows users to define and manage resources using YAML or Python templates, providing similar functionality to Terraform.

4. Ansible: Ansible is an open-source automation tool that provides infrastructure-as-code capabilities. It allows users to define and manage infrastructure using simple, human-readable YAML files. Ansible can be used to automate provisioning and configuration management tasks across a variety of platforms, including cloud environments.

5. Puppet: Puppet is a configuration management and automation tool that can be used for infrastructure provisioning. It provides a declarative language to define infrastructure resources and manage their configuration across different systems.

6. Chef: Chef is another popular configuration management and automation tool that supports infrastructure provisioning. It offers a domain-specific language (DSL) to define infrastructure resources and manage their configuration.

These are just a few examples of competitors and alternatives to Terraform. The choice of tool depends on various factors, such as the cloud provider being used, specific requirements, existing infrastructure, and personal preferences.

**Happy Learning :)**

# Day 61 task is complete!
