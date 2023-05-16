# Day 38 Getting Started with AWS Basics☁
![AWS](https://user-images.githubusercontent.com/115981550/217238286-6c6bc6e7-a1ac-4d12-98f3-f95ff5bf53fc.png)

## AWS:
Amazon Web Services is one of the most popular Cloud Provider that has free tier too for students and Cloud enthutiasts for their Handson while learning (Create your free account today to explore more on it).

Read from [here](https://aws.amazon.com/what-is-aws/)

## IAM:
AWS Identity and Access Management (IAM) is a web service that helps you securely control access to AWS resources. With IAM, you can centrally manage permissions that control which AWS resources users can access. You use IAM to control who is authenticated (signed in) and authorized (has permissions) to use resources.

Read from [here](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)
Get to know IAM more deeply [Click Here!!](https://www.youtube.com/watch?v=ORB4eY8EydA)

### Task1:

- Create an IAM user with username of your own wish and grant EC2 Access. 

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/c1af4cc8-c8fe-43bf-af30-15698db95377)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/b23a595b-bc46-4e9e-8a6f-8ced0a9d63d9)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/a74fa5d7-f611-4ec0-bf61-6d9d856d72de)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/86684be6-3f94-4568-ba89-781552ef8a6c)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/95075a99-5770-4b3e-b5bd-41f9b443c6ae)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/d7d1ee8c-c485-4c79-85d4-497df724b7f1)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/fa90e58d-5639-4e71-908d-2dba559b3a44)


- Launch your Linux instance through the IAM user that you created now and install jenkins and docker on your machine via single Shell Script.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/4db55fd9-ef07-4b25-a29f-e4409c15ea2a)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/cfd1f25b-1c40-4ae3-a6d4-604994e84be0)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/c5ad56bc-0678-4883-9ec4-6f57de89b700)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/94ebf570-69b4-44d8-802b-f21afbb64016)

```sh
# SHELL SCRIPT TO INSTALL DOCKER AND JENKINS

# Install Docker
sudo yum update
sudo yum install docker -y
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER

# Install Jenkins
# Jenkins requires Java to run, so first install Java
sudo yum update
sudo yum install java-11-openjdk -y

# Long-Term Support release of Jenkins
sudo wget -O /etc/yum.repos.d/jenkins.repo \
    https://pkg.jenkins.io/redhat-stable/jenkins.repo
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key
sudo yum upgrade

# Add required dependencies for the jenkins package
sudo yum install java-11-openjdk -y 
sudo yum install jenkins -y
sudo systemctl daemon-reload
sudo systemctl enable jenkins
sudo systemctl start jenkins

# Verify installations
docker --version
java -version
jenkins --version
sudo systemctl status jenkins
```
![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/9ece8695-702e-4005-a8ba-d3540d2d1078)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/eaf5d5df-effa-457c-90da-fc7647df0a5d)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/de18d76b-3267-4308-86a8-c02aac3ec2e0)

### Task2:

- In this task you need to prepare a devops team of avengers. Create 3 IAM users of avengers and assign them in devops groups with IAM policy.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/0bf9a772-3d3c-45e9-8cb5-03b6e43f9233)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/2ee3076d-2c4c-4033-84e7-c3052707ff5f)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/c6209d38-20c3-4043-ab6b-f003ef05f735)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/b5775152-8c47-4db9-89de-28bdd769ef52)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/1dda6182-4ef5-4819-b016-e22072992d27)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/c3d2092d-a138-4d87-925c-e5cae78370dd)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/635c1fb0-d592-48c5-a581-bb12da5221f9)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/836af663-e23c-4b9b-acf2-3134c815d860)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/05b55d38-5bdc-4b20-9136-d87b94a35346)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/61371d5b-0692-406d-9fee-ec86328d9087)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/af095225-2ed7-44c4-8589-9ad7c8bacfe1)

That's all about the task!
Happy Learning :)

# Day38 task is completetd!
