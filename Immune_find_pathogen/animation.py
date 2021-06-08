import matplotlib
matplotlib.use('Qt5Agg') #use Qt5 as backend, comment this line for default backend
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import random


#init_board = np.random.uniform(1,10, size=[10,10])
init_board = np.zeros([100, 100])
init_board[1:9, 2:3] = 100


def update_board(init_board):
    # All Changes to update the board will be made here
    #board =  np.random.uniform(1,10, size=[10,10])
    init_board = np.ones([100,100])  # To clear the previous frame
    init_board[np.random.randint(0, 100, 10), np.random.randint(0, 100, 10)] = 100  # new data will be added here
    print(type(init_board))
    return init_board


fig = plt.gcf()
plt.clf()
im = plt.imshow(init_board, origin = 'lower')


def animate(frame):
    im.set_data(update_board(init_board))

        #plt.scatter([5+i, 8+i], [20, 30])
        #plt.plot([5+i,10+i], [3,10], 'r*')
    return im,


anim = animation.FuncAnimation(fig, animate, frames=200, interval=50)
plt.show()