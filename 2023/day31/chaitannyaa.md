
## Day 31 Task: Launching your First Kubernetes Cluster with Nginx running

### Awesome! You learned the architecture of one of the top most important tool "Kubernetes" in your previous task.

## What about doing some hands-on now?

Let's read about minikube and implement *k8s* in our local machine

1) **What is minikube?**

*Ans*:- Minikube is a tool which quickly sets up a local Kubernetes cluster on macOS, Linux, and Windows. It can deploy as a VM, a container, or on bare-metal.

Minikube is a pared-down version of Kubernetes that gives you all the benefits of Kubernetes with a lot less effort.

This makes it an interesting option for users who are new to containers, and also for projects in the world of edge computing and the Internet of Things.

2) **Features of minikube**

*Ans* :-

(a) Supports the latest Kubernetes release (+6 previous minor versions)

(b) Cross-platform (Linux, macOS, Windows)

(c) Deploy as a VM, a container, or on bare-metal

(d) Multiple container runtimes (CRI-O, containerd, docker)

(e) Direct API endpoint for blazing fast image load and build

(f) Advanced features such as LoadBalancer, filesystem mounts, FeatureGates, and network policy

(g) Addons for easily installed Kubernetes applications

(h) Supports common CI environments

## Task-01:

# Install minikube on your local
For installation, you can Visit [this page](https://minikube.sigs.k8s.io/docs/start/).

## 1. Install docker first

- sudo apt-get update
- sudo apt-get install docker.io
- sudo usermod -aG docker $USER
- sudo reboot

![image](https://user-images.githubusercontent.com/117350787/236454810-16a48e3a-c9ef-4540-a816-d236bde018b3.png)

## 2. Install Kubectl

- echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check
- sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
- kubectl version --client --output=yaml

![image](https://user-images.githubusercontent.com/117350787/236454931-c10571e5-12c2-47dd-87ca-261139d098c7.png)

## 3. Install minikube 

- curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb
- sudo dpkg -i minikube_latest_amd64.deb
- minikube start

![image](https://user-images.githubusercontent.com/117350787/236455414-c8013a11-0c20-42f5-958c-9cf65b9bab8e.png)

![image](https://user-images.githubusercontent.com/117350787/236455141-01cbd001-fe59-46c6-ae62-b743284d142e.png)

If you want to try an alternative way, you can check [this](https://k8s-docs.netlify.app/en/docs/tasks/tools/install-minikube/).

## Let's understand the concept **pod**

*Ans:-*

Pods are the smallest deployable units of computing that you can create and manage in Kubernetes.

A Pod (as in a pod of whales or pea pod) is a group of one or more containers, with shared storage and network resources, and a specification for how to run the containers. A Pod's contents are always co-located and co-scheduled, and run in a shared context. A Pod models an application-specific "logical host": it contains one or more application containers which are relatively tightly coupled.

You can read more about pod from [here](https://kubernetes.io/docs/concepts/workloads/pods/) .

## Task-02:

## Create your first pod on Kubernetes through minikube.

![image](https://user-images.githubusercontent.com/117350787/236456631-7f34df46-3449-4e53-930a-62356c5b8d7c.png)

![image](https://user-images.githubusercontent.com/117350787/236456710-1edbc395-cb1a-48b4-898c-5e05ed367471.png)

We are suggesting you make an nginx pod, but you can always show your creativity and do it on your own.

**Having an issue? Don't worry, adding a sample yaml file for pod creation, you can always refer that.**

*Happy Learning :)*

# Day31 task is completed!
