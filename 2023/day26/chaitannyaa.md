# Day 26 Task: Jenkins Declarative Pipeline

  
One of the most important parts of your DevOps and CICD journey is a Declarative Pipeline Syntax of Jenkins
  

## Some terms for your Knowledge

**What is Pipeline -** A pipeline is a collection of steps or jobs interlinked in a sequence.

**Declarative:** Declarative is a more recent and advanced implementation of a pipeline as a code.

**Scripted:** Scripted was the first and most traditional implementation of the pipeline as a code in Jenkins. It was designed as a general-purpose DSL (Domain Specific Language) built with Groovy.

# Why you should have a Pipeline

The definition of a Jenkins Pipeline is written into a text file (called a  [`Jenkinsfile`](https://www.jenkins.io/doc/book/pipeline/jenkinsfile)) which in turn can be committed to a project’s source control repository.  
This is the foundation of "Pipeline-as-code"; treating the CD pipeline as a part of the application to be versioned and reviewed like any other code.

**Creating a  `Jenkinsfile`  and committing it to source control provides a number of immediate benefits:**

-   Automatically creates a Pipeline build process for all branches and pull requests.
    
-   Code review/iteration on the Pipeline (along with the remaining source code).


# Pipeline syntax

````groovy
pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                // 
            }
        }
        stage('Test') { 
            steps {
                // 
            }
        }
        stage('Deploy') { 
            steps {
                // 
            }
        }
    }
}
````

  
# Task-01

- Create a New Job, this time select Pipeline instead of Freestyle Project.

![image](https://user-images.githubusercontent.com/117350787/235579649-fae9b350-3344-475b-9ced-185aa7785e8c.png)

- Follow the Official Jenkins [example](https://www.jenkins.io/doc/pipeline/tour/hello-world/)

![image](https://user-images.githubusercontent.com/117350787/235579885-ec8aa6c5-d71c-4422-84be-c6f4692d80ba.png)

![image](https://user-images.githubusercontent.com/117350787/235580064-26b8bdbc-468a-4cea-b771-ffdc087a9e35.png)

- Complete the project using the Declarative pipeline

![image](https://user-images.githubusercontent.com/117350787/235580148-5ab4a7e2-f200-4a32-9925-b1b9301f3caf.png)

![image](https://user-images.githubusercontent.com/117350787/235580291-6be62984-ad1b-4868-8f19-f90939891f8b.png)

![image](https://user-images.githubusercontent.com/117350787/235580396-5710bf4d-a95a-4fdd-a144-f92b35c77ebb.png)

![image](https://user-images.githubusercontent.com/117350787/235580541-2c468ff1-b2e7-4609-9193-c7ddb4252494.png)

- In case of any issues feel free to post on any Groups, [Discord](https://discord.gg/Q6ntmMtH) or [Telegram](https://t.me/trainwithshubham)

![image](https://user-images.githubusercontent.com/117350787/235582028-a238cbab-f7e7-47ea-b31b-132aa2cd328c.png)

![image](https://user-images.githubusercontent.com/117350787/235580727-0072bf5d-ff43-44dc-a774-52b046f518e2.png)

Happy Learning:)

# Day26 task is completed!
