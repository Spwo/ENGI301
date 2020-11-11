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
import Adafruit_BBIO.UART as UART
import serial
import pynmea2
import time
import os


# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

#UART1 is the bluetooth module
UART.setup("PB-UART4")
 
#UART2 is the GPS module
UART.setup("PB-UART2")





# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

# None

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

# None

# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------

def BTcomm_setup():
    """Set up UART communication with BT module."""
    BTport = serial.Serial(port = "/dev/ttyO4", baudrate=9600, timeout=1)
    BTport.close()
    BTport.open()
    
    if (BTport is None) or (not BTport.isOpen()):
        print("ERROR opening UART4 port.")
        return None
    
    return BTport
# End def

def GPScomm_setup():
    """Set up UART communication with GPS module."""
    GPSport = serial.Serial(port = "/dev/ttyO2", baudrate=9600, timeout=1)
    GPSport.close()
    GPSport.open()
    
    if (GPSport is None) or (not GPSport.isOpen()):
        print("ERROR opening UART2 port.")
        return None
    
    return GPSport
# End def


def send_BTcmd(message):
    """Send and recieve AT command with BT module"""
    #print("Send: {0}".format(message))
    BTport.write(message.encode("utf-8"))
    response = BTport.read(1000).decode("utf-8")
    #  until a response is read:
    #while response == "":
        #BTport.write(message.encode("utf-8"))
        #response = BTport.read(1000).decode("utf-8")
    #print("Recv: {0}".format(response))
    
    return response
# End def

def send_location(lattitude, longitude):
    """Send location to phone"""
    # Authentication is censored for publishing
    account_sid = 'ACfa28ef2d0cf861f0edb283ed3839a47b'
    auth_token = '7761284591ec00f79522f8304131d627'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body="You have separated from your device! It was last seen at,\nLattitude: {} \nLongitude: {}".format(lattitude, longitude),
            # Phone number is censored for publishing
            from_='+12053524587',
            to='+17742706970'
            )
    #print(message.body)
# End def

def get_GPS_data():
    """Find lattitude and longitude using GPS module"""
    t_end = time.time() + 2 #2 seconds should be enough to get the data we need
    while time.time() < t_end:
        y = GPSport.readline()
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
                lattitude = msg.lat
                longitude = msg.lon
                if lattitude == "":
                    lattitude = "NO LONGITUDE DATA" # If the GPS cannot find location
                else:
                    lattitude = str(float(lattitude)/100)
                    lattitude = lattitude[:6] # Truncate the value
                    lattitude = lattitude + " " + msg.lat_dir # Add the direction
                    #print(lattitude)
                if longitude == "":
                    longitude = "NO LONGITUDE DATA" # If the GPS cannot find location
                else:
                    longitude = str(float(longitude)/100)
                    longitude = longitude[:6]
                    longitude = longitude + " " + msg.lon_dir
                    #print(longitude)
            except pynmea2.ParseError as e:
                print('Parse error: {}'.format(e))
                continue
            #If status is 'V', that means there's a warning and connection bad
    return [lattitude, longitude];

# End def



# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':
    # Set up comm
    BTport = BTcomm_setup()
    GPSport = GPScomm_setup()
    
    """ Below is a loop where the BT module will keep searching for the phone. 
    Once the phone connects and disconnects the loaction will be sent,
    and the loop will reset """
    LookForPhone = False
    while True:
        resp = send_BTcmd("AT+ADDR?") # Constantly ping BT module
        print(resp)
        if resp == "":
            # A blank string means phone is connected. Start watching for a disconnect
            LookForPhone = True
        if resp != "" and LookForPhone == True:
            # Once disconnect, gather GPS data and text phone location
            [lattitude, longitude] = get_GPS_data()
            send_location(lattitude, longitude)
            LookForPhone = False
            print("sending coordinates")    

    
    
