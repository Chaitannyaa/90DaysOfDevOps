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

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/fda78410-978a-4d46-9848-082b2a757af0)

**Install node_exporter--->**

- First, we will download the Node Exporter on both machines :

```sh
wget https://github.com/prometheus/node_exporter/releases/download/v0.15.2/node_exporter-0.15.2.linux-amd64.tar.gz
```

- Extract the downloaded archive

```sh
tar -xf node_exporter-0.15.2.linux-amd64.tar.gz
```

- Move the node_exporter binary to /usr/local/bin:

```sh
sudo mv node_exporter-0.15.2.linux-amd64/node_exporter /usr/local/bin
```

- Remove the residual files with:

```sh
rm -r node_exporter-0.15.2.linux-amd64*
```

- Next, we need to create users and service files for node_exporter.

For security reasons, it is always recommended to run any services/daemons in separate accounts of their own. Thus, we are going to create an user account for node_exporter. We have used the -r flag to indicate it is a system account, and set the default shell to /bin/false using -s to prevent logins.

```sh
sudo useradd -rs /bin/false node_exporter
```

Then, we will create a systemd unit file so that node_exporter can be started at boot. 

```sh
sudo nano /etc/systemd/system/node_exporter.service
```

-------------------------------------
```sh
[Unit]
Description=Node Exporter
After=network.target

[Service]
User=node_exporter
Group=node_exporter
Type=simple
ExecStart=/usr/local/bin/node_exporter

[Install]
WantedBy=multi-user.target
```
------------------------------------

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/5d3dac7c-e441-422f-810e-7e4be6a10c7e)

- Since, we have created a new unit file, we must reload the systemd daemon, set the service to always run at boot and start it :

```sh
sudo systemctl daemon-reload
sudo systemctl enable node_exporter
sudo systemctl start node_exporter
```

**Installing Prometheus--->**

- Download and install Prometheus only on the Prometheus Server.

```sh
wget https://github.com/prometheus/prometheus/releases/download/v2.1.0/prometheus-2.1.0.linux-amd64.tar.gz
```

- Extract the Prometheus archive :

```sh
tar -xf prometheus-2.1.0.linux-amd64.tar.gz
```

- Move the binaries to /usr/local/bin:

```sh
sudo mv prometheus-2.1.0.linux-amd64/prometheus prometheus-2.1.0.linux-amd64/promtool /usr/local/bin
```

- Now, we need to create directories for configuration files and other prometheus data.

```sh
sudo mkdir /etc/prometheus /var/lib/prometheus
```

- Then, we move the configuration files to the directory we made previously:

```sh
sudo mv prometheus-2.1.0.linux-amd64/consoles prometheus-2.1.0.linux-amd64/console_libraries /etc/prometheus
```

- Finally, we can delete the leftover files as we do not need them any more:

```sh
rm -r prometheus-2.1.0.linux-amd64*
```

**Configuring Prometheus--->**

After having installed Prometheus, we have to configure Prometheus to let it know about the HTTP endpoints it should monitor. Prometheus uses the YAML format for its configuration.

- We will use /etc/prometheus/prometheus.yml as our configuration file

-------------------------------------
```sh
global:
  scrape_interval: 10s

scrape_configs:
  - job_name: 'prometheus_metrics'
    scrape_interval: 5s
    static_configs:
      - targets: ['localhost:9090']
  - job_name: 'node_exporter_metrics'
    scrape_interval: 5s
    static_configs:
      - targets: ['localhost:9100','prometheus-target-1:9100','prometheus-target-2:9100']
```
-------------------------------------

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/47dbc6c9-2306-4f37-946f-aa9a0a1e6694)

In this file, we have defined a default scraping interval of 10 seconds. We have also define two sources of metrics, named prometheus_metrics and node_exporter_metrics. For both of them, we have set the scraping interval to 5 seconds, overriding the default. Then, we have specified the locations where these metrics will be available. Prometheus uses port 9090 and node_exporter uses port 9100 to provide their metrics.

