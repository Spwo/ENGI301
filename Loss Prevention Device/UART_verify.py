import Adafruit_BBIO.UART as UART
import serial

"""UART1 is the bluetooth module"""
UART.setup("PB-UART1")
 

ser1 = serial.Serial(port = "/dev/ttyO1", baudrate=9600, timeout=2)
ser1.close()
ser1.open()
if ser1.isOpen():
	print("Serial 1 is open! (BT Module)")


"""UART2 is the GPS module"""
UART.setup("PB-UART2")
 
ser2 = serial.Serial(port = "/dev/ttyO2", baudrate=9600, timeout=2)
ser2.close()
ser2.open()
if ser2.isOpen():
	print("Serial 2 is open! (GPS Module)")