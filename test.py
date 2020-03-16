import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('fivethirtyeight')

x_val = [1, 2, 4, 2]
ch1_y_val = [3, 4, 2, 2]
ch2_y_val = []
plt.plot(x_val, ch1_y_val, label='Channel = 1')
plt.show()