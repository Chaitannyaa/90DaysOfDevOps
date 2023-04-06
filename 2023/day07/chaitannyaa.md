# Day 7 Task: Understanding package manager and systemctl

## Tasks

## 1. You have to install docker and jenkins in your system from your terminal using package managers

![image](https://user-images.githubusercontent.com/117350787/230497225-d1d0a026-29e5-4da6-845d-bcd51d96fe65.png)

![image](https://user-images.githubusercontent.com/117350787/230497517-dae83ba9-1fd1-41ec-b29e-b2dc1d224417.png)

## 2. Write a small blog or article to install these tools using package managers on Ubuntu and CentOS

Just follow the commands given below and you get it installed on your machine.

## - Install Docker

$ sudo apt-get update

$ sudo apt-get install \
    ca-certificates \
    curl \
    gnupg

$ sudo mkdir -m 0755 -p /etc/apt/keyrings

$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

$ echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

$ sudo apt-get update

$ sudo apt-get upgrade

$ sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

$ sudo docker run hello-world

## - Install Jenkins

$ curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null

$ echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null

$ sudo apt update

$ sudo apt upgrade

$ sudo apt-get install jenkins

$ sudo apt update

$ sudo apt upgrade

$ sudo apt install openjdk-11-jre

$ java -version

## Tasks

## 1. check the status of docker service in your system (make sure you completed above tasks, else docker won't be installed)

$ systemctl status docker

![image](https://user-images.githubusercontent.com/117350787/230497757-9c95b6a0-f1c2-4ea7-bccc-9b40878c11a2.png)

$ systemctl start jenkins

$ systemctl status jenkins

![image](https://user-images.githubusercontent.com/117350787/230497966-a1b7f68d-806b-44a9-83c6-0b534ed4241c.png)

## 2. stop the service jenkins and post before and after screenshots

$ systemctl stop jenkins

$ systemctl status jenkins

![image](https://user-images.githubusercontent.com/117350787/230498382-fcce2688-ad40-4972-a51c-fdaf0159e498.png)

## 3. read about the commands systemctl vs service

Both systemctl and service are command-line utilities in Linux that are used to manage system services.

service is an older utility that is still used in some Linux distributions. It provides a simple interface for starting, stopping, and restarting system services. It works by calling scripts in the /etc/init.d directory that are responsible for managing the service.

systemctl, on the other hand, is a newer and more powerful utility that is used in modern Linux distributions that use the systemd init system. systemctl provides a more advanced interface for managing services, allowing you to control and monitor the state of services, and perform more fine-grained operations like enabling or disabling services at boot time, reloading configuration files, and more.

# Day07 task is completed!
