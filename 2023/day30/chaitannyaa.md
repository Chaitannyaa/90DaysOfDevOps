
## Day 30 Task: Kubernetes Architecture

<p  align="center"><img  align="center"  src="https://kubernetes.io/images/kubernetes-horizontal-color.png"  /></p>

## Kubernetes Overview

With the widespread adoption of [containers](https://cloud.google.com/containers) among organizations, Kubernetes, the container-centric management software, has become a standard to deploy and operate containerized applications and is one of the most important parts of DevOps. 

Originally developed at Google and released as open-source in 2014. Kubernetes builds on 15 years of running Google's containerized workloads and the valuable contributions from the open-source community. Inspired by Google’s internal cluster management system, [Borg](https://research.google.com/pubs/pub43438.html), 

## Tasks

### 1. What is Kubernetes? Write in your own words and why do we call it k8s?

- Kubernetes is an open-source container orchestration platform for automating the deployment, scaling, and managing our of containerized applications. 
It provides many features for managing our deployments amongst the remote servers that run containerized applications. Using it we can have a robust deployment structure over multiple envirinments.

- We call it k8s because "Kubernetes" is a long name and it has 8 letters between "K" and "s". Therefore, we use "k8s" to refer to it more easily.

### 2. What are the benefits of using k8s?

- Using kubernetes you can build a robust sytem for your application/service deployments
- Gives highavalability to our deployments as it supports multi-node deplyments.
- Auto-healing and scaling of pods makes it robust systen for deployment
- It is open source, free and supports multi-cloud options.
- It is flexible and portable as it supports different Container runtimes.
- We can scale apps horizontally and vertically also we can upgrade resourses

### 3. Explain the architecture of Kubernetes, refer to [this video](https://youtu.be/FqfoDUhzyDo)

- It has a unique architecture that consists of a master node and multiple worker nodes. The collection of two or more nodes forms a Kubernetes cluster.
- Master Node: The master node is also called as control plane which manages Kubernetes cluster. 
### The master node consists of:
- API Server: The API server is the major component which communicates with all other components and provides option to control cluster via Kubectl tool.
- Scheduler: The scheduler allocates containers on worker nodes based on resource availability and other things.
- Controller Manager: Watches over Kubernetes objects and other controllers and ensures that the desired state of the system is achieved and maintained.
- etcd: It is key-value store that stores the configuration data and state of the Kubernetes cluster.
### The worker node consists of:
Worker Nodes: The worker nodes are the nodes in the Kubernetes cluster that run the containerized applications.
- Kube Proxy: It contans network rules on your nodes and enables network connections to pods.
- Container Runtime: It helps to run and manage the containers on the worker node.
- Kubelet: It manages and ensures that the containers are running, healthy, and have the necessary resources.

### 4. What is Control Plane?

- Master node is also called as Control Plane. It is the set of components for managing the state of the Kubernetes cluster. 
- The Control Plane makes global decisions about scheduling, scaling, and maintaining the desired state of the system. 
- It gives us the Kubernetes API, which is used to interact with the cluster and manage containerized applications.

### 5. Write the difference between kubectl and kubelets.

- kubectl is a command-line tool that is used to interact with the Kubernetes API. It is used to create, update, delete, and view resources in the cluster.
- kubelet is a component that runs on each node in the cluster and is responsible for managing the state of containers on that node. It communicates with the Control Plane to receive instructions about which containers to run and how to manage their state.

### 6. Explain the role of the API server.

- The API Server is a component of the Kubernetes Control Plane that exposes the Kubernetes API. 
- It acts as the central control point for the Kubernetes cluster, receiving requests from us via kubectl and apply those requests on cluster. 
- The API Server is responsible for authentication, authorization, and validation of all requests to the cluster. 
- It maintains cluster's state in etcd, and provides view of that state to us.

Kubernetes architecture is important, so make sure you spend a day understanding it. [This video](https://youtu.be/FqfoDUhzyDo) will surely help you.

*Happy Learning :)*

# Day 30 task is completed!
