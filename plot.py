from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('fivethirtyeight')

x_val = []
ch1_y_val = []
ch2_y_val = []

index = count()

def animate(i):
    data = pd.read_csv('data.csv')
    x_val = data['x_val']
    ch1_y_val = data['y_ch1']
    ch2_y_val = data['y_ch2']
    plt.cla()
    plt.plot(x_val, ch1_y_val, label='Channel = 1')
    plt.plot(x_val, ch2_y_val, label='Channel = 2')
    #plt.plot(x_vals, y_vals + 1, label='Channel = 2')
    plt.legend(loc='upper left')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=100)
plt.show()