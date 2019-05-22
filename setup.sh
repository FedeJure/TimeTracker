#!/bin/sh
sudo apt-get update
sudo apt-get install python-pip -y
sudo apt-get install python-tk -y
pip install -r requirements.txt

sudo ln timetracker.sh /usr/local/bin/timetracker
#etc.