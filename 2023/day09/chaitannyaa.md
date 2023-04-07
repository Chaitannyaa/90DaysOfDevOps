# Day 9 Task: Deep Dive in Git & GitHub for DevOps Engineers.

## Find the answers by your understandings(Shoulden't be copied by internet & used hand-made diagrams) of below quistions and Write blog on it.

# What is Git and why is it important?

Git is a Version Control Tool developed by Linus Torvald who also gave Linux to the world. Git can track our file changes regarding many parameters like creation, modification, deletion details by users and can help to get back to your any previous action on it. Its just like creating new versions of our work and we can switch back to any version as per our desire and hence this is called version control system tool.

Why it is important: If you have made some changes to a software files and you feel that is not good then you retrive the previous state of software quikly with git tool. You can collaborate with people to 

# What is difference Between Main Branch and Master Branch?

In Git, the terms "main" and "master" are both used to refer to the primary branch in a repository.

The term "master" was used as the default name for the primary branch in Git. But this term was replaced with "main" due to concerns about the differenciation mentality of the term "master" like "master:slave" terminology.

# Can you explain the difference between Git and GitHub?

Git and GitHub are related but different tools.

Git is a distributed version control system that allows developers to track changes to their code over time. It allows us to create and manage different versions of their code, collaborate with others, and easily roll back to a previous version if necessary. Git is a command-line tool that can be used local machine.

GitHub is a web-based hosting service for Git repositories. It provides a platform to collaborate on code, host Git repositories, and manage the entire software development process. GitHub has variety of features including code review, issue tracking, project management tools, etc.

# How do you create a new repository on GitHub?

- Go to the GitHub website and sign in to your account.
- Click on the "+" icon in the top right corner of the page and select "New repository".
- Choose a name for your repository. Select appropriate opitons to create your repository.
- It's done.

# What is difference between local & remote repository? How to connect local to remote?

A local repository is a copy of a repository that is stored on your local machine, while a remote repository is a copy of the same repository that is stored on a server or a cloud-based hosting service, such as GitHub. local repository is stored on your own machine and can only be accessed by you, while a remote repository can be accessed by anyone who has permission to access it.

## Connect a local repository to a remote repository:

- Create a new repository on the remote server (GitHub) and clone it to local machine using "git clone {repo url}

                      or

- Create repo on local having same name that of remote repo name.

- Add remote access to repo: "git remote add origin {remote repository URL}"

- Verify the connection between the local and remote repositories using the command "git remote -v"

- Push the local repository to the remote repository using the command "git push origin main"

- Pull updates from remote repository to the local repository using the command "git pull origin main"

# Tasks

## task-1:

1. Set your user name and email address, which will be associated with your commits.

![image](https://user-images.githubusercontent.com/117350787/230587368-6c547cd3-72cb-46b4-a495-d034c23e7ee8.png)

## task-2:

1. Create a repository named "Devops" on GitHub

![image](https://user-images.githubusercontent.com/117350787/230587919-1a7dafbe-d56b-4498-9497-9ca86dc47292.png)

2. Connect your local repository to the repository on GitHub.

![image](https://user-images.githubusercontent.com/117350787/230588154-b1dcd6d7-93ed-4d60-ac89-61922e1574d7.png)

3. Create a new file in Devops/Git/Day-02.txt & add some content to it.

![image](https://user-images.githubusercontent.com/117350787/230588556-1d35d8d1-ddb5-49f3-a1ff-01a9b6ae2082.png)

4. Push your local commits to the repository on GitHub

![image](https://user-images.githubusercontent.com/117350787/230588917-56ec8f14-9c15-4999-9c7e-58b0d7ebd974.png)

![image](https://user-images.githubusercontent.com/117350787/230589034-53412fdd-a85b-4b0a-ada2-56bf39c57373.png)

# Day09 task is completed!
