#!/usr/bin/python
import os
from subprocess import check_output
import smtplib
import importlib

importlib.import_module('jacob2')

server = smtplib.SMTP('smtp.southern.edu', 587)
snmpstring1 = "snmpget -v 1 -c LiebertEM liebert.cs.southern.edu .1.3.6.1.4.1.476.1.42.3.4.1.2.3.1.50.1"
snmpstring2 = "snmpget -v 1 -c LiebertEM liebert.cs.southern.edu .1.3.6.1.4.1.476.1.42.3.4.1.2.3.1.50.2"
y1 = str(check_output(snmpstring1, shell=True)).strip()
y2 = str(check_output(snmpstring2, shell=True)).strip()
cold = y1.split('.')
cold = float(cold[16][13:15] + '.' + cold[16][15:16])
hot = y2.split('.')
hot = float(hot[16][13:15] + '.' + hot[16][15:16])
temp_diff = hot - cold
if 7 >= temp_diff > 4:
    server.login("username", "password")
    msg = '/nHey the temp in the server room is ' + temp_diff + ' F degrees. Check to make sure AC working.'
    server.sendmail("youremail@southern.edu", "targetemail@whatever.edu", msg)
if temp_diff < 4:
    server.login("username", "password")
    msg = '/nHey AC machine broke'
    server.sendmail("youremail@southern.edu", "targetemail@whatever.edu", msg)