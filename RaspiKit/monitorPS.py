# measure the battery voltage
#
# port gpio18 is cs*
# port gpio27 is u/d control
# comparator output is PGOOD pin on P5, # port gpio29
#
# set GPIO29 to input, 18 and 27 to output
#
# rev 1 PB 
#CSb = 18   
#UDb = 27
#PGOOD = 29

# 40 pin HAT map
CSb = 6
UDb = 16
PGOOD = 13

# 26 pin HAT map
#CSb = 17
#UDb = 25
#PGOOD = 27

import wiringpi2 as gpio
import time
import os
def railVarRes():
	# up mode: u/d -> 1
	gpio.digitalWrite(UDb,1)
	# cs* -> 0
	gpio.digitalWrite(CSb,0)
	#
	# u/d 64 times to get it to the rail
	#
	for x in range(0, 63):
		gpio.digitalWrite(UDb,0)
		gpio.digitalWrite(UDb,1)
	# cs* -> 1
	gpio.digitalWrite(CSb,1)
	return True

def batleveltopct(batLevel):
	
	powermap=[
		100, 100, 100, 100, 100, 100, 96,  90,  84,  78, 
		71,  63,  54,  41,  24,  14,  9,   7,   5,   4,
		3,   1,   1,   0,   0,   0,   0,   0,   0,   0,   
		0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   
		0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   
		0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   
		0,   0,   0,   0
		]

	return powermap[batLevel]

def measureBat():
	railVarRes()
	#
	# down mode: u/d -> 0
	#
	gpio.digitalWrite(UDb,0)
	# cs* -> 0
	gpio.digitalWrite(CSb,0)
	batLevel = 63
	comp =  gpio.digitalRead(PGOOD)
	while (comp == 1 and batLevel > 0):
		gpio.digitalWrite(UDb,0)
		gpio.digitalWrite(UDb,1)
		comp =  gpio.digitalRead(PGOOD)
		batLevel = batLevel -1 

	# cs* -> 1
	gpio.digitalWrite(CSb,1)
	pct = batleveltopct(batLevel)
	print batLevel,pct
	return pct
		
def initPorts():
	#
	# define constants
	#
	INPUT = 0
	OUTPUT = 1
	PUD_UP = 2
	#
	# use Broadcom GPIO pin scheme
	#
	gpio.wiringPiSetupGpio()
	
	# comparator output is PGOOD  - needs pull-up
	#
	gpio.pinMode(PGOOD,INPUT)
	gpio.pullUpDnControl(PGOOD,PUD_UP)
	#
	#
	gpio.pinMode(CSb,OUTPUT)
	gpio.pinMode(UDb,OUTPUT)
	#
	# cs* -> 1 to deselect; USb is don't care
	#
	gpio.digitalWrite(CSb,1)
	return

def writeBatLevel(batLevel):
	os.system("echo \"" + str(batLevel) + "\" > /var/battery/level")

def shutdown():
	os.system("halt")

initPorts()
pct = measureBat()
while (pct > 0):
	pct = measureBat()
	writeBatLevel(pct)
	time.sleep(30)

# after waiting the final 30 seconds after battery hits 0, then shutdown
shutdown()
