
## Day 32 Task: Launching your Kubernetes Cluster with Deployment

### Congratulation ! on your learning on K8s on Day-31

## What is Deployment in k8s

A Deployment provides a configuration for updates for Pods and ReplicaSets.

You describe a desired state in a Deployment, and the Deployment Controller changes the actual state to the desired state at a controlled rate. You can define Deployments to create new replicas for scaling, or to remove existing Deployments and adopt all their resources with new Deployments.

## Today's task let's keep it very simple.

## Task-1: 
**Create one Deployment file to deploy a sample todo-app on K8s using "Auto-healing" and "Auto-Scaling" feature**

- add a deployment.yml file (sample is kept in the folder for your reference)

![image](https://user-images.githubusercontent.com/117350787/236458338-a5a11ff9-e0ed-4322-8532-312061c54747.png)

- apply the deployment to your k8s (minikube) cluster by command
`kubectl apply -f deployment.yml`

![image](https://user-images.githubusercontent.com/117350787/236458694-b7159cac-a8aa-46c8-a389-8954868fba5f.png)

![image](https://user-images.githubusercontent.com/117350787/236459783-7fa015fa-ac29-4a73-a441-0ed18a127b45.png)

![image](https://user-images.githubusercontent.com/117350787/236459068-deaff04e-9403-41fc-a081-b7d1af2711b4.png)

**Having an issue? Don't worry, adding a sample deployment file , you can always refer that or wathch [this video](https://youtu.be/ONrbWFJXLLk)**

Happy Learning :)

# Day 32 task is completed!