- Finally, we will also change the ownership of files that Prometheus will use:

```sh
sudo useradd -rs /bin/false prometheus
sudo chown -R prometheus: /etc/prometheus /var/lib/prometheus
```

- Then, we will create a systemd unit file in /etc/systemd/system/prometheus.service with the following contents :

-------------------------------------
```sh
[Unit]
Description=Prometheus
After=network.target

[Service]
User=prometheus
Group=prometheus
Type=simple
ExecStart=/usr/local/bin/prometheus \
    --config.file /etc/prometheus/prometheus.yml \
    --storage.tsdb.path /var/lib/prometheus/ \
    --web.console.templates=/etc/prometheus/consoles \
    --web.console.libraries=/etc/prometheus/console_libraries

[Install]
WantedBy=multi-user.target
```
-------------------------------------

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/a23682fb-61e9-4915-9782-976da95579f7)

- Finally, we will reload systemd:

```sh
sudo systemctl daemon-reload
sudo systemctl enable prometheus
sudo systemctl start prometheus
```

- Prometheus provides a web UI for running basic queries located at http://<your_server_IP>:9090/. This is how it looks like in a web browser:

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/a43804cf-5d8a-46f8-b5ee-5b638817d5f1)

6. Configure the data source settings, including the AWS region and access credentials. Make sure to provide the necessary permissions to access the EC2 instances' metrics and data.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/809d9e42-6a39-4a76-9e14-eceaabc56b57)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/bdd7a229-9eb7-43b8-a8b5-f8ae1ca16c9b)

7. Test the data source connection to ensure everything is set up correctly.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/ed0403ab-3c49-4f03-8f82-80125e66253a)

Congratulations! You have successfully configured the data sources to connect with your EC2 instances. Now it's time to create dashboards and visualize the data.

## Step 3: Create Dashboards

Dashboards in Grafana are where you can design and visualize your data in a way that suits your monitoring needs. You can create multiple dashboards and customize them according to your preferences. Let's create a basic dashboard to monitor our EC2 instances.

1. In the Grafana web interface, click on the "Create" button and select "Dashboard."

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/f069c303-2a41-4275-bea5-dcdaabc6000f)

2. Choose the visualization type you want to use, such as graphs, tables, or charts.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/7859393d-7abf-47d9-96c5-64ada3e9e05e)

Before going further please check prometheus configuration for targets:

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/8ca5f166-ddda-4997-a16d-a61b1e955be5)

3. Configure the metrics and data you want to monitor. You can select specific EC2 instance metrics, such as CPU usage, memory usage, disk utilization, and network traffic.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/16181c5c-bd7d-4ba4-bf2e-41186ad360aa)

4. Customize the dashboard layout, add panels, and arrange them as needed.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/75a01591-4dae-4f81-927a-cccd314fed6c)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/0682745e-a25a-415a-9a00-5f136b54c421)

5. Save the dashboard and give it a meaningful name.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/f9fe3395-ad6c-4493-bbad-f90e6b39b520)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/3a566c4f-3dc6-4bcf-add3-a5d75284c896)

Once you have created your dashboard, Grafana will start fetching data from your EC2 instances and display it in real-time. You can explore various visualization options and features provided by Grafana to enhance your monitoring experience.

### You are done with it!

Connecting EC2 instances with Grafana opens up a world of possibilities for monitoring and analyzing your server's performance. By following the steps outlined in this blog post, you can establish a seamless connection between your Linux EC2 instances and Grafana. This connection allows you to gain valuable insights into the different components of your servers, enabling you to make informed decisions and take necessary actions to optimize their performance.

Remember, monitoring is a continuous process, and Grafana provides a powerful platform to track your server's health and performance over time. Keep exploring Grafana's features, experiment with different metrics, and refine your dashboards to meet your specific requirements.

**Happy Learning and Happy Monitoring :)**

# Day74 task is complete!
