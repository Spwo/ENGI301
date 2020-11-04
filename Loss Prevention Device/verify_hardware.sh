lsusb # Check usb
#dmesg|grep rtl # Look for "Loading Firmware rtlwifi/rtl8192cufw.bin"
#dmesg | grep wlan0

ping google.com -c 2 # Verify iPhone hotspot is connected

python3 UART_verify.py

# To connect to iphone hotspot: sudo connmanctl, agent on, scan wifi, services, connect wifi_.........
# Sometimes have to unplug then replug usb pins for it to work

#For UART there's a python library called serial (pyserial) -- sudo pip3 install pyserial
#Adafruit BBIO also has a UART library
#minicom
#ls /dev
