#!/bin/sh
cd RaspiKit
#
# copy the files to init.d
#
sudo cp monitorP* /etc/init.d
sudo cp killPower* /etc/init.d

#Install the scripts into the startup/shutdown sequence. update-rc.d will issue some warnings, but don't worry about them.

sudo update-rc.d killPower defaults
sudo update-rc.d monitorPS defaults
sudo update-rc.d monitorPB defaults


# The python scripts need the wiringpi2 class.  Installe it as in (from http://raspi.tv/how-to-install-wiringpi2-for-python-on-the-raspberry-pi):
# installing python-pip takes a while
sudo apt-get install python-dev python-pip 
sudo pip install wiringpi2
