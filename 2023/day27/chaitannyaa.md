
# Day 27 Task: Jenkins Declarative Pipeline with Docker

  

Day 26 was all about a Declarative pipeline, now its time to level up things, let's integrate Docker and your Jenkins declarative pipeline

  

## Use your Docker Build and Run Knowledge

  

**docker build  -** you can use `sh 'docker build . -t <tag>' ` in your pipeline stage block to run the docker build command. (Make sure you have docker installed with correct permissions.

  

**docker run:** you can use `sh 'docker run -d  <image>'` in your pipeline stage block to build the container.

  

**How will the stages look** 
````groovy
stages {
        stage('Build') {
            steps {
                sh 'docker build -t trainwithshubham/django-app:latest'
            }
        }
    }
````

# Task-01

  

- Create a docker-integrated Jenkins declarative pipeline 

![image](https://user-images.githubusercontent.com/117350787/235583448-bc1e3eb8-9a85-4e6f-9cdd-47098f4006eb.png)

![image](https://user-images.githubusercontent.com/117350787/235583555-9e06f7dd-9083-44f9-8c76-df842e75ba48.png)

![image](https://user-images.githubusercontent.com/117350787/235584545-6a475034-00d4-4e95-bdea-4b43f7cfb038.png)

- Use the above-given syntax using `sh` inside the stage block

````groovy
pipeline {
    agent any
    environment {
        DOCKER_IMAGE_TAG = "${BUILD_NUMBER}"
    }
    stages {
        stage ("code"){
            steps {
                git url: 'https://github.com/Chaitannyaa/django-todo-cicd.git', branch: 'develop'
            }
        }
        stage ("Build"){
            steps {
                sh 'docker build -t chaitannyaa/django-todo-app:v-${DOCKER_IMAGE_TAG} .'
            }
        }
        stage ("login and push image"){
            steps {
                echo 'Logging into docker and pushing an image on dockerhub'
                withCredentials([usernamePassword(credentialsId: 'DockerHub', passwordVariable: 'password', usernameVariable: 'user')]) {
                    sh "docker login -u ${env.user} -p ${env.password}"
                    sh "docker push chaitannyaa/django-todo-app:v-${DOCKER_IMAGE_TAG}"
                }
            }
        }
        stage ("Deploy"){
            steps {
                sh 'docker-compose down && docker-compose up -d'
            }
        }
    }
}
````

- You will face errors in case of running a job twice, as the docker container will be already created, so for that do task 2

# Task-02

- Create a docker-integrated Jenkins declarative pipeline using the `docker` groovy syntax inside the stage block.

![image](https://user-images.githubusercontent.com/117350787/235585558-f5971550-e02b-4f21-b63b-6d89f1f10583.png)

![image](https://user-images.githubusercontent.com/117350787/235586238-ffeefcfc-8036-44e3-aef6-bf41becefd72.png)

````groovy
pipeline {
    agent any
    environment {
        DOCKER_IMAGE_TAG = "${BUILD_NUMBER}"
    }
    stages {
        stage("code"){
            steps {
                git url: 'https://github.com/Chaitannyaa/django-todo-cicd.git', branch: 'develop'
            }
        }
        stage("Build and push image"){
            steps {
                script {
                    def dockerImage = docker.build("chaitannyaa/django-todo-app:v-${DOCKER_IMAGE_TAG}", "--build-arg BUILD_NUMBER=${DOCKER_IMAGE_TAG} .")
                    withCredentials([usernamePassword(credentialsId: 'DockerHub', passwordVariable: 'password', usernameVariable: 'user')]) {
                        docker.withRegistry("https://registry.hub.docker.com", "DockerHub") {
                            dockerImage.push()
                        }
                    }
                }
            }
        }
        stage("Deploy"){
            steps {
                sh '''
                    if [[ -f /home/ubuntu/db.sqlite3 ]]; then
                        echo "Perfect"
                        echo '1180' | sudo -S rm -f /var/lib/jenkins/workspace/Django-app-CICD-Pipeline/db.sqlite3
                        echo '1180' | sudo -S cp -r /home/ubuntu/db.sqlite3 /var/lib/jenkins/workspace/Django-app-CICD-Pipeline/ 
                    else
                        echo '1180' | sudo -S cp -r /var/lib/jenkins/workspace/Django-app-CICD-Pipeline/db.sqlite3 /home/ubuntu/db.sqlite3
                    fi
                    docker-compose down && docker-compose up -d
                '''
            }
        }
    }
}
````

- You won't face errors, you can Follow [this documentation](https://tempora-mutantur.github.io/jenkins.io/github_pages_test/doc/book/pipeline/docker/)

![image](https://user-images.githubusercontent.com/117350787/235617788-44b8e2df-dcd3-45dc-86eb-c4cdd46fe170.png)

- Complete your previous projects using this Declarative pipeline approach

![image](https://user-images.githubusercontent.com/117350787/235618827-fc980577-1edc-49db-b12c-6c433f18e07d.png)

![image](https://user-images.githubusercontent.com/117350787/235617934-8df4454a-2b0a-4c0c-8b2e-03384bf3d495.png)

- In case of any issues feel free to post on any Groups, [Discord](https://discord.gg/Q6ntmMtH) or [Telegram](https://t.me/trainwithshubham)

Happy Learning:)

# Day27 task is completed!
