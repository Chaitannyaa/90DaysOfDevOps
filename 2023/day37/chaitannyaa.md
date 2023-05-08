# Task: Kubernetes Important Interview Questions.

## Questions

## What is Kubernetes and why it is important?

Kubernetes is a portable, open-source, cloud-native infrastructure tool initially designed by Google to manage their clusters. Being a container orchestration tool, it automates the scaling, deployment, and management of containerized applications. 

![image](https://user-images.githubusercontent.com/117350787/236747738-9e7b41d1-fb58-4083-8387-2b596696cba2.png)

## What is the difference between docker swarm and Kubernetes?

### Let's understand the difference considering features and methods:

### Installation and setup

Kubernetes is very customizable but complex to set up. Docker Swarm is easier to install and configure.

Kubernetes: Depending on the operating system, manual installation can differ for each OS. If you are using services from a cloud provider, installation is not required.

Docker Swarm: Docker instances are typically consistent across operating systems and thus fairly simple to set up.

### Load balancing

Docker Swarm offers automatic load balancing, while Kubernetes does not. However, it is easy to integrate load balancing through third-party tools in Kubernetes.

Kubernetes: Services are made discoverable through a single DNS name. Kubernetes accesses container applications through an IP address or HTTP route.

Swarm: Comes with internal load balancers.

### Monitoring

Kubernetes: Kubernetes has built-in monitoring along with third-party monitoring tools integration support.

Docker Swarm: In contrast, there are no in-built monitoring mechanisms in Docker Swarm. However, Docker Swarm supports monitoring through third-party applications.

### Scalability

Kubernetes: Provides scaling based on traffic. Horizontal autoscaling is built in. Scaling in Kubernetes involves creating new pods and scheduling them to nodes with available resources.

Docker Swarm: Offers autoscaling of instances quickly and on-demand. As Docker Swarm deploys containers quicker, it gives the orchestration tool faster reaction times that enable on-demand scaling.

## How does Kubernetes handle network communication between containers?

Kubernetes assigns a unique IP address to each pod running on a node, and containers within the pod share the same network namespace. Kubernetes uses networking plugins such as Flannel, Calico, and Weave Net to implement the network model and services to provide a stable network endpoint for pods. 

![image](https://user-images.githubusercontent.com/117350787/236747949-c77b5623-df42-428e-bf78-06f83ee19b26.png)

## How does Kubernetes handle the scaling of applications?

When you scale an application, you increase or decrease the number of replicas. Each replica of your application represents a Kubernetes Pod that encapsulates your application's container(s).

Kubernetes supports horizontal and vertical scaling of applications using mechanisms such as Horizontal Pod Autoscaling (HPA) and Vertical Pod Autoscaling (VPA), as well as manual scaling and cluster autoscaling. 

Kubernetes also provides readiness and liveness probes to detect changes in application health and respond accordingly.

## What is a Kubernetes Deployment and how does it differ from a ReplicaSet?

Deployment provides higher-level abstractions and additional features such as rolling updates, rollbacks, and versioning of the application. ReplicaSet is a lower-level abstraction that provides basic scaling mechanisms.

Deployment manages a set of replicas of a specific application and enables rolling updates and rollbacks. It is a higher-level abstraction than a ReplicaSet, which only ensures a specified number of replicas of a pod are running. A Deployment can manage multiple ReplicaSets and control their lifecycle, while a ReplicaSet only manages a single set of replicas.

## Can you explain the concept of rolling updates in Kubernetes?

Rolling updates is a feature of Kubernetes that allows you to update a Deployment or a ReplicaSet with new versions of your application without downtime or disruption to your users.

## How does Kubernetes handle network security and access control?

Kubernetes handles network security and access control through a combination of network policies, authentication mechanisms, and authorization mechanisms.

Network policies allow administrators to define rules that control traffic within the Kubernetes cluster. These policies can be used to enforce restrictions on communication between pods or between the cluster and external networks.

Authentication mechanisms, such as certificates, tokens, or OAuth, verify the identity of users or services before they are granted access to the cluster.

Authorization mechanisms determine what actions a user or service is allowed to perform within the cluster. Kubernetes supports a variety of authorization modes, including role-based access control (RBAC) and attribute-based access control (ABAC).

## Can you give an example of how Kubernetes can be used to deploy a highly available application?

To deploy a highly available application, an administrator can create a deployment object in Kubernetes that specifies the number of replicas of the application to be created. 

Kubernetes will automatically distribute these replicas across multiple nodes in the cluster, ensuring that the application is highly available in case of node failures.

A Deployment is an object that manages a set of pods and always keeps up the desired number of replicas. A critical piece of this is to have continuous health checking and service discovery that can detect when a pod is failed and reroute traffic to healthy pods.

Kubernetes can also automatically scale the number of replicas based on metrics such as CPU utilization or request rates. This allows the application to handle varying levels of traffic without manual intervention.

In addition, Kubernetes provides built-in load balancing mechanisms that can distribute incoming traffic across multiple replicas of the application, ensuring that the load is evenly distributed and that no single replica is overloaded.

## What is a namespace in Kubernetes? Which namespace any pod takes if we don't specify any namespace?

Namespace as a virtual cluster inside your Kubernetes cluster. You can have multiple namespaces inside a single Kubernetes cluster, and they are all logically isolated from each other. They can help you and your teams with organization, security, and even performance!

![image](https://user-images.githubusercontent.com/117350787/236748217-2e5478bb-4bfb-4b3f-bf0f-f20fc0cc9ec8.png)

The pod will be created in the default namespace if we don't specify any namespace.

## How does ingress help in Kubernetes? 

![image](https://user-images.githubusercontent.com/117350787/236748291-3ab6db52-2c44-458d-9300-26c4e85514c0.png)

Kubernetes Ingress is an API object that provides routing rules to manage external users' access to the services in a Kubernetes cluster, typically via HTTPS/HTTP. With Ingress, you can easily set up rules for routing traffic without creating a bunch of Load Balancers or exposing each service on the node.

## Explain different types of services in Kubernetes.

In Kubernetes, four main types of services are used to provide network connectivity to pods:

ClusterIP: This is the default service type and creates a virtual IP address inside the cluster that can be used to access the pods. ClusterIP services are only accessible from within the cluster.

NodePort: This type of service exposes the pods on a static port on each node in the cluster. NodePort services can be accessed from outside the cluster using the IP address of any node in the cluster and the static port number.

LoadBalancer: This type of service creates an external load balancer that can distribute traffic to the pods. LoadBalancer services can be used to expose services to the internet or other external networks.

ExternalName: This type of service maps a service to an external DNS name, allowing pods to access services running outside of the cluster.

## Can you explain the concept of self-healing in Kubernetes and give examples of how it works?

Self-healing is a key concept in Kubernetes that refers to the ability of the platform to automatically detect and recover from failures of its components, including pods, nodes, and other resources. This helps to ensure the high availability and reliability of applications running on Kubernetes.

Here are some examples of how self-healing works in Kubernetes:

Pod auto-restart: If a pod crashes or becomes unresponsive, Kubernetes automatically restarts the pod. This is done using the restartPolicy property in the pod definition file, which can be set to either "Always", "OnFailure", or "Never".

Node auto-replacement: If a node becomes unhealthy or unresponsive, Kubernetes will automatically mark the node as "NotReady" and schedule the pods running on the node to other available nodes. If the node remains unhealthy for a certain period of time, Kubernetes will automatically replace the node with a new one.

Horizontal Pod Autoscaling (HPA): HPA allows Kubernetes to automatically scale the number of replicas of a pod based on resource usage or custom metrics. For example, if a pod is experiencing high CPU usage, Kubernetes can automatically increase the number of replicas to handle the increased load.

Rolling updates: When updating a deployment or a statefulset, Kubernetes performs a rolling update by gradually replacing the old pods with new ones. This allows the application to continue running with minimal downtime.

Overall, the self-healing capabilities of Kubernetes help to ensure that applications running on the platform are highly available, scalable, and resilient to failures.

## How does Kubernetes handle storage management for containers?

In Kubernetes, the most basic type of storage is non-persistent—also known as ephemeral. Each container has ephemeral storage by default—this storage uses a temporary directory on the machine that hosts the Kubernetes pod. It is portable, but not durable. Kubernetes supports multiple types of persistent storage.

![image](https://user-images.githubusercontent.com/117350787/236748473-a4778c30-9851-4c7f-884a-bccc2a18dd9d.png)

Volumes: Volumes are the simplest and most commonly used way to provide storage to containers in Kubernetes. Volumes are created as part of the pod definition and can be backed by local storage, network storage, or cloud storage.

Persistent Volumes (PVs): PVs are a way to provide persistent storage to pods. A PV is a piece of network-attached storage (NAS) or a physical disk that is mounted to a node and can be accessed by pods running on the node.

Persistent Volume Claims (PVCs): A PVC is a request for a specific amount of storage from a PV. When a PVC is created, Kubernetes looks for a PV that matches the requested size, access mode, and storage class.

## How does the NodePort service work?

In Kubernetes, a NodePort service is a type of service that exposes a pod to the outside world on a static port on each node in the cluster. Here's how it works:

![image](https://user-images.githubusercontent.com/117350787/236748532-7e15e364-14a5-4e7d-ab7b-9d0779cd6ae1.png)

When a NodePort service is created, Kubernetes allocates a port in the range of 30000-32767 on each node in the cluster.

The NodePort service is mapped to a specific port on the pod(s) that it is targeting. This can be either a static port or a dynamically allocated port.

When traffic is sent to the NodePort service from outside the cluster, the traffic is routed to the NodePort on any node in the cluster.

The node then forwards the traffic to the pod(s) that the NodePort service is targeting, using the port mapping specified in the service definition.

## What is a multinode cluster and a single-node cluster in Kubernetes?

![image](https://user-images.githubusercontent.com/117350787/236748614-b7b47494-4c13-4878-a153-f81f1c8aabde.png)

A single-node cluster is a Kubernetes cluster consisting of one node, while a multinode cluster consists of multiple nodes. 

![image](https://user-images.githubusercontent.com/117350787/236748642-fe65310f-c776-42f8-a263-a5a7346e7aa8.png)

Single-node clusters are often used for development and testing, while multi-node clusters are used in production environments for high availability, scalability, and fault tolerance.

## Difference between create and apply in kubernetes?

"apply" can be used to update existing resources, while "create" can only be used to create new resources. 

Additionally, "apply" supports a more fine-grained approach to updates, as it only applies changes that are specified in the YAML file, leaving other aspects of the resource unchanged.

## These questions will help you in your next DevOps Interview.

Happy Learning :)

# Day 37 task is completed!

