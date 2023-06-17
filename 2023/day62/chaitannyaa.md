# Day 62 - Terraform and Docker 🔥

Terraform needs to be told which provider to be used in the automation, hence we need to give the provider name with source and version.
For Docker, we can use this block of code in your main.tf

## Blocks and Resources in Terraform 

## Create a Terraform block with provider docker 

```sh
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.21.0"
}
}
}
```
### Note: kreuzwerker/docker, is shorthand for registry.terraform.io/kreuzwerker/docker.

## Provider Block
The provider block configures the specified provider, in this case, docker. A provider is a plugin that Terraform uses to create and manage your resources.

```sh
provider "docker" {
  host = "unix:///var/run/docker.sock"
}
```
**provider "docker"** indicates that we are configuring the Docker provider. This tells Terraform to use the Docker provider to manage Docker resources.

**host = "unix:///var/run/docker.sock"** is a configuration option for the Docker provider. It specifies the address of the Docker daemon's Unix socket.

- The unix:///var/run/docker.sock value is the default socket path for Docker daemon running on Unix-based systems. The Docker daemon listens for API requests on this Unix socket.

- The Docker socket is a special file that provides a way to interact with the Docker daemon locally. By specifying this path, Terraform can communicate with the Docker daemon on the same machine where Terraform is executed.

## Resource Block
Use resource blocks to define components of your infrastructure. A resource might be a physical or virtual component such as a Docker container, or it can be a logical resource such as a Heroku application.

Resource blocks have two strings before the block: the resource type and the resource name. 

In this example, the first resource type is docker_image and the name is Nginx.

```sh
resource "docker_image" "nginx" {
  #Configuration data
}
```

## Create a resource Block for an nginx docker image

```sh
resource "docker_image" "nginx" {
 name         = "nginx:latest"
 keep_locally = false
}
```

## Create a resource Block for running a docker container for nginx

```sh
resource "docker_container" "nginx" {
 image = docker_image.nginx.image_id
 name  = "tutorial"
 ports {
   internal = 80
   external = 80
 }
}
```
![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/6f647147-75c7-4a8f-b07e-eb616fc7b6cb)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/ff8c1913-78af-471a-84a3-e498b2b3a8bd)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/93790fbe-2b2e-4e9b-80d7-f6f81c78d50e)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/730e6eae-4263-4b34-8d9e-a146fc2acb60)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/24d75202-79f2-49a6-81e9-808e45092600)

**Note: In case Docker is not installed**

`sudo apt-get install docker.io`
`sudo usermod -aG $USER`
`sudo reboot`
`sudo docker ps`

Happy Learning :)

# Day62 task is complete!
