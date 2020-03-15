import csv
import random
import time
import serial
import re

x_val = 0
y_ch1 = 0
y_ch2 = 0

fieldnames = ["x_val", "y_ch1", "y_ch2"]

ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM3'
ser.open()
print("Is open:", ser.is_open)


with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:
    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        channel1 = ser.readline()
        channel2 = ser.readline()
        res_ch1 = re.findall(r'\d+', str(channel1))
        res_ch2 = re.findall(r'\d+', str(channel2))
        y_ch1 = int(res_ch1[1])
        y_ch2 = int(res_ch2[1])
        print(int(res_ch1[0]), int(res_ch1[1]))
        print(int(res_ch2[0]), int(res_ch2[1]))
        info = {
            "x_val": x_val,
            "y_ch1": y_ch1,
            "y_ch2": y_ch2
        }
        csv_writer.writerow(info)
        x_val+=1