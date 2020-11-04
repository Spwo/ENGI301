cd /sys/class/gpio/gpio43 #TX from bluetooth module
cat direction
cat value

cd /sys/class/gpio/gpio42 #RX from bluetooth module
cat direction
cat value

cd /sys/class/gpio/gpio31 #TX from GPS
cat direction
cat value

cd /sys/class/gpio/gpio30 #RX from GPS
cat direction
cat value

lsusb # Check usb
#dmesg|grep rtl # Look for "Loading Firmware rtlwifi/rtl8192cufw.bin"
#dmesg | grep wlan0

ping google.com # Verify iPhone hotspot is connected



#To connect to iphone hotspot: sudo connmanctl, agent on, scan wifi, connect wifi_.........

#For UART there's a python library called serial (pyserial) -- sudo pip3 install pyserial
#Adafruit BBIO also has a UART library
#minicom
#ls /dev
