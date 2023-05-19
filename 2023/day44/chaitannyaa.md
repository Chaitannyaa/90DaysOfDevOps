# Day 44: Relational Database Service in AWS

Amazon Relational Database Service (Amazon RDS) is a collection of managed services that makes it simple to set up, operate, and scale databases in the cloud

## Task-01

- Create a Free tier RDS instance of MySQL

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/1641009e-be11-4f4b-8610-bd6bf1d1c3e1)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/7c11ac5f-474d-4d55-9c1c-8be7f85996d2)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/4a540126-3c66-4519-9d45-0f24cc2b429b)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/fda68262-880f-4e22-99b2-97aadfb97fc6)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/b765cf0e-ea47-46c4-ada6-23aa90b60bf6)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/bd076026-2eba-4e80-a14d-dbfd85f20978)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/241522fe-a112-4b40-a833-d51ac6a4197c)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/d19282b3-f911-4988-a6b9-0aec516dd6ef)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/a6af5e03-93e0-454a-8607-07cd13f7167a)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/1232da3e-6de8-49cf-a109-58575501f8cc)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/f9593086-d8ec-43be-9468-7bab4de5df10)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/c8f5e240-6e77-413b-8dc2-aa31e9226d2b)

- Create an EC2 instance

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/c14e85b5-f0e4-481c-9870-4e1b8d0c9126)

- Create an IAM role with RDS access

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/14e1e992-a825-4974-9151-e33e4e47b3e7)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/f629335e-696f-48c3-808f-e3929ed30b9a)

- Assign the role to EC2 so that your EC2 Instance can connect with RDS

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/ec156054-2a8a-4381-ac3c-b5006a960ae3)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/fffca8d7-b47e-4885-acdf-562c59c6a2c6)

- Once the RDS instance is up and running, get the credentials and connect your EC2 instance using a MySQL client.

```sh
mysql -h [Endpoint] -u [Username] -p [DatabaseName]
```
```sh
mysql -h my-database.cxtd1comdmzm.us-east-1.rds.amazonaws.com -u Admin -p chaitannyaa
```
![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/bcbf01d9-c507-47fe-a18d-bd4b3da86ce9)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/ba9bb3d1-b009-403a-b641-7d4a7ab4600c)

- Post the screenshots once your EC2 instance can connect a MySQL server

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/595b8a60-c19c-47fe-a4cf-f9c52e0c3669)

Hint:
You should install mysql client on EC2, and connect the Host and open Port(3306) of RDS with this client.

Happy Learning:)

# Day44 task is complete!

