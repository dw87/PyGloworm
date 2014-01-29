## PyGloworm

PyGloworm is a small Python project, hosted on a Raspberry Pi webserver that uses the PiGlow addon for the Raspberry Pi 
(by Pimoroni, http://shop.pimoroni.com/products/piglow) to provide a visual notification of visitor activity to a website.  
It uses Ben Lebherz's PyGlow Python module (https://github.com/benleb/PyGlow) to control the PiGlow.  

## Features
 - Generates and lights a random configuration of PiGlow LEDs on each activation.
 - Outputs (Prints) a valid HTML signature for correct web browser intepretation.
 - Can be run locally for testing, and served by a Raspberry Pi webserver.

## Files
 - pygloworm.py - 	Simplified code to update the LEDs to a new random pattern when run. Outputs the minimum
			HTML needed allowing web browsers to see it as a valid web page.  
 - pygloworm_debug.py - Debug code that displays the random generated bits used to configure the LEDs
			and a simple HTML page to confirm script has run. Works locally on command line
			and remotely when served by a Raspberry Pi webserver.  
### Extra Examples
 - pygloworm_pulsedsingle.py - Pulses a single LED to maximum brightness and back to off.
 - pygloworm_pulsedcolour.py - Pulses a single colour group of LEDs to maximum brightness and back to off.
 - pygloworm_pulsedgroup.py - Pulses a configurable group of LEDs to maximum brightness and back to off.
 - pygloworm_pulsedall.py - Pulses all LEDs to maximum brightness and back to off.  

## Requirements

    sudo apt-get install python-smbus
    sudo apt-get install lighttpd

## Setup Instructions

All instructions are based on a default install of Raspbian Wheezy logged in as the 'pi' user.  
Although the project is simple, it requires a number of specific things to be configured on the Raspberry Pi.
This README may be long, but please stick with it.  

### PiGlow Preparation

Follow the instructions provided by Pimoroni on how to setup your Raspberry Pi to use the PiGlow, found here:
https://github.com/pimoroni/piglow#setting-up-your-raspberry-pi

### PyGlow Module

You need to download Ben Lebherz's pyglow.py file somewhere your Python code can access it.  
I have stored this in /usr/lib/python2.7 so all projects I develop that use Python 2.7 can use it.  

    sudo wget https://raw.github.com/benleb/PyGlow/master/pyglow.py -P /usr/lib/python2.7

If you are unsure, or have a different Python configuration, you can add this file to each directory 
when you write a Python project that will use it.  

### I2C Permissions

By default any Python project that uses I2C (or other GPIO), including PyGlow, must be run using sudo.  
This is a problem when these Python scripts are run by a web server.  When the web server runs these scripts, 
it will fail when it reaches the I2C interaction, as it does not have the correct permissions.  

To fix this, add a new user to the i2c group: 
    
    sudo adduser pi i2c

Also, create or edit the file /etc/udev/rules.d/99-i2c.rules and add the line: 
    
    SUBSYSTEM=="i2c-dev", MODE="0666"

When finished, reboot your Raspberry Pi.  
    
    sudo reboot

### Static IP

Before setting up a web server on the Raspberry Pi, you should configure a static IP. This makes it easier to route 
traffic from outside your local network through your router to your Raspberry Pi.  

There are many guides out there if you are unsure how to do this.  
A good one is here: http://raspberryshake.com/raspberry-pistatic-ip-address/

If you know your local network details and the IP address you want to give to the Pi, edit the file /etc/network/interfaces.  
A typical configuration is shown below: 

    sudo nano /etc/network/interfaces

Change

    iface eth0 inet dhcp
To

    iface eth0 inet static
    address 192.168.0.###
    netmask 255.255.255.0
    network 192.168.0.0
    broadcast 192.168.0.255
    gateway 192.168.0.1

When finished, reboot your Raspberry Pi.  

    sudo reboot

Then configure Port Forwarding on your router, to forward all incoming connections on Port 80 (HTTP traffic) to the static IP 
address you have just configured.  If you want SSH access to your Raspberry Pi from outside your local network, also forward Port 22.  

To test the web server configuration, either browse to your external IP.  Use a service like http://myip.dnsdynamic.com to find 
this out.  If the configuration is correct, you will see the Lighttpd example index.  

If your ISP provides only dynamic IP address, your external IP address may change.  If you do not know the current external IP
for your Raspberry Pi, you will not be able to browse to it on the internet.  

Use Dynamic DNS if you want to route a friendly fixed URL to your Raspberry Pi.  There are many services that provide this 
for free, either with their own domains, or with your own.  I am using http://dnsexit.com with my own domain for free.  There are
utilities that can be installed on the Raspberry Pi to monitor your external IP and update the Dynamic DNS service if this changes.  

### Web server Configuration

You will need to install and configure a Web Server on your Raspberry Pi.  I have chosen Lighttpd (http://lighttpd.net), 
a lightweight webserver often recommended for use on the Raspberry Pi.  

Once installed, you need to configure the web server to enable Python CGI support, so it will run Python scripts hosted 
on the Raspberry Pi in the same way as it will PHP.  

You will need to edit the Lighttpd config file to enable CGI and allow it to recognise Python scripts.  

    sudo nano /etc/lighttpd/lighttpd.conf

Edit the server.modules section to include or uncomment "mod_cgi": 

    server.modules = (
    	"mod_access",
    	"mod_alias",
    	"mod_compress",
    	"mod_redirect",
    	"mod_cgi",
    	#"mod_rewrite",
    )

At the end of the file, add this section so Lighttpd will recognize Python scripts in the 'www' directory.  

    $HTTP["url"] =~ "^/" {
    	cgi.assign = (".py" => "/usr/bin/python")
    }

Finally alter the permissions of the www directory (by default /var/www).

    sudo chown www-data:www-data /var/www
    sudo chmod 775 /var/www
    sudo usermod -a -G www-data pi

When finished, restart the Lighttpd service.

    sudo service lighttpd restart

See more information on configuration a Raspberry Pi web server at: 
http://mike632t.wordpresss.com/2013/09/21/installing-lighttpd-with-python-cgi-support/

http://raspberrypi-spy.co.uk/2013/06/how-to-setup-a-web-server-on-your-raspberry-pi/

## Installing Pygloworm

With your Raspberry Pi configured as a web server, and accessible on the internet, download Pygloworm.py to
your www directory.  

    sudo wget https://raw.github.com/dw87/PyGloworm/master/pygloworm.py -P /var/www

To test if this has worked correctly, browse to it in a web browser.  
e.g http://your-raspberry-pi.com/pygloworm.py

Your browser should display a blank page, and the lights on your PiGlow should change.  When you refresh/reload 
the page, the lights should change again.  

If this does not happen, download the debug file to your www directory and try that.  

    sudo wget https://raw.github.com/dw87/PyGloworm/master/pygloworm.py -P /var/www

Browse to this page.  Your browser should display the word 'Done' in the body of the HTML
if this has worked correctly.  

If it does not, please check ALL steps above and make sure these have been completed correctly.  

## Connecting from your Website

Once all above steps have been completed, tested and are working, you can now link from your own website
to the PiGlow using PyGloworm.  

I do this using cURL in PHP, to directly call pygloworm.py on my Raspberry Pi using the URL I have 
configured using Dynamic DNS.  If you are using a static external IP, use that in the URL in the example below.   

I have added this code to the top of my page:

    <?php
    	$ch = curl_init("http://your-raspberry-pi.com/pygloworm.py");
    	curl_setopt($ch, CURLOPT_CONNECTTIMEOUT_MS, 1000); //Added timeout options
    	curl_setopt($ch, CURLOPT_TIMEOUT_MS, 1000);
    	curl_exec($ch);
    	curl_close($ch);
    ?>

It does not create any output so your original page will load and display correctly.  

I have experienced issues when browsing to the page when the Raspberry Pi is offline, so there is no web server 
for the cURL function to connect to.  I think it was waiting for the cURL execution to timeout before loading the rest of 
the page to display, which is not good for user experience.  This should have little to no impact to users visiting my website.  
I have set a connection timeout and execution timeout of 1000ms (1s) to the cURL call.  I experimented with less, but that 
stopped it from functioning, and I believe the minimum allowed is 1 second.  

This is probably not the best way to solve this.  If there is a more appropriate way, please contribute it to the project.  

## Help

This is both my first project on Github and my first project with the Raspberry Pi.  
It was something I thought up as an introduction to both.  

There are bound to be problems.  

It is likely I have missed something, or made mistakes, when going back through the steps I took to configure 
my Raspberry Pi to make this work.  

I have written this README on the Raspberry Pi, and the PiGlow is still changing when I get visitors 
to my website, so it definitely works.  The instructions above should tell you how.  

If you find a problem, please let me know.
