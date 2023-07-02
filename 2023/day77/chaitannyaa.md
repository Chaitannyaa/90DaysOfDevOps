# Day 77 Alerting

Grafana Alerting allows you to learn about problems in your systems moments after they occur. Create, manage, and take action on your alerts in a single, consolidated view, and improve your team’s ability to identify and resolve issues quickly.

Grafana Alerting is available for Grafana OSS, Grafana Enterprise, or Grafana Cloud. With Mimir and Loki alert rules you can run alert expressions closer to your data and at massive scale, all managed by the Grafana UI you are already familiar with.

## Setup Grafana cloud

- Click Here [>>>](https://grafana.com/products/cloud/)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/56b2b892-2135-4047-bd67-5dedb63cc4d2)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/48464aa4-451e-42f6-92d1-7340986dc71b)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/5ab89c02-b868-48b8-817f-f9a70394c7f7)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/ccdbb5c3-f9e5-49a2-b474-f12024b46c0a)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/8483c70d-fa59-4fbd-8d1e-464e300b1208)

## Setup sample alerting 

**I have Grafana OSS configured for this practical--->**

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/24d87814-b0b1-4b26-b58a-9398f52e93ee)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/591f975e-d63b-450c-9f70-df763e993782)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/4801d604-97b6-489c-9a27-7876c4a93e39)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/b95287fe-5a0f-488c-a505-f92ac7956d38)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/4e37efc4-f492-4bea-b893-c5624a0e0062)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/8bbc8916-0f98-4b7f-9148-b41c1bf8eee1)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/f3ecfcf5-ca80-437a-81c0-63a562584073)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/203649c1-a33c-48aa-9c86-63cf3b275ca3)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/2b583b2b-26ed-4409-abf6-99283583ee43)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/91527ad2-2aae-4432-a24f-e252d2f1ebcc)

**You  must configure your grafana server for SMTP section of **

### Locate the `grafana.ini` configuration file. By default, it is found in the `/etc/grafana` directory on Linux systems or the installation directory on Windows.

```sh
[smtp]
enabled = true
host = smtp.example.com:25
user = your_email@example.com
password = your_email_password
```
![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/f100d95f-a471-4067-b5ac-c3444edb9e56)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/48c80e32-3671-43d3-834b-3b9ca78fba98)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/59c29f1f-5f80-49d0-b0ec-4b2abefc56c1)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/e1987fca-25a8-4b45-9f18-08efffe088ef)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/f99cde69-61dc-4a74-a5f4-2e083338e407)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/67a214fb-8cf3-434a-84ba-dc5f508e34d8)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/960e4a33-176b-472a-8e5a-958b66d5ffc2)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/6d6cc2ea-2136-40d2-8ea4-0661a6c16f59)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/cf8db6a3-51c6-4da8-ae83-9675d36c75c7)

That's how you get alerts on your email!

# Day77 task is complete!















