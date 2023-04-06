#!/bin/bash

sudo useradd -m User_1
sudo useradd -m User_2

cat /etc/passwd | grep User_*

