Spencer Wong
ENGI 301
Loss Prevention Device

This is the directory for the "Loss Prevention Device", my project for ENGI 301, Introduction to Practical Electrical Engineering.

This is a project that utilizes a bluetooth module, GPS module, and WiFi adapter with a PocketBeagle to alert a user through text when their phone is separated too far from the device. The bluetooth module I used was a DSD TECH HM-10, and the GPS module I used was a Goouuu Tech GT-U7. The WiFi module used was an Edimax N150.

The GPS and BT module are connected using standard UART ports, and the WiFi adapter is connected to the USB pins of the PocketBeagle using an adapter.


To run this, 
1. Set up the WiFi module using sudo connmanctl > agent on > scan wifi > services > connect wifi_....... [the WiFi you want to connect to in the services list]

2. Configure the pins using configure_pins.sh

3. Install Adafruit BBIO UART, pynmea2, and twilio

4. Download the DSD Tech app on your phone to connect and disconnect from the BT module

5. Run MainLPD.py

The device will constantly ping your phone until the connection is lost. Once connection is lost, Twilio will text you the coordinates from the GPS. The script will keep this loop running indefinitely.


**verify_hardware.sh can be used to check all connections


Note that any Twilio information is censored. Make an account on Twilio and use your own information to get that part to work.

*Hackster URL*
