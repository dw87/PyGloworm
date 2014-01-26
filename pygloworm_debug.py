#! /usr/bin/python
#
print "Content-Type: text/html\n\n"
print '<!DOCTYPE html>'

from pyglow import PyGlow
from time import sleep
from datetime import datetime
import random

pyglow = PyGlow()
pyglow.all(0)

random.seed(datetime.now().time())

randomLightsInt = random.randint(0,262143)

randomLightBits = "{0:b}".format(randomLightsInt)

#print randomLightBits

i = 1
leds = []
for c in randomLightBits:
	print c
	if (int(c)*i>0):
		leds.append(i)
	i=i+1

pyglow.set_leds(leds, 50)
pyglow.update_leds()
#print i

print '<html>'
print '<head><meta content="text/html; charset=UTF-8" /></head>'
print '<body>Done</body>'
print '</html>'
