#! /usr/bin/python
#
print "Content-Type: text/html\n"

from pyglow import PyGlow
from time import sleep

pyglow = PyGlow()
pyglow.all(0)

max_brightness = 255 #(0 == off, 75 == bright, 255 == blinding!)

#Pulse all LEDs up to max_brightness and back to off
for x in range (0, max_brightness):
	pyglow.all(x)
	sleep(0.001)

for x in range (max_brightness, 0, -1):
	pyglow.all(x)
	sleep(0.001)

pyglow.all(0)
