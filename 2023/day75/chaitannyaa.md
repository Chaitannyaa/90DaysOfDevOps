# Day 75 - Sending Docker Log to Grafana

## Pre requisites:

1. [Grafana](https://90daysofdevopschallenge.hashnode.dev/day73-90daysofdevops-challenge-tws) server up and running with data source  [Prometheus](https://90daysofdevopschallenge.hashnode.dev/day74-90daysofdevops-challenge-tws) configured.

2. One Linux instance to serve as a Docker Engine.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/8d31f781-cbca-4362-85f5-96a6a4c0c659)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/aaefa210-9904-4ab3-bf3a-9ed40cfceb59)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/399c48df-30df-4230-b2f2-bc9b18e293a6)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/497df76e-4c5a-4bc1-9a15-d4c3d4534f16)

## Let's get started--->

- Install *Docker* and start docker service on your Linux EC2 instance (Ubuntu 20.04 LTS) and configure docker to send metrices to prometheus.

```sh
sudo apt install docker.io -y
sudo usermod -aG docker $USER
sudo reboot
sudo systemctl enable docker
sudo systemctl status docker
```

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/bc852fde-914c-41b8-a9c6-0e1574f92cc8)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/38156016-56c2-4cdc-962d-6a6890b0b8b5)

**Create this file  "/etc/docker/daemon.json" and Add below contents**

```sh
{
    "metrics-addr" : "0.0.0.0:9323",
    "experimental" : true
}
```
![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/a010d5cc-08b3-4330-af87-c80856b17ab5)

- Create 2 Docker containers and run any basic application on those containers.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/1a237307-6907-40cc-80e3-bd1bc7ad32d4)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/1f34691b-768d-49b1-bd9e-67db4f98e312)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/0a7d5961-2c2b-4f54-b8c3-b1a22cecba70)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/8e7e1aee-f034-4945-a749-5bbd4f1513f1)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/36e19d11-aeb4-472b-bc9b-7745dedf9343)

- Now intregrate the docker containers and share the real time logs with Grafana.

**Add your "Target machine details" to this prometheus configuration file**

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/8eefc7be-6527-4d33-9599-9db8b0b2b8ac)

**Check your prometheus server's Target section for updates**

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/cad36c51-2f62-49bf-8578-287a1eb70f41)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/325f14b8-dbb5-4c19-9797-23890efdacbb)

**Create dashboard for your Docker Engine to monitor containers**

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/e4755c89-1615-4ca3-b4e3-d60839ea11ef)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/56495a25-8f11-4bf8-8e22-970553b8533c)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/1d048b9d-c292-413a-a072-7a9f4367b370)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/4c879b95-a8c1-4bb4-ac5e-ac4b7d310428)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/3b9e26bb-7509-48c2-a9ca-8fb366f9af82)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/c89de110-7c80-4565-8f94-1cd6ff8a8856)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/6896a518-4ecf-4a6a-b144-f4cc1bbb0572)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/7c4de615-a259-40a6-ba1a-30308abf663b)

## Check the logs or docker container name on Grafana UI.

To retrive more detailed docker container logs you need another exporter like **cadvisor** to send data to prometheus

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/d45ebc4d-9c74-4f56-840c-94492feeb1ec)

**Let's install **cadvisor** first on your target servers--->**

```sh
sudo apt install cadvisor
```
![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/66ef87e0-5aff-4a88-8340-3b58a85af834)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/f7f03cfc-e264-46b0-a25c-62776190fb9c)

**Configure your Prometheus to scrap data from cadvisor's metrics--->**

```sh
sudo vim /etc/prometheus/prometheus.yml
```

**Add below data in above prometheus.yml file**

```sh
global:
  scrape_interval: 10s

scrape_configs:
  - job_name: 'prometheus_metrics'
    scrape_interval: 5s
    static_configs:
      - targets: ['3.237.177.101:9090']

  - job_name: 'Cadvisor'
    scrape_interval: 5s
    static_configs:
      - targets: ['44.211.96.219:8080']
```

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/95e26221-a9c3-4d57-a294-3e60cd1f14bf)

**Check prometheus targets updated with cadvisor**

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/3bade320-19bf-4c9a-9e95-207d72690175)

**Now let's build our dashboard to see running container names--->**

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/95a80c06-1076-4097-bb2b-974539c8d618)

### Create a new panel and use "container_tasks_state" metrics

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/1da271c3-3b4e-46be-a76f-0b5d1a358e0b)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/6df8ca75-837c-4e5a-8d2f-cbf4ed3df50f)

**Give proper visualization to the table with some background colour**

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/086d11d3-ba7c-4881-9662-804202634374)

**Add some metrics check for Prometheus Server and Docker host server memory ustilization**

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/b32f194d-7940-4a17-8386-e7d38322968e)

### Arrange layout of dashboard as per your ease to monitor--->

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/eac94ab7-bcec-489a-b1c2-53bff2fca8ea)

## Happy Learning :)

# Day 75 task is complete!
