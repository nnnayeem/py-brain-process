import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

fig, ax = plt.subplots()
xdata, ydata = [0], [0]
ln, = plt.plot([], [], 'ro')


def init():
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    return fig,


def update(frame):
    print(frame)
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)
    return ln,


def cus(frame):
    axis = xdata[-1] + frame
    if xdata[-1] > 100 and axis - xdata[-1] < 20: ax.set_xlim(0, axis + 20)
    xdata.append(axis)
    ydata.append(ydata[-1] + frame)
    ln.set_data(xdata, ydata)
    return ln,




ani = FuncAnimation(fig, cus, init_func=init, blit=True, interval=100)
plt.show()



