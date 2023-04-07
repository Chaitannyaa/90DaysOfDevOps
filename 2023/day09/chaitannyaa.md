# Day 9 Task: Deep Dive in Git & GitHub for DevOps Engineers.

- Find the answers by your understandings(Shoulden't be copied by internet & used hand-made diagrams) of below quistions and Write blog on it.

1. What is Git and why is it important?

Git is a Version Control Tool developed by Linus Torvald who also gave Linux to the world. Git can track our file changes regarding many parameters like creation, modification, deletion details by users and can help to get back to your any previous action on it. Its just like creating new versions of our work and we can switch back to any version as per our desire and hence this is called version control system tool.

Why it is important: If you have made some changes to a software files and you feel that is not good then you retrive the previous state of software quikly with git tool. You can collaborate with people to 

2. What is difference Between Main Branch and Master Branch?

In Git, the terms "main" and "master" are both used to refer to the primary branch in a repository.

The term "master" was used as the default name for the primary branch in Git. But this term was replaced with "main" due to concerns about the differenciation mentality of the term "master" like "master:slave" terminology.

3. Can you explain the difference between Git and GitHub?

Git and GitHub are related but different tools.

Git is a distributed version control system that allows developers to track changes to their code over time. It allows us to create and manage different versions of their code, collaborate with others, and easily roll back to a previous version if necessary. Git is a command-line tool that can be used local machine.

GitHub is a web-based hosting service for Git repositories. It provides a platform to collaborate on code, host Git repositories, and manage the entire software development process. GitHub has variety of features including code review, issue tracking, project management tools, etc.

4. How do you create a new repository on GitHub?

- Go to the GitHub website and sign in to your account.
- Click on the "+" icon in the top right corner of the page and select "New repository".
- Choose a name for your repository. Select appropriate opitons to create your repository.
- It's done.

5. What is difference between local & remote repository? How to connect local to remote?

A local repository is a copy of a repository that is stored on your local machine, while a remote repository is a copy of the same repository that is stored on a server or a cloud-based hosting service, such as GitHub. local repository is stored on your own machine and can only be accessed by you, while a remote repository can be accessed by anyone who has permission to access it.

Connect a local repository to a remote repository:

1. Create a new repository on the remote server (GitHub) and clone it to local machine using "git clone {}
On your local machine, navigate to the directory that contains your project files.
Open the command line interface (e.g., Git Bash on Windows) and navigate to the project directory.
Initialize the local repository using the command git init. This will create a new local repository in the directory.
Connect the local repository to the remote repository by adding the remote URL using the command git remote add origin <remote repository URL>.
Verify the connection between the local and remote repositories using the command git remote -v.
Push the local repository to the remote repository using the command git push -u origin main (or git push -u origin master for older repositories). This will upload all the files and commits from the local repository to the remote repository.

# Tasks

## task-1:

Set your user name and email address, which will be associated with your commits.

## task-2:

1. Create a repository named "Devops" on GitHub

2. Connect your local repository to the repository on GitHub.

3. Create a new file in Devops/Git/Day-02.txt & add some content to it

4. Push your local commits to the repository on GitHub
