#!/bin/sh
cd RaspiKit
#
# copy the files to init.d
#
sudo cp monitorP* /etc/init.d
sudo cp killPower* /etc/init.d

#Install the scripts into the startup/shutdown sequence. update-rc.d will issue some warnings, but don't worry about them.

sudo update-rc.d killPower default
sudo update-rc.d monitorPS default
sudo update-rc.d monitorPB default


# The python scripts need the wiringpi2 class.  Installe it as in (from http://raspi.tv/how-to-install-wiringpi2-for-python-on-the-raspberry-pi):

sudo apt-get install python-dev python-pip (takes a while)
sudo pip install wiringpi2
