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

`$ ansible-playbook create_file.yml`

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/04c0bb59-ff89-4666-84dc-4389b65fc88b)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/0eb87090-b04d-4d0f-a916-20fa3625afec)

- Write an ansible playbook to create a new user.

`$ vim create_new_user.yml`

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/73b94786-40c9-4b41-b3b4-6e820ac28d6b)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/923e658f-9f10-46af-81e6-08eada5e9ff9)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/13693376-443b-4ef9-9eca-de04cc15db2c)

- Write an ansible playbook to install docker on a group of servers

`$ vim install_docker.yml`

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/95c1ee6b-1155-48e9-82bc-bbd2d677be0a)

`$ ansible-playbook install_docker.yml`

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/7d78dcce-5baa-4734-916f-e10563b01590)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/bd237d62-9018-4701-be4f-8619735153f6)

Watch [this](https://youtu.be/089mRKoJTzo) video to learn about ansible Playbooks

# Task-02

- Write a blog about writing ansible playbooks with the best practices.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/ca506e26-b615-4a66-b59f-00e2a91d9d5b)

Happy Learning :)

# Day 58 task is complete!
