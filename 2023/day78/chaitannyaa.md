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

     Select the appropriate metric(s) based on your monitoring requirements. You can add multiple conditions by clicking on "Add condition" again.

   c. Set the conditions for triggering the alert. For example, you can set a threshold for CPU Utilization to trigger the alert when it exceeds 60% for a duration of 5 minutes. Adjust the thresholds and durations based on your specific needs.

   d. Specify the notification channel you added earlier to receive the alerts. Select the appropriate channel from the "Send to" dropdown menu.

7. Save the alert rule, and Grafana will start monitoring the selected EC2 instance based on your defined conditions and send alerts to the configured notification channel when triggered.

## Setup alerts for AWS Billing Alerts.


For Reference: https://www.linkedin.com/posts/chetanrakhra_devops-project-share-activity-7044695663913148416-LfvD?utm_source=share&utm_medium=member_desktop
