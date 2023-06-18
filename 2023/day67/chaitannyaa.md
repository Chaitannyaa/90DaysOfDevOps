# Day 67: AWS S3 Bucket Creation and Management

## AWS S3 Bucket

Amazon S3 (Simple Storage Service) is an object storage service that offers industry-leading scalability, data availability, security, and performance. It can be used for a variety of use cases, such as storing and retrieving data, hosting static websites, and more.

In this task, you will learn how to create and manage S3 buckets in AWS.

## Task

- Create an S3 bucket using Terraform.

```sh
# Create an S3 bucket
resource "aws_s3_bucket" "my_bucket" {
  bucket = "my-bucket-name"
}
```

- Configure the bucket to allow public read access.

```sh
# Configure public read access for the bucket
resource "aws_s3_bucket_public_access_block" "my_bucket_public_access_block" {
  bucket_name         = aws_s3_bucket.my_bucket.id
  block_public_acls   = false
  block_public_policy = false
  ignore_public_acls  = false
  restrict_public_buckets = false
}
```

- Create an S3 bucket policy that allows read-only access to a specific IAM user or role.

```sh
# Create an S3 bucket policy that allows read-only access to a specific IAM user or role
resource "aws_s3_bucket_policy" "my_bucket_policy" {
  bucket = aws_s3_bucket.my_bucket.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          AWS = "arn:aws:iam::ACCOUNT_ID:user/USERNAME"
        }
        Action = [
          "s3:GetObject",
          "s3:GetObjectVersion"
        ]
        Resource = "${aws_s3_bucket.my_bucket.arn}/*"
      },
      {
        Effect = "Allow"
        Principal = {
          AWS = "arn:aws:iam::ACCOUNT_ID:role/ROLENAME"
        }
        Action = [
          "s3:GetObject",
          "s3:GetObjectVersion"
        ]
        Resource = "${aws_s3_bucket.my_bucket.arn}/*"
      }
    ]
  })
}
```

- Enable versioning on the S3 bucket.

```sh
resource "aws_s3_bucket_versioning" "my_bucket_versioning" {
  bucket = aws_s3_bucket.my_bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}
```

**Let's create our resources--->**

```sh
provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "my_bucket" {
  bucket = "chaitannyaa"
}

resource "aws_s3_bucket_public_access_block" "my_bucket_public_access_block" {
  bucket = aws_s3_bucket.my_bucket.id
  block_public_acls   = false
  block_public_policy = false
  ignore_public_acls  = false
  restrict_public_buckets = false
}

resource "aws_s3_bucket_policy" "my_bucket_policy" {
  bucket = aws_s3_bucket.my_bucket.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          AWS = "arn:aws:iam::753938387830:user/Admin"
        }
        Action = [
          "s3:GetObject",
          "s3:PutObject"
        ]
        Resource = "${aws_s3_bucket.my_bucket.arn}/*"
      },
      {
        Effect = "Allow"
        Principal = {
          AWS = "arn:aws:iam::753938387830:role/DevOps-User"
        }
        Action = [
          "s3:GetObject",
          "s3:PutObject"
        ]
        Resource = "${aws_s3_bucket.my_bucket.arn}/*"
      }
    ]
  })
}

resource "aws_s3_bucket_versioning" "my_bucket_versioning" {
  bucket = aws_s3_bucket.my_bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}
```
![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/51225476-140c-4b77-94fa-0dd9f7910b4c)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/8eb7e0cd-7ba3-47d3-8da4-7ba43858f5d5)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/f327f23b-04e8-4f36-b9a8-c49b458f38e1)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/a29c63f0-acf9-4fe5-bfee-42abd7cb080b)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/e70bae08-1433-4b99-b62e-2f6ce75cc077)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/b26dc4b9-bcb1-433d-af37-9f72275b620c)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/854bf1a5-03a2-4354-9415-4737a72b38cb)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/86db2081-9877-433b-9346-81eee11fde34)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/a18bbdc9-00dc-45e3-bc62-426f3a594c8a)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/c1b6ac7d-5c75-4a0e-af00-6235665777a0)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/4dc619c1-f4f4-443c-b8cd-0e8975786f80)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/b89d2c03-98eb-4ce2-a328-f998bbd8bee1)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/afb91088-bbb3-4734-9fec-1debfb051ed3)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/9a5d5ba7-87bb-41dc-8751-b7b8589ceb26)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/ba2ffe06-f1fe-400d-af99-c87c9294e0f1)


**Happy learning!**

# Day 67 task is complete!
