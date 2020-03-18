import serial
import re
ser = serial.Serial()
ser.baudrate = 460800
ser.port = 'COM4'
ser.open()
print("Is open:", ser.is_open)
while 1:
    line = ser.readline()
    match = re.findall(r'\d+', str(line))
    print(match)