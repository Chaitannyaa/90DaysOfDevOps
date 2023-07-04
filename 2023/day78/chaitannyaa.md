Day - 78 : Create Grafana Alerting for An AWS EC2 instance and Your AWS account billing

**Pre-requisites--->**

- Grafana server configured with Data Source:Prometheus [Refer](https://90daysofdevopschallenge.hashnode.dev/day74-90daysofdevops-challenge-tws)

- An AWS account for monitoring billing alerts [Refer](https://aws.amazon.com/free/?trk=17a47518-9bfe-4f1e-a67f-42bdd19264e5&sc_channel=ps&ef_id=CjwKCAjw44mlBhAQEiwAqP3eVtVUav8CKJEQyq5uKDZ1DwpoeOBuYMAGE5TKBwgV8b6AnRWkjuP6-BoCPZMQAvD_BwE:G:s&s_kwcid=AL!4422!3!525855180410!p!!g!!amazon%20web%20server!13385427590!122597168825&all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all)

- A Linux Ec2 Instance running and registered with prometheus as a Target machine.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/5ba991d6-abef-40f7-8074-cf90fb6e1b20)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/8c92379c-a572-466d-ab30-b779b1a4d388)

# Let's get started 

## Setup alerts for our AWS EC2 instance. (Linux-Ubuntu_22.04_LTS)

1. Start by logging into your Grafana Server.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/25956352-27ec-4a49-9279-d416bb9616fa)

2. Navigate to the "Alerting" section in the left sidebar and click on "Notification channels".

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/65edd7d0-f7bf-4cab-a78e-4772be1f9acd)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/27f33d9a-09db-4036-9baf-0c87922cb28f)

3. Add the appropriate notification channel, such as email or a messaging service like Slack, where you want to receive the alerts. Follow the instructions provided by Grafana to set up the notification channel.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/c053294a-a424-41dd-a9d4-2338ff69d2ec)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/cbe6601e-94f1-4c0f-940c-3d638063c700)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/c14e3e35-60e7-43e5-9091-faa48d8b9c8f)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/c88ab857-e554-4b72-9331-c831629ba2af)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/4a6ef6d4-dfab-4db4-8877-3c0e972a0b1e)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/ea6f5721-a3df-47a1-9977-5b51f2a88bfe)

4. Once the notification channel is set up, go back to the "Alerting" section and click on "New alert".

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/c74bea6a-790b-4101-b1f2-8f2253b1ef18)

5. Configure the alert rule:

   a. Give the alert rule a name that clearly describes its purpose, such as "EC2 Instance Monitoring".

   ![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/e60603ca-c3eb-475b-9542-5f4c420453c4)

   ![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/f9e83c55-1584-49db-ab08-82e805792011)

   ![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/edf06034-cd64-4852-8ce8-ca36fef4f417)

   ![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/c024c785-3d4f-4ad1-9db2-19a9e05b9476)

   ![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/d5c4421d-c28b-4259-a75f-41fc43edcd65)

   ![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/d9c67e37-0cb7-404b-aafe-d4369a742822)

   ![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/539efd44-3719-44be-a7ce-f1a11903bee0)

   b. In the "Conditions" section, click on "Add condition" and select the metric you want to monitor. Some commonly used metrics for EC2 instance monitoring include:

      - CPU Utilization (%): Monitors the percentage of CPU utilization by the EC2 instance.
      - Memory Usage (%): Monitors the percentage of memory (RAM) usage by the EC2 instance.
      - Disk Space (%): Monitors the percentage of disk space usage on the EC2 instance's disk(s).
      - Network In (Bytes): Monitors the incoming network traffic in bytes.
      - Network Out (Bytes): Monitors the outgoing network traffic in bytes.
      - Status Check Failed: Monitors if the EC2 instance's status checks are failing.

   ![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/c9686b1c-13c0-4539-8b24-e94df6da8814)

   ![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/0845e1f5-f5d1-4d70-a88f-1703685d80c8)

   ![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/f04b9d92-2d54-4bb1-a96b-1f994907ddbe)

   ![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/781d8784-4659-4ac7-9024-660bad465db2)

   ![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/31c1228e-c5e0-4cdc-9cd2-8c9333d9496f)

   ![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/81019f60-1dc1-4036-8870-4d374ce3fe0c)

   Select the appropriate metric(s) based on your monitoring requirements. You can add multiple conditions by clicking on "Add condition" again.

   d. Specify the notification channel you added earlier to receive the alerts. Select the appropriate channel from the "Send to" dropdown menu.

   ![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/57f7993b-4cab-481c-8486-5dcd6e959f63)

6. Grafana will start monitoring the selected EC2 instance based on your defined conditions and send alerts to the configured notification channel when triggered.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/e76b9dd8-3cba-4182-a3ce-2bb67ab51b43)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/b7940d78-b129-4e10-afca-04693f65f7a8)

## Have you received any alert on slack channel? Let's check--->

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/3c1a853d-c041-4684-9607-c578792a79cb)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/e4e68ca2-cb1c-4472-be32-ce3a42d1b0c3)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/a8d2ae02-6776-40db-bfc0-94bdca485562)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/b978aac3-1de0-404b-b65a-8e3bbc384072)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/41ccd78d-52e3-46d3-b1ea-89fa532dad41)

## Setup Grafana for AWS Billing Alerts using CloudWatch as Data source.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/a83df5da-1ba7-413a-bc66-09324a03b11d)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/290b61e5-051d-4147-9d64-4b317b568b3f)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/ab0a3407-3eda-4278-99c9-5332e889ad6e)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/f7ed8719-c4e4-44e2-a4c8-6ca1ef933ba2)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/87fcb410-b017-44ad-ac4b-f07121efddb6)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/7e9e5069-ea7a-4085-abcb-39054f1053c7)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/73fafa0c-9dba-42aa-a110-db7e59a0e9fa)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/e0136298-fd9e-4cbd-a54f-de2426cb5553)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/111b55f0-98d3-44e4-aa22-06de0a8cdb9d)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/f962cbcc-f545-42ed-8d85-e6a299a57c8e)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/88d67f5b-0a55-48c0-898a-f44b72535418)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/d4e8ca33-d26a-491f-b89b-d46c3be917f8)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/315a2d7d-1ec9-46d4-943c-339b30270135)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/5453a851-19f7-486a-ae6c-5b455274cffa)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/d4c804d4-4915-4d50-8a79-cba2458cdd07)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/8c8967e9-a40c-4dda-b252-4876c79bcf0b)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/1e5b9c68-d4b0-43c4-93d5-86b1355a6039)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/4d42d458-21a1-49fd-8e8c-35334e937edc)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/7c770eb7-ffbe-4b8b-9e54-549c3a6bcee5)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/6caff6d0-1e7e-4911-ab16-ebd667ab785f)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/24123c00-5a9f-4ce9-87ad-eb67152db524)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/08394938-c84c-446f-97fd-ab72f159224f)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/113e770a-b6ce-4095-ad3b-14c2ce70b06d)

### Happy Learning!

# Day 78 task is complete!
