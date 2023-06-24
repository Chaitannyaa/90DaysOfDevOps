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

2. To add a repository for stable releases, run the following command:

```sh
echo "deb [signed-by=/usr/share/keyrings/grafana.key] https://apt.grafana.com stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
```

3. To add a repository for beta releases, run the following command:

```sh
echo "deb [signed-by=/usr/share/keyrings/grafana.key] https://apt.grafana.com beta main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
```

4. Run the following command to update the list of available packages:

```sh
sudo apt-get update
```

5. To install Grafana OSS, run the following command:

```sh
sudo apt-get install grafana
```

**You should see a message indicating that Grafana is active and running.**

## Accessing Grafana Web Interface

1. Open a web browser and enter the following URL:

```sh
http://public-ip:3000
```

**Replace `public-ip` with the public IP address of your EC2 instance.**

3. You should now see the Grafana login page. Enter the default credentials:

   - Username: admin

   - Password: admin

4. After logging in, Grafana will prompt you to change the password. Follow the instructions to set a new password.

6. Congratulations! You have successfully set up Grafana on your Ubuntu EC2 instance. Now you can start exploring its features, creating dashboards, and visualizing your metrics data.

**Happy monitoring with Grafana!**

# Day 73 task is complete!
