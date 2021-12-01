# Factory reset Ruckus APs via the CLI

Requires the following python2 modules:

pexpect
sys
argparse
logging
multiprocessing
time

install them via **pip2 install <module>**

## usage


*usage: ap-reset-multi.py [-h] filepath username password*

*filepath* is the path to a file containing the IP address of each AP to reset in the following format:

192.168.1.2
192.168.1.3
192.168.1.4

username and pass is the AP CLI username and password (not the SZ credentials) 

Script is multithreaded so will fire off a socket for each IP simultanously to speed up resets on large deployments
