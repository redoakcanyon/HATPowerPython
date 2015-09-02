import wiringpi2 as gpio
import time
import os

# choose correct GPIO mapping
# REQ_OFFb = 30 # Rev 1 PB mapping
REQ_OFFb = 5 # 40 pin HAT board mapping
# REQ_OFFb = 2 # 28 pin HAT board mapping

def init_shutdown():
	os.system('logger monitorPS:io REQ_OFFb asserted')
	os.system('halt')
	return True

#
# define some constants
#
INPUT = 0
INT_EDGE_FALLING = 1
PUD_UP = 2
#
# use Broadcom GPIO pin scheme
#
gpio.wiringPiSetupGpio()

# setup pins as inut with pull-up
#
gpio.pinMode(REQ_OFFb,INPUT)
gpio.pullUpDnControl(REQ_OFFb,PUD_UP)

#
# get state of REQ_OFFb
#
if gpio.digitalRead(REQ_OFFb):
	os.system('logger monitorPS:REQ_OFF* is high')
else:
	os.system('logger monitorPS:REQ_OFF* is low')
#
# register the interrupt handler
#
# poll for REQ_OFFb going low
#
while gpio.digitalRead(REQ_OFFb):
	time.sleep(.200)

init_shutdown()

