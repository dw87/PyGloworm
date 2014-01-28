#! /usr/bin/python
#
print "Content-Type: text/html\n"

from pyglow import PyGlow
from time import sleep

pyglow = PyGlow()
pyglow.all(0)

max_brightness = 255 #(0 == off, 75 == bright, 255 == blinding!)
# Select which single colour group you want to light (will light all 3 of that colour)
colour = "white" #"red", "orange", "yellow", "green", "blue"

for x in range (0, max_brightness):
	pyglow.color("white", x)
	sleep(0.001)

for x in range (max_brightness, 0, -1):
	pyglow.color("white", x)
	sleep(0.001)

pyglow.all(0)
