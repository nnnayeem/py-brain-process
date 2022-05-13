import time
import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Scope:
    data = []
    data_pointer = 0

    def __init__(self, ax, maxt=2, dt=0.02):
        self.ax = ax
        self.dt = dt
        self.maxt = maxt
        self.tdata = [0]
        self.ydata = [0]
        self.line = Line2D(self.tdata, self.ydata)
        self.ax.add_line(self.line)
        self.ax.set_ylim(-.1, 1)
        self.ax.set_xlim(0, self.maxt)
        self.ani = None

    def update(self, y):
        lastt = self.tdata[-1]
        if lastt > self.tdata[0] + self.maxt:  # reset the arrays
            self.tdata = [self.tdata[-1]]
            self.ydata = [self.ydata[-1]]
            self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
            self.ax.figure.canvas.draw()

        t = self.tdata[-1] + self.dt
        self.tdata.append(t)
        self.ydata.append(y)
        self.line.set_data(self.tdata, self.ydata)
        return self.line,

    def emitter(self, p=0.1):
        while True:
            v = np.random.rand(1)
            if v > p:
                yield 0.
            else:
                yield np.random.rand(1)

    def emitter1(self, p=0.1):
        total_data = len(self.data)
        print(total_data)
        if total_data > 0:
            while total_data - self.data_pointer - 1 > 0:
                self.data_pointer = self.data_pointer + 1
                if total_data > 200:
                    yield self.data[self.data_pointer]
                    del self.data[0:self.data_pointer]
                    self.data_pointer = 0

                yield self.data[self.data_pointer]

        yield 0.

    def emitter2(self, p=0.1):
        data = self.data[self.data_pointer:]
        total_data = len(data)
        if total_data == 0:
            data = [0]
            return iter(data)

        if self.data_pointer > 100:
            del self.data[0:self.data_pointer]
            self.data_pointer = 0
            return iter(data)

        print(self.data_pointer, data)

        self.data_pointer = self.data_pointer + len(data)
        return iter(data)

    def emitter3(self, p=0.1):
        total_data = len(self.data)

        if total_data > 0:
            data = iter(self.data[0:total_data])
            del self.data[0:total_data]
            return data

        return iter([0])

    def start(self, fig):
        ani = animation.FuncAnimation(fig, self.update, self.emitter3, interval=10, blit=True)
        plt.show()

    def generate(self):
        while 1:
            self.data.append(np.random.rand(1))
            time.sleep(0.01)

    def set(self, y):
        self.data.append(y)



