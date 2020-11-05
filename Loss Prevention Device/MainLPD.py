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

"""UART1 is the bluetooth module"""
UART.setup("PB-UART1")
 

ser1 = serial.Serial(port = "/dev/ttyO1", baudrate=9600, timeout=2)
ser1.close()
ser1.open()

# Verification for serial port
if ser1 is None or not ser1.isOpen():
    print("ERROR opening UART1")
    sys.exit(0)

wakeup_str = "a" * 100
ser1.write(wakeup_str.encode("utf-8"))
ser1.write("AT+ADDR?".encode("utf-8"))
x = ser1.readline()
print("Serial reading from BT Module:")
print(x)


"""UART2 is the GPS module"""
UART.setup("PB-UART2")
 
ser2 = serial.Serial(port = "/dev/ttyO2", baudrate=9600, timeout=2)
ser2.close()
ser2.open()

# Verification for serial port
if ser2 is None or not ser2.isOpen():
    print("ERROR opening UART2")
    sys.exit(0)
    
    
y = ser2.readline()
print("Serial reading from GPS Module:")
print(y)




"""BLUETOOTH:
Wait for UART verification tomorrow
"""


"""GPS:
Use Library to convert NMEA data to something good
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

