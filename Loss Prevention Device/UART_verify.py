import Adafruit_BBIO.UART as UART
import serial

"""UART4 is the bluetooth module"""
#UART.setup("UART1")
 

ser = serial.Serial(port = "/dev/ttyO4", baudrate=9600)
ser.close()
ser.open()
if ser.isOpen():
	print("Serial 4 is open! (BT Module)")
ser.close()


"""UART2 is the GPS module"""
#UART.setup("UART2")
 
ser = serial.Serial(port = "/dev/ttyO2", baudrate=9600)
ser.close()
ser.open()
if ser.isOpen():
	print("Serial 2 is open! (GPS Module)")
ser.close()