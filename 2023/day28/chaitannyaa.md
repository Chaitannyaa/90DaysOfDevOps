# Day 28 Task: Jenkins Agents

# Jenkins Master (Server)
Jenkins’s server or master node holds all key configurations. Jenkins master server is like a control server that orchestrates all the workflow defined in the pipelines. For example, scheduling a job, monitoring the jobs, etc.

# Jenkins Agent
An agent is typically a machine or container that connects to a Jenkins master and this agent that actually execute all the steps mentioned in a Job. When you create a Jenkins job, you have to assign an agent to it. Every agent has a label as a unique identifier.

When you trigger a Jenkins job from the master, the actual execution happens on the agent node that is configured in the job.

A single, monolithic Jenkins installation can work great for a small team with a relatively small number of projects. As your needs grow, however, it often becomes necessary to scale up. Jenkins provides a way to do this called “master to agent connection.” Instead of serving the Jenkins UI and running build jobs all on a single system, you can provide Jenkins with agents to handle the execution of jobs while the master serves the Jenkins UI and acts as a control node.

 <p align="center"><img align="center" src="https://user-images.githubusercontent.com/115981550/215276859-fa140ab7-e905-41c9-8ae2-1eef577c5e72.png" /></p>

## Pre-requisites
Let’s say we’re starting with a fresh Ubuntu 22.04 Linux installation. To get an agent working make sure you install Java ( same version as jenkins master server ) and Docker on it.

![image](https://user-images.githubusercontent.com/117350787/235694721-d3d7973b-208e-49b8-b028-ac9c0e393864.png)

`
Note:-
While creating an agent, be sure to separate rights, permissions, and ownership for jenkins users. 
`
![image](https://user-images.githubusercontent.com/117350787/235695063-34aa1dc6-f8cb-4488-914f-d671e66a952f.png)

![image](https://user-images.githubusercontent.com/117350787/235695200-1b1fa56a-e09a-4f52-9135-a471d521e2b5.png)

![image](https://user-images.githubusercontent.com/117350787/235695367-ef2bc4f8-e5dc-48ac-8738-b6b0377b7817.png)

![image](https://user-images.githubusercontent.com/117350787/235696109-05a3200c-abb1-4066-9eab-2492b10f2c23.png)

![image](https://user-images.githubusercontent.com/117350787/235696432-bd680cb4-8407-49c4-9e8b-464ce3d46b30.png)

# Task-01

- Create an agent by setting up a node on Jenkins

![image](https://user-images.githubusercontent.com/117350787/235697668-a4c1c93c-ec62-4c4e-b8b1-bee274cd01d2.png)

![image](https://user-images.githubusercontent.com/117350787/235698543-78f23b2c-dc1f-475a-8b03-3c14540bcfa2.png)

- Create a new AWS EC2 Instance and connect it to master(Where Jenkins is installed)

![image](https://user-images.githubusercontent.com/117350787/235712279-7baca1f3-ba44-41ef-a014-fbc1930cba17.png)

![image](https://user-images.githubusercontent.com/117350787/235712597-983298f5-b68c-421c-b6d0-f655d599d26c.png)

- The connection of master and agent requires SSH and the public-private key pair exchange.

![image](https://user-images.githubusercontent.com/117350787/235700905-d3484b17-4339-4efe-ab6c-9c061490da03.png)

- Verify its status under "Nodes" section.

![image](https://user-images.githubusercontent.com/117350787/235710785-41acee0f-c6de-46fe-bef3-084258755586.png)

- You can follow [this article](https://www.linkedin.com/posts/chetanrakhra_devops-project-share-activity-7017885886461698048-os5f?utm_source=share&utm_medium=member_android) for the same

# Task-02

- Run your CI/CD pipeline (which you built on Day 26, and Day 27) on the new agent

![image](https://user-images.githubusercontent.com/117350787/235718949-7813d506-41da-4d2f-95d8-511b6472cb9f.png)

![image](https://user-images.githubusercontent.com/117350787/235718360-59f9137d-d724-43f5-aa84-5e7cb57da8d6.png)

- Use labels for the agent, your master server should trigger builds for the agent server.

![image](https://user-images.githubusercontent.com/117350787/235735251-7134172b-89cd-400b-8ad4-c72bccb98363.png)

![image](https://user-images.githubusercontent.com/117350787/235735370-30c70612-e2f0-4556-bc92-76877c3e0f9c.png)

![image](https://user-images.githubusercontent.com/117350787/235735642-d694ff46-0093-43b4-8b20-a8692aabdba5.png)

![image](https://user-images.githubusercontent.com/117350787/235735740-86c811ba-5724-430e-83c8-374ac8d49b24.png)

- In case of any issues feel free to post on any Groups, [Discord](https://discord.gg/Q6ntmMtH) or [Telegram](https://t.me/trainwithshubham)

![image](https://user-images.githubusercontent.com/117350787/235745160-c0740c31-42a0-4a7c-a5b4-502cb8d9917e.png)
 
![image](https://user-images.githubusercontent.com/117350787/235747177-52a346c3-73c0-4f6c-9192-745896048896.png)

Are you enjoying the #90DaysOfDevOps Challenge?

[linkedin post >>](https://www.linkedin.com/posts/chaitannyaa-gaikwad-b16965115_day28-90daysofdevops-challenge-tws-activity-7059243852917817344-xDi0?utm_source=share&utm_medium=member_desktop)

Happy Learning:)

# Day 28 task is completed!
