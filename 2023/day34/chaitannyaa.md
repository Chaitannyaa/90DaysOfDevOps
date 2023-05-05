# Day 34 Task: Working with Services in Kubernetes
### Congratulation🎊  on your learning on Deployments in K8s on Day-33
## What are Services in K8s
In Kubernetes, Services are objects that provide stable network identities to Pods and abstract away the details of Pod IP addresses. Services allow Pods to receive traffic from other Pods, Services, and external clients.


## Task-1:
Create a Service for your app Deployment to make it accessible from outside the cluster

- Create a Service definition for your todo-app Deployment in a YAML file.

![image](https://user-images.githubusercontent.com/117350787/236522024-b4bd7a52-6db1-43f1-8998-d503ef8dcd0c.png)

- Apply the Service definition to your K8s (minikube) cluster using the `kubectl apply -f service.yml -n <namespace-name>` command.

```sh
kubectl apply -f service.yml -n test-ns
```

![image](https://user-images.githubusercontent.com/117350787/236522831-7fc2c4fb-5396-43da-ba75-a02e0624e6b3.png)

- Verify that the Service is working by accessing the app using the Service's IP and Port in your Namespace.

![image](https://user-images.githubusercontent.com/117350787/236523136-e5623877-201b-434a-a6a4-3a5b59ff0f6f.png)

As our app is running on pod and pod is running on minikube and minikube is running on ec2 intsance. We have service for directing traffic from minikube node to container app. But minikube is itself running as a virtualization on ec2 instance via docker engine. Hence we need to forward traffic from ec2 to minikube node--->

```sh
kubectl port-forward --address 0.0.0.0 svc/my-webapp-service --namespace test-ns 30430:80
```

![image](https://user-images.githubusercontent.com/117350787/236524475-62589fdc-7bc9-4af9-82a1-8f713ddf3bd9.png)

## Task-2:
Create a ClusterIP Service for accessing the app from within the cluster

- Create a ClusterIP Service definition for your app Deployment in a YAML file.

![image](https://user-images.githubusercontent.com/117350787/236528215-4f981f53-8b3e-467d-b2a2-84ff8d5ce9c1.png)

- Apply the ClusterIP Service definition to your K8s (minikube) cluster using the `kubectl apply -f cluster-ip-service.yml -n <namespace-name>` command.

```sh
kubectl apply -f clusterIP-service.yml -n test-ns
```

![image](https://user-images.githubusercontent.com/117350787/236528516-e9bf464f-3924-4c18-afc5-d6a9ffb14346.png)

- Verify that the ClusterIP Service is working by accessing the todo-app from another Pod in the cluster in your Namespace.

```sh
kubectl port-forward --address 0.0.0.0 svc/my-webapp-service --namespace test-ns 8501:80
```

![image](https://user-images.githubusercontent.com/117350787/236529014-e4bbdfa3-e3d5-47e8-a96c-55384b288cde.png)

![image](https://user-images.githubusercontent.com/117350787/236529674-ae848a3c-dc25-41d2-bf83-8d8bb83571ae.png)

## Task-3:
Create a LoadBalancer Service for accessing the app from outside the cluster

- Create a LoadBalancer Service definition for your todo-app Deployment in a YAML file.

![image](https://user-images.githubusercontent.com/117350787/236533462-0512b2b2-031d-49e0-8792-0faf55076317.png)

- Apply the LoadBalancer Service definition to your K8s (minikube) cluster using the `kubectl apply -f load-balancer-service.yml -n <namespace-name>` command.

```sh
kubectl apply -f loadbalancer-service.yml -n test-ns
```

![image](https://user-images.githubusercontent.com/117350787/236533774-8fc4c54b-4272-4764-8606-8ea7173205ce.png)

- Verify that the LoadBalancer Service is working by accessing the app from outside the cluster in your Namespace.

```sh
kubectl port-forward --address 0.0.0.0 svc/my-webapp-service --namespace test-ns 30430:80
```

![image](https://user-images.githubusercontent.com/117350787/236534387-ee136531-c476-48e2-bff7-038f9540e49e.png)

![image](https://user-images.githubusercontent.com/117350787/236534846-d7f9829e-7a12-47b6-ae76-4bbb4e3b8b8d.png)

## Struggling with Services? Take a look at this video for a step-by-step [guide](https://youtu.be/OJths_RojFA).

## Need help with Services in Kubernetes? Check out the Kubernetes [documentation](https://kubernetes.io/docs/concepts/services-networking/service/) for assistance.

Happy Learning :)

# Day 34 task is completed!

