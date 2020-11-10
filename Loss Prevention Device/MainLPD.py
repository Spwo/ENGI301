# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
MainLPD
--------------------------------------------------------------------------
Authors: Spencer Wong (sbw1 [at] rice [dot] edu)
 
Copyright 2020, Spencer Wong

License:  

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, 
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Program that will be used for loss prevention device. See Code flow diagram.

--------------------------------------------------------------------------
"""
import sys
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.UART as UART
import serial
import pynmea2
import time



# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

"""UART1 is the bluetooth module"""
UART.setup("PB-UART4")
 

ser1 = serial.Serial(port = "/dev/ttyO4", baudrate=9600, timeout=2)
ser1.close()
ser1.open()

# Verification for serial port
if ser1 is None or not ser1.isOpen():
    print("ERROR opening UART4")
    sys.exit(0)

#wakeup_str = "a" * 100
#ser1.write(wakeup_str.encode("utf-8"))
ser1.write("AT+RSSI?".encode("utf-8"))
time.sleep(1)
#You will recieve OK+RSSI:[P1]
x = ser1.readline()
print("Serial reading from BT Module:")
print(x)

"""ConnectionStrength = x[8:]
while ConnectionStrength < -80:
    ser1.write("AT+RSSI?".encode("utf-8"))
    time.sleep(1)
    x = ser1.readline()
    ConnectionStrength = x[8:]"""
    #Loop reading ConnectionStrength until it gets below -80


"""UART2 is the GPS module"""
UART.setup("PB-UART2")
 
ser2 = serial.Serial(port = "/dev/ttyO2", baudrate=9600, timeout=2)
ser2.close()
ser2.open()

# Verification for serial port
if ser2 is None or not ser2.isOpen():
    print("ERROR opening UART2")
    sys.exit(0)
    
    



#print("Serial reading from GPS Module:")
t_end = time.time() + 2
while time.time() < t_end:
    y = ser2.readline()
    try:
        y = y.decode("utf-8")
    except:
        pass
    DataType = y[:6] #Grab the type of NMEA data from the beginning of the string
    #print(y) # This will print all types of NMEA data
    if DataType == "$GPGGA":
        #GPGGA is the most standard form of NMEA output
        try:
            msg = pynmea2.parse(y, check=False) #Convert string using pynmea2
            #print(repr(msg))
            #print("Lattitude and Longitude:")
            lattitude = str(float(msg.lat)/100)
            lattitude = lattitude[:6] # Truncate the value
            lattitude = lattitude + " " + msg.lat_dir # Add the direction
            longitude = str(float(msg.lon)/100)
            longitude = longitude[:6]
            longitude = longitude + " " + msg.lon_dir
            if lattitude == "":
                lattitude = "NO LONGITUDE DATA"
            #print(lattitude)
            if longitude == "":
                longitude = "NO LONGITUDE DATA"
            #print(longitude)
        except pynmea2.ParseError as e:
            print('Parse error: {}'.format(e))
            continue
            
            #If status is 'V', that means there's a warning and connection bad



"""Messaging system"""
account_sid = 'XXXXXX'
auth_token = 'XXXXX'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
        body="Your device was last seen at,\nLattitude: {} \nLongitude: {}".format(lattitude, longitude),
        from_='XXXXXX',
        to='XXXXXXX'
        )
print(message.body)




"""BLUETOOTH:
Use the code Erik emailed

Move to UART 4

Direct connection instead
"""






# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------



# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

# None

# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------




# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

