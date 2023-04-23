# Day 19 Task: Docker for DevOps Engineers

# Docker-Volume

Docker allows you to create something called volumes. Volumes are like separate storage areas that can be accessed by containers. They allow you to store data, like a database, outside the container, so it doesn't get deleted when the container is deleted. You can also mount from the same volume and create more containers having same data.

# Docker Network

Docker allows you to create virtual spaces called networks, where you can connect multiple containers (small packages that hold all the necessary files for a specific application to run) together. This way, the containers can communicate with each other and with the host machine (the computer on which the Docker is installed). When we run a container, it has its own storage space that is only accessible by that specific container. If we want to share that storage space with other containers, we can't do that.

## Task-1

- Create a multi-container docker-compose file which will bring UP and bring DOWN containers in a single shot ( Example - Create application and database container )

hints:

- Use the docker-compose up command with the -d flag to start a multi-container application in detached mode.

- Use the docker-compose scale command to increase or decrease the number of replicas for a specific service. You can also add replicas in deployment file for auto-scaling.

- Use the docker-compose ps command to view the status of all containers, and docker-compose logs to view the logs of a specific service.

- Use the docker-compose down command to stop and remove all containers, networks, and volumes associated with the application

# Lets Start with my Mini-Project using docker-compose.yml file.

This is a simple voting app developed using Python, Flask, and MySQL. It allows users to vote for their favorite scripting language and displays the vote count for each language in real-time. The app is built and deployed using Docker-Compose.

Get source code for this task $ git clone https://github.com/Chaitannyaa/Simple_Docker-Compose-Project.git

![image](https://user-images.githubusercontent.com/117350787/233855681-187461ea-fff7-4845-bb02-48f8daa4a8c9.png)

![image](https://user-images.githubusercontent.com/117350787/233855758-75b9b26f-6979-4dec-8d6f-913cd4689a02.png)

![image](https://user-images.githubusercontent.com/117350787/233855813-23ae0e3c-f5fd-440c-89f9-c5a95200d73e.png)

![image](https://user-images.githubusercontent.com/117350787/233855974-ee6fbf27-7dea-4e9e-835e-ace30eb6d509.png)

![image](https://user-images.githubusercontent.com/117350787/233856025-d6bacef2-ade7-4cbc-b6b8-ec914ffcbb67.png)

## Task-2

# - Learn how to use Docker Volumes and Named Volumes to share files and directories between multiple containers.

Let's take the example of "Django-todo-notes-app" $ git clone https://github.com/Chaitannyaa/django-todo-cicd.git

![image](https://user-images.githubusercontent.com/117350787/233859929-0d32bfb2-66fb-4ae5-b932-0e1712c8e850.png)

In a typical Django application (which seems to be the case based on the presence of manage.py, db.sqlite3, and staticfiles), the database file in this case is  db.sqlite3 : would be the file that stores the appdata.

1. Let's create a directory with data-file "volume/store_data/db.sqlite3" in the same directory where docker-compose.yml is located.

![image](https://user-images.githubusercontent.com/117350787/233860026-b71132e2-a176-4758-b4e1-8850b8a3e8be.png)

2. Add this "volume" in ".dockerignore" and add volume mapping inside "docker-compose.yml" file.

![image](https://user-images.githubusercontent.com/117350787/233860056-022fd3b4-a72d-4d32-8829-299f00546a3f.png)

3. Run "docker-compose up" and add some data to app. Then delete the container and again spin new container with our local volume mapping to confirm data persistency.

![image](https://user-images.githubusercontent.com/117350787/233860569-5597bdff-dac6-48a7-9bfa-165d55e3b9ec.png)

![image](https://user-images.githubusercontent.com/117350787/233860509-b72546ae-f92c-493e-99af-862b9db0524a.png)

![image](https://user-images.githubusercontent.com/117350787/233860677-b247481e-6a6a-4ae6-96ff-4cb318631bfa.png)

![image](https://user-images.githubusercontent.com/117350787/233860751-3048ee48-fdaf-4ca0-8dc0-c2c5434a8e84.png)

![image](https://user-images.githubusercontent.com/117350787/233860816-b5074851-1768-4fad-a865-79da2c80ed43.png)


# - Create two or more containers that read and write data to the same volume using the docker run --mount command.

![image](https://user-images.githubusercontent.com/117350787/233861451-2e28e88c-0329-4081-a7b3-080d80dc7168.png)

![image](https://user-images.githubusercontent.com/117350787/233861609-0eb7f180-01af-4c75-9dac-c5d88c2f721d.png)

![image](https://user-images.githubusercontent.com/117350787/233861702-708e25cf-8926-46c2-ba68-100ea2e0b908.png)

![image](https://user-images.githubusercontent.com/117350787/233861873-cca66d1d-d7c8-4a78-a1f0-620625e1189e.png)

# - Verify that the data is the same in all containers by using the docker exec command to run commands inside each container.

![image](https://user-images.githubusercontent.com/117350787/233862832-ee806f84-6cd2-4d63-9f3d-c8a0c9f49622.png)

![image](https://user-images.githubusercontent.com/117350787/233863273-f25a9ddd-ac53-4ca3-bd1a-a8bd6d8ff937.png)

![image](https://user-images.githubusercontent.com/117350787/233863576-46e69b72-8a4c-41b5-9bb7-07743437eaad.png)

# - Use the docker volume ls command to list all volumes and docker volume rm command to remove the volume when you're done.

![image](https://user-images.githubusercontent.com/117350787/233863753-72cb75e5-b29b-40dd-beb1-ec4d300f9b91.png)

## You can use this task as Project to add in your resume.

You can Post on LinkedIn and let us know what you have learned from this task by #90DaysOfDevOps Challange. Happy Learning :)

https://www.linkedin.com/posts/chaitannyaa-gaikwad-b16965115_day19-90daysofdevops-challenge-tws-activity-7056021929245179905--1Cs?utm_source=share&utm_medium=member_desktop

# Day 19 Task is completed!
