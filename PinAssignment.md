This file documents the GPIO connector pins for the signals that control the power functions.  

The HAT module has the pins allocated in the "new" portion of the 40 pin connector as follows:

HAT Module:

Signal	GPIO 	Connector Pin #

REQ_OFF	GPIO5	29
OFF	GPIO12	32
PGOOD	GPIO13	33
CS*	GPIO6	31
U/D*	GPIO16	36
D2-	GPIO26	37
D1-	GPIO20	38

To use the Power Board on the older Rev A and Rev B Rasperry Pi's, these connections are 
recommended as they have the correct initial pullup/down modes.  

Note that jumper wires from the connector pins listed above must to those listed below must be
installed.

HAT Module wiring for REV B 26 pin connector

Signal	GPIO	Connector Pin #

REQ_OFF	GPIO2	3
OFF	GPIO18	12
PGOOD	GPIO27	13
CS*	GPIO17	11
U/D*	GPIO25	22
D2-	GPIO23	16
D1-	GPIO24	18
