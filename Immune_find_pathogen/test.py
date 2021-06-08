import random
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure(figsize=(15,15))


x,y = [], []
index = count()


def animate(i):
    x.append(next(index))
    y.append(random.randint(2,20))
    plt.style.use("ggplot")
    plt.plot(x,y)

ani = FuncAnimation(fig, animate, interval=300)
plt.show()
