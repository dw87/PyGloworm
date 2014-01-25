#! /usr/bin/python
#
#Config the output as HTML, to stop the browser serving the
#response as a .py file download.
print "Content-Type: text/html\n\n"
print '<!DOCTYPE html>'

# Import the PyGlow Module (stored in /usr/lib/python2.7)
from pyglow import PyGlow
from time import sleep
from datetime import datetime
import random

#Setup new PyGlow instance
pyglow = PyGlow()
#Turn off all LEDs
pyglow.all(0)

random.seed(datetime.now().time())

#Generate random (maximum of 18 bit) number
randomLightsInt = random.randint(0,262143)

#Get the 18 bits, 1 for each PyGlow LED
randomLightBits = "{0:b}".format(randomLightsInt)

#Display the 18 bits
print randomLightBits

i = 0
leds = []
#Loop for each bit, if value is 1, add to LED list
for c in randomLightBits:
	i = i+1
	print c
	if (int(c)*i>0):
		print i
		leds.append(i)

#Set brightness of LEDs in list to 50 (0/Low - 255/Very very bright)
pyglow.set_leds(leds, 50)
#Turn on the listed LEDs
pyglow.update_leds()
print i

#For debugging, output a barebones HTML page
print '<html>'
print '<head><meta content="text/html; charset=UTF-8" /></head>'
print '<body>Done!</body>'
print '</html>'
