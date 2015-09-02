import wiringpi2 as gpio
import time
import os

# choose correct GPIO mapping
# 40 pin mapping
# D1m = 20
# D2m = 26

# 26 pin mapping
D1m = 24
D2m = 23

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

# setup pins as input with pull-up
#
gpio.pinMode(D1m,INPUT)
gpio.pullUpDnControl(D1m,PUD_UP)
gpio.pinMode(D2m,INPUT)
gpio.pullUpDnControl(D2m,PUD_UP)

#
# D2m is PowerApplied, D1m is Charging
#
#if gpio.digitalRead(D2m):
#	os.system('logger chargeStatus:PowerApplied is false')
#else:
#	os.system('logger chargeStatus:PowerApplied is true')
#if gpio.digitalRead(D1m):
#	os.system('logger chargeStatus:Charging is false')
#else:
#	os.system('logger chargeStatus:Charging is true')
#
# poll for REQ_OFFb going low
#
n = 0
while (1):
	if gpio.digitalRead(D2m):
		print( "seq %6i PowerApplied is false" % n)
	else:
		print( "seq %6i PowerApplied is true" % n)
	if gpio.digitalRead(D1m):
		print "           Charging is false"
	else:
		print "           Charging is true"
	n = n + 1
	time.sleep(10)
