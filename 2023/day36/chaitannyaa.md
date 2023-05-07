# Day 36 Task: Managing Persistent Volumes in Your Deployment 💥

## What are Persistent Volumes in k8s

In Kubernetes, a Persistent Volume (PV) is a piece of storage in the cluster that has been provisioned by an administrator. A Persistent Volume Claim (PVC) is a request for storage by a user. The PVC references the PV, and the PV is bound to a specific node. Read official documentation of [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/). 

## Today's tasks:

### Task 1:

Add a Persistent Volume to your Deployment todo app.

- Create a Persistent Volume using a file on your node. [Template](https://github.com/LondheShubham153/90DaysOfDevOps/blob/94e3970819e097a5b8edea40fe565d583419f912/2023/day36/pv.yml)

![image](https://user-images.githubusercontent.com/117350787/236672575-5476b6a6-02dd-48c3-8d65-720c6516f06e.png)

- Create a Persistent Volume Claim that references the Persistent Volume. [Template](https://github.com/LondheShubham153/90DaysOfDevOps/blob/94e3970819e097a5b8edea40fe565d583419f912/2023/day36/pvc.yml)

![image](https://user-images.githubusercontent.com/117350787/236672590-f7544933-3912-4526-af76-6371e99b6cc5.png)

- Update your deployment.yml file to include the Persistent Volume Claim. After Applying pv.yml pvc.yml your deployment file look like this [Template](https://github.com/LondheShubham153/90DaysOfDevOps/blob/94e3970819e097a5b8edea40fe565d583419f912/2023/day36/Deployment.yml)

![image](https://user-images.githubusercontent.com/117350787/236672639-c377eff7-c3ec-4dc2-b61a-da5906e122f0.png)

- Apply the updated deployment using the command: `kubectl apply -f deployment.yml`

![image](https://user-images.githubusercontent.com/117350787/236672682-53f75846-f93e-4aaf-8d57-15b0857d49fa.png)

- Verify that the Persistent Volume has been added to your Deployment by checking the status of the Pods and Persistent Volumes in your cluster. 
  Use this commands `kubectl get pods` , `kubectl get pv`

![image](https://user-images.githubusercontent.com/117350787/236673070-8d3c0b06-5a2a-43b7-b6d0-b8f60607ec55.png)

⚠️ Don't forget: To apply changes or create files in your Kubernetes deployments, each file must be applied separately. ⚠️

### Task 2:
Accessing data in the Persistent Volume

- Connect to a Pod in your Deployment using command : `kubectl exec -it <pod-name> -- /bin/bash`

![image](https://user-images.githubusercontent.com/117350787/236676008-49b4867c-7239-4091-b15a-05cbddf894ad.png)

- Verify that you can access the data stored in the Persistent Volume from within the Pod

![image](https://user-images.githubusercontent.com/117350787/236675971-3e6f0be8-cfb5-45c2-af63-16af20ddc769.png)


Need help with Persistent Volumes? Check out this [video](https://youtu.be/U0_N3v7vJys) for assistance.

Keep up the excellent work🙌💥

Happy Learning :)

# Day36 task is completed!

