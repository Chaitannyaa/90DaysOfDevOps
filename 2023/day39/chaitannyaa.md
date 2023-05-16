# Day 39 EC2 User data and IAM Roles ☁
![AWS](https://miro.medium.com/max/1400/0*dIzXLQn6aBClm1TJ.png)

## User Data in AWS:
- When you launch an instance in Amazon EC2, you have the option of passing user data to the instance that can be used to perform common automated configuration tasks and even run scripts after the instance starts. You can pass two types of user data to Amazon EC2: shell scripts and cloud-init directives.

- You can also pass this data into the launch instance wizard as plain text, as a file (this is useful for launching instances using the command line tools), or as base64-encoded text (for API calls).

- This will save time and manual effort everytime you launch an instance and want to install any application on it like apache, docker, Jenkins etc

Read more from [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html)

## IAM Roles

- IAM (Identity and Access Management) roles in AWS (Amazon Web Services) are a secure way to grant permissions to entities, such as AWS services, users, or applications, to access AWS resources. 

- IAM roles are different from IAM users in that they are not associated with a specific individual or service account.

## Task1:

- Launch EC2 instance with userdata to install Jenkins on it. Once server shows up in console, hit the IP address in browser and you Jenkins page should be visible.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/ec52c74d-1ec6-45df-bca1-286f7957e5ac)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/4c4f3237-d3ff-470a-b8fd-6c1ded0b1003)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/4e16ba0a-14d3-48df-b1bf-8f6fdb8f33eb)

- Take screenshot of Userdata and Jenkins page, this will verify the task completion.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/ea8fc510-ae0f-4e3d-9e7a-da8a28e7a963)

```sh
#!/bin/bash

#Install Docker
sudo apt-get update -y
sudo apt-get install docker.io -y
sudo usermod -aG docker $USER

#Install Jenkins
#Jenkins requires Java to run, so first install Java -->
sudo apt-get update -y
sudo apt install openjdk-11-jre -y

#Long-Term Support release of Jenkins---->

curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null

echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null

sudo apt-get update -y
sudo apt-get install jenkins -y

docker --version
java -version
jenkins --version
```
![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/75d25025-145d-4dfb-a213-dd7c336e9690)

## Task2:

- Read more on IAM Roles and explain the IAM Users, Groups and Roles in your own terms.

- IAM is a service provided by AWS that helps us to control access to our AWS resources. In IAM, there are three main entities: IAM users, groups, and roles. 

'IAM Users': IAM users are similar to user accounts. They represent individual people or services that interact with your AWS resources. Each IAM user has a unique name and credentials (username and password) or access keys (access key ID and secret access key) for programmatic access. IAM users have their own set of permissions that determine what actions they can perform on AWS resources.

'IAM Groups': IAM groups are collections or sets of IAM users. Instead of assigning permissions to individual users, you can assign permissions to groups. This simplifies permission management, as you can add or remove users from groups to grant or revoke permissions for multiple users at once.

'IAM Roles': IAM roles are a way to grant permissions to entities that are not directly associated with a specific user. Roles are often used by AWS services or applications running within your AWS infrastructure. Roles have policies attached to them that define what actions can be performed and what resources can be accessed. Roles can also establish trust relationships with other AWS accounts or external identity providers, allowing those trusted entities to assume the role and access resources.

- Create three Roles named: DevOps-User, Test-User and Admin.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/c9d3478b-b96c-45ff-9f26-225734e70f25)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/72aebbd1-910b-4815-8319-fbc332dd0cf6)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/8595cbc7-7828-4f94-964d-2418ec2935ff)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/2338c9bf-3b1b-4b3b-a0df-ed0a43bb6f48)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/974712b3-cc86-4044-b59f-e1b722d4922a)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/61b2254d-d4fa-405f-afab-74391e7ad932)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/980d7e01-81d5-4ea6-8c9e-1038020d0be3)

# Day39 task is complete!
