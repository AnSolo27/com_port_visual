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
    #plt.cla()
    #A = A.transpose()
    obj.set_data(A)

ani = FuncAnimation(plt.gcf(), animate, interval=50)
plt.plot()
obj = plt.imshow(A, origin='upper', interpolation=interp, extent=[0, 4, 0, 4], vmax=2300, vmin=300)
plt.title(interp.capitalize())
plt.grid(True)
plt.show()

