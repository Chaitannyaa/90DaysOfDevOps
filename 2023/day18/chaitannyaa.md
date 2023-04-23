#  Day 18 Task: Docker for DevOps Engineers

## Docker Compose

Docker Compose is a tool that was developed to help define and share multi-container applications.
With Compose, we can create a YAML file to define the services and with a single command, can spin everything up or tear it all down.
Learn more about docker-compose visit here

## What is YAML?
YAML is a data serialization language that is often used for writing configuration files. Depending on whom you ask, YAML stands for yet another markup language or YAML ain’t markup language (a recursive acronym), which emphasizes that YAML is for data, not documents.
YAML is a popular programming language because it is human-readable and easy to understand.
YAML files use a .yml or .yaml extension.

# Task-1

## Learn how to use the docker-compose.yml file, to set up the environment, configure the services and links between different containers, and also to use environment variables in the docker-compose.yml file.

1. Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration.

2. Setting Up the Environment
Before we start defining our services, we need to set up our environment. Create a new directory for your project and navigate to it in your terminal. Then, create a new file called docker-compose.yml in this directory.

3. Configuring Services
We will define our services. Each service is defined as a separate block in the docker-compose.yml file. Here is an example of how to define a service:

## docker-compose.yml

![image](https://user-images.githubusercontent.com/117350787/233853322-7f464bc4-1e9f-4285-8135-443cde110fa5.png)

4. Configuring links

## docker-compose.yml

![image](https://user-images.githubusercontent.com/117350787/233853369-7d72e8cc-9df1-4308-a637-c1d0b4ede267.png)

5. environment variables

![image](https://user-images.githubusercontent.com/117350787/233853420-aa8d1322-5df2-4fda-b4a4-9cceb6740257.png)

# Task-2

- Pull a pre-existing Docker image from a public repository (e.g. Docker Hub) and run it on your local machine. Run the container as a non-root user (Hint- Use usermod  command to give user permission to docker). Make sure you reboot instance after giving permission to user.

![image](https://user-images.githubusercontent.com/117350787/233852094-96e8a049-1525-4372-a67b-7081f08ef0a3.png)

![image](https://user-images.githubusercontent.com/117350787/233852138-083ee01e-214a-4691-a676-b12ebcf2c423.png)

- Inspect the container's running processes and exposed ports using the docker inspect command.

![image](https://user-images.githubusercontent.com/117350787/233852465-6fa896ab-951b-4ba3-8ecf-aa58ca47bd30.png)

![image](https://user-images.githubusercontent.com/117350787/233852433-761711a5-4946-49ae-aefa-7dd9845b7483.png)

- Use the docker logs command to view the container's log output.

![image](https://user-images.githubusercontent.com/117350787/233852534-5a924808-ad8e-46c7-8222-04946fb3a290.png)

- Use the docker stop and docker start commands to stop and start the container.

![image](https://user-images.githubusercontent.com/117350787/233852607-2b80aa43-0f2f-4960-8bd0-4ff1c6c3c814.png)

- Use the docker rm command to remove the container when you're done.

![image](https://user-images.githubusercontent.com/117350787/233852678-f81dee60-9535-4070-a4c8-90222af19bdc.png)

# How to run Docker commands without sudo?

- Make sure docker is installed and system is updated (This is already been completed as a part of previous tasks):

$ docker --version

$ sudo usermod -a -G docker $USER

$ sudo reboot

# Day18 task is completed!
