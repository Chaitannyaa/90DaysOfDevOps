# Day 73 - Setting Up Grafana on Ubuntu EC2 Instance 🔥

Today, we will go through the process of setting up Grafana in your local environment on an Ubuntu EC2 instance. Grafana is a powerful open-source metric analytics and visualization suite that enables you to query, visualize, and gain insights from your metrics data. So let's dive in and get Grafana up and running!

## Installing Grafana

### Steps to install Grafana from the APT repository:

1. To install required packages and download the Grafana repository signing key, run the following commands:

```sh
sudo apt-get install -y apt-transport-https
sudo apt-get install -y software-properties-common wget
sudo wget -q -O /usr/share/keyrings/grafana.key https://apt.grafana.com/gpg.key
```
![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/4fbbc530-5a9f-407d-a127-576d14eb15a6)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/63c0c2cf-5de9-4b35-8543-cf403328084c)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/542f82c0-9ee7-4abe-af06-f45ee1cac706)

2. To add a repository for stable releases, run the following command:

```sh
echo "deb [signed-by=/usr/share/keyrings/grafana.key] https://apt.grafana.com stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
```

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/8bc2952c-a449-42e1-827c-ab04b83000d3)

3. To add a repository for beta releases, run the following command:

```sh
echo "deb [signed-by=/usr/share/keyrings/grafana.key] https://apt.grafana.com beta main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
```

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/af3592da-f39b-48e8-a0c0-939851ae0abf)

4. Run the following command to update the list of available packages:

```sh
sudo apt-get update
```

5. To install Grafana OSS, run the following command:

```sh
sudo apt-get install grafana
```

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/959c8889-580e-427e-bc21-f8e9dda26a5e)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/27808505-3a95-4da0-a2ef-dbfc5df0fdfe)

6. Start Grafana Server and enable it.

```sh
sudo systemctl start grafana-server
sudo systemctl enable grafana-server
```
![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/bd608c92-7306-47d0-bee5-81f4c1e95910)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/08dd7ecd-a693-470e-8524-1064e55c68e4)

**You should see a message indicating that Grafana is active and running.**

## Accessing Grafana Web Interface

1. Open a web browser and enter the following URL:

```sh
http://public-ip:3000
```
![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/affbdcf3-f812-4374-9286-25850b765db6)

**Replace `public-ip` with the public IP address of your EC2 instance.**

3. You should now see the Grafana login page. Enter the default credentials:

   - Username: admin

   - Password: admin

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/82559fc9-f2d9-4ada-a32f-cacca4f2494d)

4. After logging in, Grafana will prompt you to change the password. Follow the instructions to set a new password.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/bc19e866-20dc-402c-807b-8be6f2361ab8)

6. Congratulations! You have successfully set up Grafana on your Ubuntu EC2 instance. Now you can start exploring its features, creating dashboards, and visualizing your metrics data.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/95d725ba-6b25-47a2-acba-86bde29c3155)

**Happy monitoring with Grafana!**

# Day 73 task is complete!
