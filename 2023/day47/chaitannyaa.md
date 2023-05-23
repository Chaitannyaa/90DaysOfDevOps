# Day 47: Test Knowledge on aws 💻 📈

## Task-01

- Launch an EC2 instance using the AWS Management Console and connect to it using SSH.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/3403458f-31c7-4367-8e86-a238f91e1dc8)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/5f706f10-8524-42ca-905c-24ec9ce4ce58)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/e1fa7851-5966-4af7-bc21-154583b87a4b)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/e6f4f1b2-41d4-427c-b734-b35dded40d80)

- Install a web server on the EC2 instance and deploy a simple web application.

```sh
#!/bin/bash

sudo apt update -y 

# Install Apache2
sudo apt install -y apache2

# Start Apache2 service
sudo systemctl start apache2

# Enable Apache2 to start on boot
sudo systemctl enable apache2
```
![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/f3a66da8-7446-4a65-b2c5-225660f0f7f3)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/5284181c-9ca7-4eef-a24f-62730c8bbe5f)

- Monitor the EC2 instance using Amazon CloudWatch and troubleshoot any issues that arise.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/eb9eda44-26e5-459a-9b06-9969bea8c230)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/fc4eb4b6-d3a1-4f81-a023-cf6fcba7211f)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/06bd6130-6029-40db-befe-32bcfbc5733a)

## Task-02

- Create an Auto Scaling group using the AWS Management Console and configure it to launch EC2 instances in response to changes in demand.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/5ddc1568-736d-45c3-bf70-52cf31a007dc)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/4dade6bc-78c8-462c-9f26-26bf87db9b15)

- Use Amazon CloudWatch to monitor the performance of the Auto Scaling group and the EC2 instances and troubleshoot any issues that arise.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/705b81c7-ba76-4ba0-b192-62f94cffa6b5)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/d6e4fa5d-15c4-4c30-b481-c40d4ae67c56)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/76e3d1f1-ca08-49be-80d1-3c614ab24844)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/c8dbf1d4-61c0-40b7-8c2a-614e0bea7592)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/8f8ae36c-9e8d-45f2-a5a2-83f5c855fafc)

- Use the AWS CLI to view the state of the Auto Scaling group and the EC2 instances and verify that the correct number of instances are running.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/9f2b0f50-69ef-4e09-86b0-e9ebc47ee65e)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/d8fba948-6779-442d-b15e-613dac168e22)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/f4392430-0884-4eec-b195-c7aaf6f9bc36)

We hope that these tasks will give you hands-on experience with aws services and help you understand how these services work together. If you have any questions or face any issues while doing the tasks, please write in the comments.

Happy Learning :)

# Day 47 task is complete!
