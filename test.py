import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('fivethirtyeight')

x_val = [1, 2, 2, 1, 1]
ch1_y_val = [1, 1, 2, 2, 1]
ch1_z_val = [1, 1, 2, 2, 1]
plt.plot(x_val, ch1_y_val, ch1_z_val)
plt.show()