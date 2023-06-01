# Day 55: Understanding Configuration Management with Ansible

## What's this Ansible?

Ansible is an open-source automation tool, or platform, used for IT tasks such as configuration management, application deployment, intraservice orchestration, and provisioning

# Task-01 
- Installation of Ansible on AWS EC2 (Master Node)

`sudo apt-add-repository ppa:ansible/ansible` 

`sudo apt update`

`sudo apt install ansible -y`

`ansible --version`

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/b7bd88cc-c023-4027-9a48-68978d57b68e)

# Task-02 
- read more about Hosts file

`sudo nano /etc/ansible/hosts` 

`ansible-inventory --list -y`

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/7d9921aa-ef24-4481-bd16-30385a9d5d08)

# Task-03

- Setup 2 more EC2 instances with same Private keys as the previous instance (Node)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/65ee1037-77e3-47fa-a8d1-318c8f1df1d9)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/8c3661ca-05db-4d9a-8b0e-5cfac1dec466)

- Copy the private key to master server where Ansible is setup

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/3fcc2928-ccbb-4aef-849e-f6d061e71288)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/f56ca593-7923-4e8a-8e57-e4c1934d7764)

- Try a ping command using ansible to the Nodes.

`ansible servers -m ping`

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/744d9f00-85f5-494a-9440-09e9718e8b91)

Write a blog on this topic with screenshots in the most creative way and post it on linkedIn :)

### happy learning.

# Day 55 task is complete!
