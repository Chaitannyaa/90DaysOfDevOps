# Day 56: Understanding Ad-hoc commands in Ansible

Ansible ad hoc commands are one-liners designed to achieve a very specific task they are like quick snippets and your compact swiss army knife when you want to do a quick task across multiple machines.

To put simply, Ansible ad hoc commands are one-liner Linux shell commands and playbooks are like a shell script, a collective of many commands with logic.

Ansible ad hoc commands come handy when you want to perform a quick task.

# Task-01

- Write an ansible ad hoc ping command to ping 2 servers from inventory file

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/03f6fdca-daf9-4909-be7f-1674d2fe34d3)

![1212121212](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/fff4d1b5-ae3e-4431-836b-03dd51cc1bb7)

#### Let me show you my inventory file first--->

`sudo cat /etc/ansible/hosts`

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/88cd2924-ac89-481c-b13e-3f31c7277416)

#### Ansible ad hoc ping command--->
`ansible servers -m ping` 

Note: `servers` is the group of hosts defined in my inventory file

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/c0a0b967-5acb-42a7-99af-a075357069a9)

- Write an ansible ad hoc command to check uptime

`ansible servers -a uptime`

Note: `servers` is the group of hosts defined in my inventory file

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/303db109-f3f2-44cf-95e2-10db01efb0fd)

- Refer to [this](https://www.middlewareinventory.com/blog/ansible-ad-hoc-commands/) blog to understand the different examples of ad-hoc commands and try out them.

#### Check free memory space using AD-HOC command

`ansible servers -a "free -h"`

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/c7bcdde4-f042-4b91-b2f9-e8c311c03103)

#### Check free disk space using AD-HOC command

`ansible servers -a "df -h"`

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/64250832-6783-4e1d-8a70-bece085ff8b1)

#### Update all node's system using AD-HOC command

`ansible servers -a "sudo apt update"`

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/3d22b8ca-93f0-489f-89f1-e25374a167fe)

## I hope you learned the use of Ansible Ad-Hoc commands

Happy Learning :)

# Day 56 task is complete!
