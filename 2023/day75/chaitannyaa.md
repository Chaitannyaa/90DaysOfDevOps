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

- Check the logs or docker container name on Grafana UI.


## Happy Learning :)

# Day 75 task is complete!
