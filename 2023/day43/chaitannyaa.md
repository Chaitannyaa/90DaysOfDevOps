# Day 43: S3 Programmatic access with AWS-CLI 💻 📁

![s3](https://user-images.githubusercontent.com/115981550/218308379-a2e841cf-6b77-4d02-bfbe-20d1bae09b20.png)

# S3
Amazon Simple Storage Service (Amazon S3) is an object storage service that provides a secure and scalable way to store and access data on the cloud. It is designed for storing any kind of data, such as text files, images, videos, backups, and more.
Read more [here](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)

## Task-01
- Launch an EC2 instance using the AWS Management Console and connect to it using Secure Shell (SSH).

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/894f561d-6355-4519-b832-d022e92c7eb1)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/41f5e3b9-10be-41da-adcc-0ac239cd82ca)

- Create an S3 bucket and upload a file to it using the AWS Management Console.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/b7a46c9c-9266-4624-b367-a1951f140872)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/06f2b49f-fc9b-47ee-a89b-6394b4bb0ce1)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/f35c6a39-c2c4-40a0-832c-92484b901e62)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/bff30bd2-846a-407e-9a48-b00125809956)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/0b5aa075-2ebf-4d38-8106-5fe7772d3c62)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/e1d43f04-415a-45d4-a996-6f77c6ba5e7c)

- Access the file from the EC2 instance using the AWS Command Line Interface (AWS CLI). 

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/4aa0ea63-6409-4e30-90c8-92617ccd23eb)

- Download a file from the S3 bucket using the AWS CLI.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/0a043947-9537-4693-8cb2-18d74d932b52)

Read more [here](https://docs.aws.amazon.com/cli/latest/reference/s3/index.html)

## Task-02
- Create a snapshot of the EC2 instance and use it to launch a new EC2 instance.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/a1db652d-92be-40c8-979c-9d1ce049ab53)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/8d265606-605e-4ede-8127-258ea02558f6)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/60b458d1-f10d-4972-9319-9c21ac63ad00)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/3ba082a1-54a9-4dc2-a902-fe414c8a16aa)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/004d012f-c4aa-43c4-9cbd-886ae3dc0edb)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/706c38ba-4789-4269-b167-22e12d2e0438)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/ba3bce8e-678b-4933-92a3-d0167a55a23d)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/de5078b2-63f2-441b-9d18-40227192e6b7)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/0a89e868-0e3e-4b5c-824d-cb39ab9dc18a)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/0cb2dd33-f28a-4f87-b9ce-79d7f3cf3702)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/8e78c0b6-620a-44c2-960d-2b673ab0c262)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/d6f014b0-1a60-4867-9baa-fc105f2b3115)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/7ab661bd-b7d2-4df5-a255-7831203959e3)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/b9f5d058-b826-4fe1-9e5e-4b58288048bd)

- Verify that the file is available inside our newly created instance.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/9be39976-7da2-436b-a4cf-aea6c0f1fd1e)

Here are some commonly used AWS CLI commands for Amazon S3:

`aws s3 ls` - This command lists all of the S3 buckets in your AWS account.

`aws s3 mb s3://bucket-name` - This command creates a new S3 bucket with the specified name.

`aws s3 rb s3://bucket-name` - This command deletes the specified S3 bucket.

`aws s3 cp file.txt s3://bucket-name` - This command uploads a file to an S3 bucket.

`aws s3 cp s3://bucket-name/file.txt .` - This command downloads a file from an S3 bucket to your local file system.

`aws s3 sync local-folder s3://bucket-name` - This command syncs the contents of a local folder with an S3 bucket.

`aws s3 ls s3://bucket-name` - This command lists the objects in an S3 bucket.

`aws s3 rm s3://bucket-name/file.txt` - This command deletes an object from an S3 bucket.

`aws s3 presign s3://bucket-name/file.txt` - This command generates a pre-signed URL for an S3 object, which can be used to grant temporary access to the object.

`aws s3api list-buckets` - This command retrieves a list of all S3 buckets in your AWS account, using the S3 API.

Happy Learning :)

# Day 43 task is complete!
