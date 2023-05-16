# Day 39 AWS and IAM Basics☁
![AWS](https://miro.medium.com/max/1400/0*dIzXLQn6aBClm1TJ.png)

## User Data in AWS:
- When you launch an instance in Amazon EC2, you have the option of passing user data to the instance that can be used to perform common automated configuration tasks and even run scripts after the instance starts. You can pass two types of user data to Amazon EC2: shell scripts and cloud-init directives.
- You can also pass this data into the launch instance wizard as plain text, as a file (this is useful for launching instances using the command line tools), or as base64-encoded text (for API calls).
- This will save time and manual effort everytime you launch an instance and want to install any application on it like apache, docker, Jenkins etc

Read more from [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html)

## IAM Roles

IAM (Identity and Access Management) roles in AWS (Amazon Web Services) are a secure way to grant permissions to entities, such as AWS services, users, or applications, to access AWS resources. IAM roles are different from IAM users in that they are not associated with a specific individual or service account.

## Task1:

- Launch EC2 instance with userdata to install Jenkins on it. Once server shows up in console, hit the IP address in browser and you Jenkins page should be visible.

- Take screenshot of Userdata and Jenkins page, this will verify the task completion.

## Task2:

- Read more on IAM Roles and explain the IAM Users, Groups and Roles in your own terms.

- Create three Roles named: DevOps-User, Test-User and Admin.


# Day39 task is complete!
