# Day 75 - Sending Docker Log to Grafana

## Pre requisites:

1. [Grafana](https://90daysofdevopschallenge.hashnode.dev/day73-90daysofdevops-challenge-tws) server up and running with data source  [Prometheus](https://90daysofdevopschallenge.hashnode.dev/day74-90daysofdevops-challenge-tws) configured.

2. One Linux instance to serve as a Docker Engine.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/8d31f781-cbca-4362-85f5-96a6a4c0c659)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/aaefa210-9904-4ab3-bf3a-9ed40cfceb59)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/399c48df-30df-4230-b2f2-bc9b18e293a6)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/497df76e-4c5a-4bc1-9a15-d4c3d4534f16)

## Let's get started--->

- Install *Docker* and start docker service on your Linux EC2 instance (Ubuntu 20.04 LTS).

```sh
sudo apt install docker.io -y
sudo usermod -aG docker $USER
sudo reboot
sudo systemctl enable docker
sudo systemctl status docker
```

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/bc852fde-914c-41b8-a9c6-0e1574f92cc8)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/38156016-56c2-4cdc-962d-6a6890b0b8b5)

- Create 2 Docker containers and run any basic application on those containers.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/1a237307-6907-40cc-80e3-bd1bc7ad32d4)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/1f34691b-768d-49b1-bd9e-67db4f98e312)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/0a7d5961-2c2b-4f54-b8c3-b1a22cecba70)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/8e7e1aee-f034-4945-a749-5bbd4f1513f1)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/36e19d11-aeb4-472b-bc9b-7745dedf9343)

- Now intregrate the docker containers and share the real time logs with Grafana.

**Add your "Target machine details" to this prometheus configuration file**
![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/b07547ef-522d-41cc-91d1-160c62b3e931)




- Check the logs or docker container name on Grafana UI.


## Happy Learning :)

# Day 75 task is complete!
