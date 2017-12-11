#!/usr/bin/python
# imports modules needed for functionality
import os
import subprocess
import smtplib

# email variables Variables
USERNAME = '<username>' # username for account used in the smtp server
PASSWORD = '<password>' # password for account used in the smtp server
sender = '<sender@example.com>' # account used for the sender's email address
receiver = '<receiver@example.com' # account used for the receiver's email address
server = smtplib.SMTP('smtp.southern.edu', 587) # sets the server to use for smtp


cold_OID = "snmpget -v 1 -c LiebertEM liebert.cs.southern.edu .1.3.6.1.4.1.476.1.42.3.4.1.2.3.1.50.1" # is the command and OID for the thermostat in the cold side of the room
hot_OID = "snmpget -v 1 -c LiebertEM liebert.cs.southern.edu .1.3.6.1.4.1.476.1.42.3.4.1.2.3.1.50.2" # is the command and OID for the thermostat in the hot side of the room
cold_temp = str(subprocess.check_output(cold_OID,shell=True)).strip() # runs the cold command
hot_temp = str(subprocess.check_output(hot_OID,shell=True)).strip() # runs the hot command
cold = cold_temp.split('.') # splits the data by . for cold
cold = float(cold[16][13:15] + '.' + cold[16][15:16]) # extracts the data that contains the cold temperature information
hot = hot_temp.split('.') # splits the data by . for hot
hot = float(hot[16][13:15] + '.' + hot[16][15:16]) # extracts the data that contains the hot temperature information
temp_diff = hot - cold # determines the difference between the tempuratures



if 7 >= temp_diff > 4: # checks if differenceless than seven and greater than four
   server.login(USERNAME, PASSWORD) # sets the server login as active
   msg = '\nThe current temperature is ' + temp_diff + ' F degrees. Check for functionality' # generates message for the temperature approaching unsafe levels
   server.sendmail(sender, receiver, msg) # sends the message

if temp_diff < 4: # checks if difference is less than 4 degrees
   server.login("jancion","BoBum1991") # sets server login as active
   msg = '\nA/C not functioning.' # generates message for the temperature reaching dangerous levels
   server.sendmail("jancion@southern.edu", "jancion@southern.edu", msg) # sends the message    