# Day 53: Your CI/CD pipeline on AWS - Part 4 🚀 ☁

On your journey of making a CI/CD pipeline on AWS with these tools, you completed AWS CodeCommit, CodeBuild & CodeDeploy.

# Let's hands-on with AWS CodePipeline --->

## What is CodePipeline ? 
CodePipeline builds, tests, and deploys your code every time there is a code change, based on the release process models you define.
Think of it as a CI/CD Pipeline service

# Task-01 :
- Build a project to get source code from GitHub repo and store build artifacts on S3.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/b5126a65-0620-4b72-8ee7-d165d84b0443)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/b4ba0a4f-a35f-4913-a43a-20f6f1bbacec)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/1dd32d39-a97f-4728-a1ab-b2fe637639b1)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/50b12000-1a45-45f0-b52d-8fa4649664ed)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/40483463-568e-44ca-bd01-1c6425b922ab)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/2a0a3955-7ff1-4ebb-b208-b271023c12b5)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/eaa101de-2fdf-456f-aa7a-9ba0994ff224)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/869ca001-c209-4fdf-a6a4-98425b49dcbf)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/02dc6c6d-2fbb-4a49-83b2-322907280db7)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/94a843c1-00b1-4516-b0f5-4d99e6bee995)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/861d5df4-dd08-4fc4-b9ec-94300afe6576)


- Create a CodePipeline that gets the code from CodeCommit, Builds the code using CodeBuild and deploys it to a Deployment Group.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/f38a0a22-4fd1-41d3-8b38-92815ad98a41)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/3d1643b2-b9fd-47e4-b2fc-56dd10befa96)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/da67115b-d342-4d61-99c1-8bc3315f6727)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/e2c16c03-7b34-4d6a-8c97-e3be31831d65)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/f28e2d6e-3fad-4ca7-9224-4dc0d31a507e)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/ef466e10-6d8d-448a-8ca3-c2039bf62be8)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/fb7af585-a344-49d8-9731-fe3d71cfb483)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/37105db5-0050-4979-8f1a-92b65cd2f220)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/ce271f6d-0f9f-4c65-9778-0ee1424fe3f3)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/4d883ad9-7ac7-406e-95ed-da5976d63345)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/690bab8b-88d8-46d4-9f94-d07d0fcce4fd)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/70237a3f-725d-499a-90d8-91742041229a)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/bc7d0ed9-d213-4723-b41f-4a03b6777228)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/d59d2ee8-d4c8-4191-bf3c-5ba352161fe6)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/ade32dbc-9683-4fd7-9f7c-e181ba8d7b08)

- Now let's commit to GitHub source code to trigger the pipeline

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/f6aca1ae-9b89-4f31-a053-d707f82f2342)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/6b45c59e-1b47-4ed6-bc8a-3a5c52798ac4)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/d154cc0e-1b1d-4a21-8f09-af10d046f168)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/2e44a50b-8776-46a1-b24b-8302ddda1278)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/58cdf2c3-e841-4425-b72b-a3bd6785f0e9)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/ffd09f55-a4a5-45e8-b4f5-e54f94d7211f)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/03835cd9-625f-441c-b9d7-ab8088b0e4c7)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/5ce349b2-c56b-4f89-b959-908cd794e5d1)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/1d214572-a71b-4dd9-944d-94196c798cb3)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/bc8ba090-0466-4865-86c7-a440fff2c922)

This is how AWS CodePipeline Works!
Happy Learning :)

# Day 53 task is complete!



