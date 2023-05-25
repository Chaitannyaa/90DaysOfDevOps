# Day 51: Your CI/CD pipeline on AWS - Part 2 🚀 ☁

## What is CodeBuild ? 
- AWS CodeBuild is a fully managed build service in the cloud. CodeBuild compiles your source code, runs unit tests, and produces artifacts that are ready to deploy. CodeBuild eliminates the need to provision, manage, and scale your own build servers.

# Task-01 :
- Read about Buildspec file for Codebuild.

A buildspec is a collection of build commands and related settings, in YAML format, that CodeBuild uses to run a build. You can include a buildspec as part of the source code or you can define a buildspec when you create a build project.  

https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html#build-spec-ref-name-storage

If you include a buildspec as part of the source code, by default, the buildspec file must be named buildspec.yml and placed in the root of your source directory.

Buildspec syntax--->

```sh
version: 0.2
  
phases:
  install:
    on-failure: ABORT | CONTINUE
    commands:
      - command
      - command
    finally:
      - command
      - command
  pre_build:
    on-failure: ABORT | CONTINUE
    commands:
      - command
      - command
    finally:
      - command
      - command
  build:
    on-failure: ABORT | CONTINUE
    commands:
      - command
      - command
    finally:
      - command
      - command
  post_build:
    on-failure: ABORT | CONTINUE
    commands:
      - command
      - command
    finally:
      - command
      - command
artifacts:
  files:
    - location
```

- Create a simple index.html file in CodeCommit Repository

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/dcc469ca-99a3-47cb-9675-048b50a0de7d)

- You have to build the index.html using nginx server

```sh
version: 0.2

phases:
  install:
    commands:
      - echo Installing NGINX
      - sudo apt-get update
      - sudo apt-get install nginx -y
  build:
    commands:
      - echo Build started on 'date'
      - cp index.html /var/www/html/
  post_build:
    commands:
      - echo Configuring NGINX

artifacts:
    files:
      - "**/*"
```

# Task-02 :
- Add buildspec.yaml file to CodeCommit Repository and complete the build process.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/8c4aebb4-dea0-4221-881b-6a22fbe41d5c)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/f578527b-78eb-4314-b96c-ed43686142bf)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/c60bf3b2-1f2b-4ed8-8f1a-cf3172a02689)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/73d13660-354b-4aa4-8f76-aa33803c67d5)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/8204436d-9e4f-4ede-9005-16a602b529dd)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/98fe0975-164f-4165-9fed-d98cd5e0c3c8)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/c7ca3445-e216-429e-b1b1-bd2cd2b54dd2)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/3e7c4c2f-8c56-49b9-9794-07732227899f)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/fbdb9c2d-796e-4183-9e7d-e83fdd9e0ef0)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/2cb97681-547f-49d2-979f-5dcae7367006)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/93916bed-3ba8-49df-b6e3-83a82e21eb8d)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/92007e9e-66fe-43ed-905e-43e1fb7d4fda)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/5dbfd18b-3c66-48ea-9fe8-9bb4e77ef8f9)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/3cd3bef1-df7b-40ed-884d-5e7455326281)

Happy Learning :)

I hope you enjoyed the task with me :)

# Day 51 task is complete!
