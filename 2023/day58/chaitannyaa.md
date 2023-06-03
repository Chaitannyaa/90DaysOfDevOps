# Day 58: Ansible Playbooks

Ansible playbooks run multiple tasks, assign roles, and define configurations, deployment steps, and variables. If you’re using multiple servers, Ansible playbooks organize the steps between the assembled machines or servers and get them organized and running in the way the users need them to. Consider playbooks as the equivalent of instruction manuals.

# Task-01

- Write an ansible playbook to create a file on a different server

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/e2f05c0b-a982-45b5-a065-685a0450dbf3)

`$ ansible-inventory --list -y`

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/3fdb4171-e0fd-4f97-88b5-38766df09244)

`$ ansible servers -m ping`

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/83da4329-3afa-4675-ae72-98a058941291)

`$ vim create_file.yml`

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/4c341c48-62c2-4413-b445-4c9528bdfb71)

`ansible-playbook create_file.yml`

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/04c0bb59-ff89-4666-84dc-4389b65fc88b)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/0eb87090-b04d-4d0f-a916-20fa3625afec)

- Write an ansible playbook to create a new user.

- Write an ansible playbook to install docker on a group of servers

Watch [this](https://youtu.be/089mRKoJTzo) video to learn about ansible Playbooks

# Task-02

- Write a blog about writing ansible playbooks with the best practices.

Let me or anyone in the community know if you face any challenges

happy Learning :)
