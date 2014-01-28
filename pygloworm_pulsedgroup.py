#! /usr/bin/python
#
print "Content-Type: text/html\n"

from pyglow import PyGlow
from time import sleep

pyglow = PyGlow()
pyglow.all(0)

max_brightness = 255 #(0 == off, 75 == bright, 255 == blinding!)
#Create a group of LEDS to light together, any combination of 1-18 LEDs.
leds = [1,3,5,7,9,11,13,15,17] #[1-18]

for x in range (0, max_brightness):
	pyglow.set_leds(leds, x)
	pyglow.update_leds()
	sleep(0.001)

for x in range (max_brightness, 0, -1):
	pyglow.set_leds(leds, x)
	pyglow.update_leds()
	sleep(0.001)

pyglow.all(0)
