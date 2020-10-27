!#/bin/bash

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

lsusb
