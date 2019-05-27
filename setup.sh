#!/bin/sh
sudo apt-get update
sudo apt-get install python-pip -y
sudo apt-get install python-tk -y
pip install -r requirements.txt

echo "python $(pwd)/src/main.py" > timetracker.sh
chmod +x timetracker.sh
sudo ln timetracker.sh /usr/bin/timetracker
#etc.