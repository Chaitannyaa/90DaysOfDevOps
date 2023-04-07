# Day 8 Task: Basic Git & GitHub for DevOps Engineers.

## Task:

- Install Git on your computer (if it is not already installed). You can download it from the official website at https://git-scm.com/downloads

![image](https://user-images.githubusercontent.com/117350787/230553687-f6075067-226c-4be3-a196-af85f52ad0d4.png)

- Create a free account on GitHub (if you don't already have one). You can sign up at https://github.com/

![image](https://user-images.githubusercontent.com/117350787/230554035-38fac715-d3b3-494b-8d28-03794e5ec97a.png)

- Learn the basics of Git by reading through the video This will give you an understanding of what Git is, how it works, and how to use it to track changes to files.

Git is VCS tool- provides file tracking regarding when and who created, modified, deleted the file. Also you can revert the modification done to it. 

Following are the basic git commands:

$ git init-------------------------->To initialize the current directory as a git repo.

$ git status------------------------>Check git repo and Local FS are on same state or not.

$ git add <filename>---------------->Add file to staging area

$ git commit -m <filename>---------->add file to git repo to start tracking it

$ git log--------------------------->check git operations history

$ git restore <filename>------------>to get the last commited state of particular file

$ git config --global user.name "username"------------->Add user details because git keeps track of commiters activity

$ git config --global user.email "user_email_add"---->Add user details because git keeps track of commiters activity

$ git rm --cached <filename>---------------------------> to removed file from stagging area before commiting it

$ git rm --cached -f <filename>------------------------> to removed from stagging area

$ git remote -v------------------------> check remote access availability to your local repo

$ git remote add origin <url>----------> add remote access to server repo

$ git push origin master--------------->push commit from local master branch to remote

$ git push origin main----------------->push commit from local main branch to remote

$ git checkout -b dev------------------>create a new branch-dev from parent branch and switch to it

$ git diff master-------------------> Check diff between current and master branch 

$ git branch------------------------>check branhces available

$ git switch <name of branch>------->switch to different branch

$ git branch -d <branchname>-------->delete particular branch

$ git clone </repos/url/>------------->clone the remote repo to local machine

## Exercises:

- Create a new repository on GitHub and clone it to your local machine

![image](https://user-images.githubusercontent.com/117350787/230557268-57cd472e-eff5-46ef-aca2-2c06ff949ee6.png)

![image](https://user-images.githubusercontent.com/117350787/230557469-846abd83-7077-4083-8918-6840a01a7dd7.png)

- Make some changes to a file in the repository and commit them to the repository using Git

![image](https://user-images.githubusercontent.com/117350787/230558263-2e300f1a-48c9-4957-965c-a33281497d55.png)

- Push the changes back to the repository on GitHub

![image](https://user-images.githubusercontent.com/117350787/230558632-21a07411-d170-4f24-b21f-8a4d889bc71a.png)


## Day08 task is completed!
