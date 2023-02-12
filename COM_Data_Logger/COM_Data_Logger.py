import time
import serial

baud = 9600 #115200

arduino_port1 = 'COM1'
arduino_port2 = 'COM2'
arduino_port3 = 'COM3'
arduino_port4 = 'COM4'
arduino_port5 = 'COM5'
arduino_port6 = 'COM6'

fileName1 = "Laufrad1.csv"
fileName2 = "Laufrad2.csv"
fileName3 = "Laufrad3.csv"
fileName4 = "Laufrad4.csv"
fileName5 = "Laufrad5.csv"
fileName6 = "Laufrad6.csv"

arduinoData1 = serial.Serial(arduino_port1, baud)
arduinoData2 = serial.Serial(arduino_port2, baud)
arduinoData3 = serial.Serial(arduino_port3, baud)
arduinoData4 = serial.Serial(arduino_port4 , baud)
arduinoData5 = serial.Serial(arduino_port5, baud)
arduinoData6 = serial.Serial(arduino_port6, baud)

# Print Info about the Program
print('+----------------------------------------------------------------+')
print('|  Arduino Python Serial Port Data Logging to CSV file Software  |')
print('+----------------------------------------------------------------+')
print('| Requires Pyserial installed on your System                     |')
print('| use CTRL + C to exit from the software                         |')
print('+----------------------------------------------------------------+\n')

time.sleep(1)

### Write separate code??
while True:
    while (arduinoData.inWaiting() == 0):
        pass
    dataPacket = arduinoData.readline()
    print(dataPacket)
    dataPacket = str(dataPacket, 'utf-8')
    print(dataPacket)
    dataPacket = dataPacket.strip('\r\n')
    print(dataPacket)
    splitPacket = dataPacket.split(",")
    print(splitPacket)
    with open(fileName1,"a") as file:
        file.write(splitPacket)
        file.write("\n")
