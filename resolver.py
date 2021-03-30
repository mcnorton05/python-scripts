#!/bin/python

import socket

#change this to the file that lists the domains
FILE="./domains.txt"

with open(FILE) as file:
    domain = [line.strip() for line in file]
    for host in domain:
    	print host + " " + socket.gethostbyname(host)
