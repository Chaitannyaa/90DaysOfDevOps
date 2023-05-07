# Day 35: Mastering ConfigMaps and Secrets in Kubernetes🔒🔑🛡️

###  👏🎉 Yay! Yesterday we conquered Namespaces and Services 💪💻🔗🚀

## What are ConfigMaps and Secrets in k8s
In Kubernetes, ConfigMaps and Secrets are used to store configuration data and secrets, respectively. ConfigMaps store configuration data as key-value pairs, while Secrets store sensitive data in an encrypted form.

- *Example :- Imagine you're in charge of a big spaceship (Kubernetes cluster) with lots of different parts (containers) that need information to function properly.
ConfigMaps are like a file cabinet where you store all the information each part needs in simple, labeled folders (key-value pairs).
Secrets, on the other hand, are like a safe where you keep the important, sensitive information that shouldn't be accessible to just anyone (encrypted data).
So, using ConfigMaps and Secrets, you can ensure each part of your spaceship (Kubernetes cluster) has the information it needs to work properly and keep sensitive information secure! 🚀*
- Read more about [ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/) & [Secret](https://kubernetes.io/docs/concepts/configuration/secret/).
## Today's task:
## Task 1:
Create a ConfigMap for your Deployment

- Create a ConfigMap for your Deployment using a file or the command line

```sh
kind: ConfigMap
apiVersion: v1
metadata:
  name: mysql-config
  labels:
    app: todo
data:
  MYSQL_DB: "todo-db"
```

- Update the deployment.yml file to include the ConfigMap

```sh
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mysql
  labels:
    app: mysql
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mysql
  template:
    metadata:
      labels:
        app: mysql
    spec:
      containers:
      - name: mysql
        image: mysql:8
        ports:
        - containerPort: 3306
        env:
        - name: MYSQL_ROOT_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mysql-secret
              key: password
        - name: MYSQL_DATABASE
          valueFrom:
            configMapKeyRef:
              name: mysql-config
              key: MYSQL_DB
```

- Apply the updated deployment using the command: `kubectl apply -f deployment.yml -n <namespace-name>`

![image](https://user-images.githubusercontent.com/117350787/236670749-66e4045a-af9d-415c-9c77-5233a4de6ac2.png)

- Verify that the ConfigMap has been created by checking the status of the ConfigMaps in your Namespace.

![image](https://user-images.githubusercontent.com/117350787/236670778-6b26be64-60b0-43b9-a273-dfaafa4478b3.png)

## Task 2:
Create a Secret for your Deployment

- Create a Secret for your Deployment using a file or the command line
- Update the deployment.yml file to include the Secret
- Apply the updated deployment using the command: `kubectl apply -f deployment.yml -n <namespace-name>`
- Verify that the Secret has been created by checking the status of the Secrets in your Namespace.

Need help with ConfigMaps and Secrets? Check out this [video](https://youtu.be/FAnQTgr04mU) for assistance.
  
Keep learning and expanding your knowledge of Kubernetes💥🙌
