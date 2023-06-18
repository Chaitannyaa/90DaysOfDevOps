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

**Happy learning!**

# Day 67 task is complete!
