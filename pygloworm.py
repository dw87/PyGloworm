#! /usr/bin/python
#
print "Content-Type: text/html\n"

from pyglow import PyGlow
from time import sleep
from datetime import datetime
import random

pyglow = PyGlow()
pyglow.all(0)

random.seed(datetime.now().time())

randomLightsInt = random.randint(0,262143)

randomLightBits = "{0:b}".format(randomLightsInt)

i = 1
leds = []
for c in randomLightBits:
	if (int(c)*i>0):
		leds.append(i)
	i=i+1

pyglow.set_leds(leds, 50)
pyglow.update_leds()
