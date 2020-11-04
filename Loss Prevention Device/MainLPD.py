# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
LPD_Main
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
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.UART as UART
UART.setup("UART1")

"""BLUETOOTH:
The DSD TECH app shows about -50 dBm when VERY close to the BT module,
and about -87 when 385 inches away

I downloaded the DSD tech windows tool and was able to connect to it, 
but idk what to do with that
"""


"""I still can't really figure out how to verify my UART devices 
on a .sh file (not using a python command), nor how to communicate 
with them. There's a retrying loop when installing pyserial

Fix network first

https://learn.adafruit.com/setting-up-io-python-library-on-beaglebone-black/uart

"""

"""GPS:
Example usage is in Arduino. How do I use it? 

There's a command to convert arduino to python
    
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

