# Day 52: Your CI/CD pipeline on AWS - Part 3 🚀 ☁

On your journey of making a CI/CD pipeline on AWS with these tools, you completed AWS CodeCommit & CodeBuild.

Next few days you'll learn these tools/services:

- CodeDeploy
- CodePipeline
- S3

## What is CodeDeploy ? 

AWS CodeDeploy is a deployment service that automates application deployments to Amazon EC2 instances, on-premises instances, serverless Lambda functions, or Amazon ECS services.

CodeDeploy can deploy application content that runs on a server and is stored in Amazon S3 buckets, GitHub repositories, or Bitbucket repositories. CodeDeploy can also deploy a serverless Lambda function. You do not need to make changes to your existing code before you can use CodeDeploy.

# Task-01 :
- Read about Appspec.yaml file for CodeDeploy.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/dd81c9b3-f821-447f-b9b0-fcbfe61c9fb1)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/50eaded9-f171-4323-b2c0-4ca1a211ec02)

### Create a Ec2 role first--->

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/8c702dd0-ab50-4b9b-8386-c1c363f2043d)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/5b1c1a4b-6342-4d5f-97b4-104ffccc40da)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/4f063c6e-01fd-4824-a2db-3abd538f74e2)

### Create application--->

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/ee0000c9-7501-4b9e-ba1f-7f6a381f5979)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/087d0d02-1193-4e86-b85a-63eba2c3eb0d)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/8e3f5828-532b-4676-9303-7a2738834e0a)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/29c1a066-84dc-4073-a6b2-b15507eb3bbb)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/086eadaa-24d0-4f6e-bb86-788061df33bd)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/6f146205-5fd5-4ea0-8997-94a73c6f5292)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/52848195-5fba-41fb-ac1d-544670eb3739)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/7268b636-4950-43ef-b94a-cb4a609b68b9)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/a62130f9-5f46-495a-97c7-e337c989f732)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/de141f0c-3a38-4176-923a-93fdeaf35af0)

https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html

- You have to setup a CodeDeploy agent in order to deploy code on EC2.

In order to deploy your app to EC2, CodeDeploy needs an agent which actually deploys the code on your EC2.

Create a shell script with the below contents and run it

install.sh
----------------------
```sh
#!/bin/bash 
# This installs the CodeDeploy agent and its prerequisites on Ubuntu 22.04.  
sudo apt-get update 
sudo apt-get install ruby-full ruby-webrick wget -y 
cd /tmp 
wget https://aws-codedeploy-us-east-1.s3.us-east-1.amazonaws.com/releases/codedeploy-agent_1.3.2-1902_all.deb 
mkdir codedeploy-agent_1.3.2-1902_ubuntu22 
dpkg-deb -R codedeploy-agent_1.3.2-1902_all.deb codedeploy-agent_1.3.2-1902_ubuntu22 
sed 's/Depends:.*/Depends:ruby3.0/' -i ./codedeploy-agent_1.3.2-1902_ubuntu22/DEBIAN/control 
dpkg-deb -b codedeploy-agent_1.3.2-1902_ubuntu22/ 
sudo dpkg -i codedeploy-agent_1.3.2-1902_ubuntu22.deb 
systemctl list-units --type=service | grep codedeploy 
sudo service codedeploy-agent status
```
![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/e3605f8c-02b8-47c1-af4b-0144ecde6dc1)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/59f939d3-76e6-4c92-9a14-d1f8145df737)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/e27a74db-f92b-4784-ba09-a170a6b12d35)

- Add appspec.yaml file to CodeCommit Repository and complete the deployment process.

```sh
version: 0.0

os: linux

files:
  - source: /
    destination: /var/www/html/
hooks:
  AfterInstall:
    - location: scripts/install_nginx.sh
      timeout: 300
      runas: root
  ApplicationStart:
    - location: scripts/start_nginx.sh
      timeout: 300
      runas: root
```
![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/cd2068a7-3a38-49d4-8323-566c8924b3e8)

```sh
#install_nginx.sh
#!/bin/bash
sudo apt-get update
sudo apt-get install -y nginx
```

```sh
#start_nginx.sh
#!/bin/bash
sudo service nginx start
```

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/9a9266bf-26af-4c6a-84e2-a629e28f9b3c)

- Make sure your artifact is created inside S3 bucket.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/bfa5cdec-b164-42b1-bf17-64c6c844f48c)

- Deploy index.html file on EC2 machine using nginx.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/bdf00f35-55b9-468e-99f6-0b7debd1d2b1)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/1e1564b6-b6a9-4b3b-80c0-e403fc7ee7a9)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/51fe46b7-ce8d-4317-ba1f-6d71ca174fa0)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/78090364-8378-45ed-abb7-8e208c17606a)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/1ae724c4-5795-40ed-9aa8-9579554a2a42)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/dec9e8af-7c7c-4dc4-8a13-4f40a1584b9d)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/52aa6770-2e48-4b7c-9290-58344f622d96)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/4c9c32c6-4d4f-4e03-b3f5-9bff4a6aa3f5)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/ca53fd77-6baf-4674-9410-97c60931cb14)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/9e552f7e-67e6-42e3-a184-294529518195)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/1e7ebb7c-2c31-4967-a9ba-ad881b3a13b9)

Happy Learning :)

# Day 52 task is complete!




