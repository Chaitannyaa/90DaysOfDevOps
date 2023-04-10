# Day 11 Task: Advance Git & GitHub for DevOps Engineers: Part-2

## Task-01

- Create a new branch and make some changes to it.

![image](https://user-images.githubusercontent.com/117350787/230971241-b17f1d03-de54-4ab0-96dd-4b5d543fe98f.png)

- Use git stash to save the changes without committing them.

![image](https://user-images.githubusercontent.com/117350787/230971391-2bf5961c-ab67-4fd2-b40d-83bd1e923c01.png)

- Switch to a different branch, make some changes and commit them.

![image](https://user-images.githubusercontent.com/117350787/230971513-31100dc6-35cd-4c20-b482-11ca1a1ce2c1.png)

- Use git stash pop to bring the changes back and apply them on top of the new commits.

![image](https://user-images.githubusercontent.com/117350787/230971986-921b43dc-61e3-4ae5-b50d-0da9ada47a35.png)

## Task-02

- In version01.txt of development branch add below lines after “This is the bug fix in development branch” that you added in Day10 and reverted to this commit.

- Line2>> After bug fixing, this is the new feature with minor alteration”

Commit this with message “ Added feature2.1 in development branch”

![image](https://user-images.githubusercontent.com/117350787/230973817-4507c026-c7fb-45c8-a462-fa0dcf4296b9.png)

- Line3>> This is the advancement of previous feature

Commit this with message “ Added feature2.2 in development branch”

![image](https://user-images.githubusercontent.com/117350787/230974075-97f8d693-e53a-408f-b87c-d5545d77f366.png)

- Line4>> Feature 2 is completed and ready for release

Commit this with message “ Feature2 completed”

![image](https://user-images.githubusercontent.com/117350787/230974308-ec3bb6bc-cad6-4830-a87d-f56af0d6f34c.png)

- All these commits messages should be reflected in Production branch too which will come out from Master branch (Hint: try rebase).

![image](https://user-images.githubusercontent.com/117350787/230978850-d96a99ec-3eb1-4197-872b-481be2925683.png)

![image](https://user-images.githubusercontent.com/117350787/230978997-c0066f1b-82d7-4e39-8bef-14b09c0f5f1c.png)

![image](https://user-images.githubusercontent.com/117350787/230976769-b965432f-1fd6-4249-859f-3ce284e5ac37.png)

![image](https://user-images.githubusercontent.com/117350787/230979199-f13e9c94-3163-4143-b59d-0e3c1f9fa9e7.png)

![image](https://user-images.githubusercontent.com/117350787/230979656-ee9209c4-82ed-4bbe-a17b-c3e6689d4f54.png)


## Task-03

- In Production branch Cherry pick Commit “Added feature2.2 in development branch” and added below lines in it:

![image](https://user-images.githubusercontent.com/117350787/230981316-e9359d4a-a301-4a66-b933-1b8405345be5.png)

- Line to be added after Line3>> This is the advancement of previous feature

![image](https://user-images.githubusercontent.com/117350787/230981677-adc71acb-8017-472c-848a-47176739680b.png)

- Line4>>Added few more changes to make it more optimized.
Commit: Optimized the feature

![image](https://user-images.githubusercontent.com/117350787/230981998-9e5930e0-beda-443b-bf4b-c4651daabed4.png)

You can Post on LinkedIn and let us know what you have learned from this task by #90DaysOfDevOps Challange. Happy Learning :)

https://www.linkedin.com/posts/activity-7051286623736537089-nhqd?utm_source=share&utm_medium=member_desktop

# Day 11 task Completed
