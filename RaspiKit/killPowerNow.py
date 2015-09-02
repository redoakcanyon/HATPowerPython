import wiringpi2 as gpio
import time
import os

#
# pulse gpio28 hi/lo until the power dies

os.system('logger killPower:going down')

#
# define some constants
#
INPUT = 0
OUTPUT = 1
INT_EDGE_FALLING = 1
PUD_UP = 2
# 
# select correct PB version
#
# OFF = 28 # original PB version
OFF = 12 # 40 pin map for HAT board
# OFF = 18 # 26 pin map for HAT board
#
# use Broadcom GPIO pin scheme
#
gpio.wiringPiSetupGpio()

# setup pin OFF as OUTPUT
#
gpio.pinMode(OFF,OUTPUT)

for x in xrange(1, 10):
	gpio.digitalWrite(OFF,1)
	time.sleep(.1)
	gpio.digitalWrite(OFF,0)
	time.sleep(.1)

