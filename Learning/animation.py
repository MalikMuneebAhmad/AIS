import matplotlib
#import matplotlib; matplotlib.use("TkAgg")
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Animation of a line
plt.figure(1)
x_data = []
y_data = []

fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 10)
line, = ax.plot(0,0)


def animation_frame(i):
    x_data.append(i * 10)
    y_data.append(i)
    line.set_xdata(x_data)
    line.set_ydata(y_data)
    return line,


animation = animation.FuncAnimation(fig, func=animation_frame, frames=np.arange(0, 10, 0.05), interval=10, blit=True)
plt.show()

'''ar = np.ones(10000).reshape(100,100)
fig1, ax1 = plt.subplots()
ax1.set_xlim(0, 100)
ax1.set_ylim(0, 100)
imag = ax1.imshow(ar)
im = np.ones(10000).reshape(100,100)

def animation_frame(i):
    im[i][i] = 0
    imag.set_data(im)
    return imag


animation = animation.FuncAnimation(fig1, func=animation_frame, frames=np.arange(0, 100, 1), interval=10)
plt.show()'''


# Animation of Sin wave
'''fig1, ax1 = plt.subplots()

x = np.arange(0, 2 * np.pi, 0.01)
sine, = ax1.plot(x, np.sin(x))


def animate(i):
    sine.set_ydata(np.sin(x + i / 10.0))  # update the data
    return sine,


# Init only required for blitting to give a clean slate.
def init():
    sine.set_ydata(np.ma.array(x, mask=True))
    return sine,


ani = animation.FuncAnimation(fig1, animate, np.arange(1, 20000), init_func=init,
                              interval=25, blit=True)
plt.show()'''