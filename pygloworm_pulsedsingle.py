#! /usr/bin/python
#
print "Content-Type: text/html\n"

from pyglow import PyGlow
from time import sleep

pyglow = PyGlow()
pyglow.all(0)

max_brightness = 255 #(0 == off, 75 == bright, 255 == blinding!)
single_led = 2 #1-18

for x in range (0, max_brightness):
	pyglow.led(single_led, x)
	sleep(0.001)

for x in range (max_brightness, 0, -1):
	pyglow.led(single_led, x)
	sleep(0.001)

pyglow.all(0)
