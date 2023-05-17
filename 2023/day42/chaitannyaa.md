# Day 42: IAM Programmatic access and AWS CLI 🚀 ☁

## IAM Programmatic access

In order to access your AWS account from a terminal or system, you can use AWS Access keys and AWS Secret Access keys
Watch [this video](https://youtu.be/XYKqL5GFI-I) for more details.

## AWS CLI

The AWS Command Line Interface (AWS CLI) is a unified tool to manage your AWS services. With just one tool to download and configure, you can control multiple AWS services from the command line and automate them through scripts.

The AWS CLI v2 offers several new features including improved installers, new configuration options such as AWS IAM Identity Center (successor to AWS SSO), and various interactive features. 


## Task-01

- Create AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY from AWS Console.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/6c1a2403-2020-48dc-bc4f-055a0db1940d)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/a1741093-6d19-4663-bce7-ab18ebf3ef2c)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/cbe3e7ed-4241-47fa-bf05-bc2174a606bf)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/e915625c-a7db-40fe-ac5f-04048d2fb0b6)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/4b7db706-d8c7-4891-a703-6a7f6fda0e19)


## Task-02

- Setup and install AWS CLI and configure your account credentials

'''sh
 sudo apt-get install awscli -y
'''

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/9c2ba25c-bba9-4e27-b8d5-ee591f9de2b6)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/ef8d8514-b516-4c3a-b0fe-38148498dec7)

'''sh
aws ec2 describe-instances --region us-east-1
```
'''sh
aws ec2 describe-instances --filters "Name=instance-type,Values=t2.micro" --query "Reservations[].Instances[].InstanceId" --region us-east-1
```
![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/03b02388-e9bc-4800-bc95-761379ff8ef9)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/1dbb372a-37d1-40f1-8b5f-85bb13bf19d3)

Happy Learning :)

# Day 42 task is complete!
