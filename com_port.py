import serial
import re
ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM3'
ser.open()
print("Is open:", ser.is_open)
while 1:
    line = ser.readline()
    match = re.findall(r'\d+', str(line))
    print(match[0], match[1])