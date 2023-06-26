# Day 74 - Monitor your AWS EC2 instances with Grafana and Prometheus.

Connect a Linux and Windows EC2 instance with Grafana. By doing so, we'll be able to monitor various components of our servers and gain valuable insights into their performance. So let's dive right in and get started!

## Step 1: Install Grafana and setup instances to monitor

To begin, we need to have Grafana installed on a separate EC2 instance or a server. Grafana is an open-source monitoring and visualization tool that provides a rich set of features for data analytics and monitoring various systems and applications.

1. Install Grafana by following this link---> [Install Grafana](https://90daysofdevopschallenge.hashnode.dev/day73-90daysofdevops-challenge-tws)

2. Launch another EC2 instance (Linux or Windows) on AWS for monitoring its resources using Grafana.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/2de282df-3839-4e95-9113-be7d3cbf055d)

I have created Linux instance - Ubuntu 22.04 LTS for this demo.

Once you have Grafana up and running on your server, Let's move to the next step.

## Step 2: Install and Configure Data Sources (Prometheus in this case)

Now Grafana is installed, we need to configure it to connect with our Linux and Windows EC2 instances. Grafana supports various data sources, including Prometheus, Graphite, Elasticsearch, and more. In our case, we'll focus on connecting with the EC2 instances directly.

1. Open your web browser and access the Grafana web interface by entering the IP address or domain name of your Grafana server.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/21f12536-07c0-405c-b860-bf91a9d5758e)

2. Log in to Grafana using your credentials. The default username and password are usually "admin" and "admin" respectively. Make sure to change the password after logging in.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/55122e9c-86ed-48ce-a31a-58fd5b6e3f1b)

3. Once logged in, go to the Configuration menu and select "Data Sources."

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/e7c7c943-563e-46cd-9f0f-2e356204d2d2)

4. Click on "Add data source" to add a new data source.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/23b9486c-c183-41e5-bf77-2569307a9de4)

5. Select the appropriate data source type for your EC2 instances. For Linux, you can choose "Prometheus" or "CloudWatch." For Windows, select "CloudWatch."

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/e6e518e0-5c98-4f27-a8c7-6fde3ce61386)

**Now you need to install Prometheus server as our data source--->**

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/f68746ab-073b-4c9d-8e6f-315829cdcf47)

**What is Node Exporter?**

Node Exporter is a Prometheus exporter specifically designed to collect and expose system-level metrics from a target machine. It is a popular component of the Prometheus monitoring ecosystem. Node Exporter runs as a separate service on the target machine and provides a wide range of metrics related to CPU usage, memory utilization, disk activity, network statistics, system load, and more.

Node Exporter collects these metrics by interacting with various operating system interfaces, such as /proc and /sys on Linux systems. It exposes these metrics in a Prometheus-compatible format, allowing Prometheus to scrape and store them for monitoring and alerting purposes.

**Let's install Prometheus on monitoring server where our Grafana is running and node exporter on both monitoring server and Targeted instance --->**

6. Configure the data source settings, including the AWS region and access credentials. Make sure to provide the necessary permissions to access the EC2 instances' metrics and data.


7. Test the data source connection to ensure everything is set up correctly.

Congratulations! You have successfully configured the data sources to connect with your EC2 instances. Now it's time to create dashboards and visualize the data.

## Step 3: Create Dashboards

Dashboards in Grafana are where you can design and visualize your data in a way that suits your monitoring needs. You can create multiple dashboards and customize them according to your preferences. Let's create a basic dashboard to monitor our EC2 instances.

1. In the Grafana web interface, click on the "Create" button and select "Dashboard."
2. Choose the visualization type you want to use, such as graphs, tables, or charts.
3. Configure the metrics and data you want to monitor. You can select specific EC2 instance metrics, such as CPU usage, memory usage, disk utilization, and network traffic.
4. Customize the dashboard layout, add panels, and arrange them as needed.
5. Save the dashboard and give it a meaningful name.

Once you have created your dashboard, Grafana will start fetching data from your EC2 instances and display it in real-time. You can explore various visualization options and features provided by Grafana to enhance your monitoring experience.

## Conclusion

Connecting EC2 instances with Grafana opens up a world of possibilities for monitoring and analyzing your server's performance. By following the steps outlined in this blog post, you can establish a seamless connection between your Linux and Windows EC2 instances and Grafana. This connection allows you to gain valuable insights into the different components of your servers, enabling you to make informed decisions and take necessary actions to optimize their performance.

Remember, monitoring is a continuous process, and Grafana provides a powerful platform to track your server's health and performance over time. Keep exploring Grafana's features, experiment with different metrics, and refine your dashboards to meet your specific requirements.

**Happy Learning and Happy Monitoring :)**

