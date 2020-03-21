import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('fivethirtyeight')

x_val = []
y_val = []

topLeftX = 0
topLeftY = 0
BotRightX = 0
BotRightY = 0
for y in range(4):
    for x in range(4):
        topLeftX = 4 * x
        topLeftY = 15 - 4 * y
        BotRightX = 4 * x + 3
        BotRightY = 15 - 4 * y - 3
        print("---")
        print(topLeftX, topLeftY, BotRightX, BotRightY)
        print("---")
        x_val = [topLeftX, topLeftX, BotRightX, BotRightX, topLeftX]
        y_val = [BotRightY, topLeftY, topLeftY, BotRightY, BotRightY]
        plt.plot(x_val, y_val)
plt.xticks(range(16))
plt.yticks(range(16))
plt.show()
