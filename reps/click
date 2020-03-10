#!/usr/bin/python3

import os
import sys

arglist = sys.argv
ip = arglist[1]
os.system("scp /root/Desktop/reps/cam.py {}:/tmp/".format(ip))
os.system("ssh {} python36 /tmp/cam.py".format(ip))
os.system("scp {}:/root/Desktop/pic.png /var/www/html/".format(ip))
os.system("ssh {} rm -rf /root/Desktop/pic.png".format(ip))
