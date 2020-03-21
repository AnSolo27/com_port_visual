import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from matplotlib.animation import FuncAnimation
import serial
import re

ser = serial.Serial()
ser.baudrate = 460800
ser.port = 'COM4'
ser.open()
print("Is open:", ser.is_open)

A = np.random.rand(4, 4)
interp = 'bicubic'

def animate(i):
    data = ser.readline()
    result = re.findall(r'\d+', str(data))
    i = 0
    for number1 in range(4):
        for number2 in range(4):
            A[number1][number2] = result[i]
            i+=1
    print(result)
    print(A)
    for stroka in range(4):
        A[stroka][0], A[stroka][2] = A[stroka][2], A[stroka][0]
        A[stroka][1], A[stroka][3] = A[stroka][3], A[stroka][1]
    A[0][2], A[3][2] = A[3][2], A[0][2]
    A[0][3], A[3][3] = A[3][3], A[0][3]
    A[0][2], A[2][2] = A[2][2], A[0][2]
    A[0][3], A[2][3] = A[2][3], A[0][3]
    A[0][2], A[1][2] = A[1][2], A[0][2]
    A[0][3], A[1][3] = A[1][3], A[0][3]
    print("---")
    print(A)
    obj.set_data(A)

ani = FuncAnimation(plt.gcf(), animate, interval=50)
plt.plot()
obj = plt.imshow(A, origin='upper', interpolation=interp, extent=[0, 4, 0, 4], vmax=2500, vmin=300)
plt.title(interp.capitalize())
plt.grid(True)
plt.show()

