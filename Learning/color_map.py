import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


def plot_examples(colormaps, data):
    n = len(colormaps)
    fig, axs = plt.subplots(1, n,
                            constrained_layout=False, squeeze=False)
    for [ax, cmap] in zip(axs.flat, colormaps):
        psm = ax.pcolormesh(data, cmap=cmap, rasterized=True, vmin=-10, vmax=10)
        #fig.colorbar(psm, ax=ax)
    plt.show()


data = np.ones((30,30))-2
np.random.seed(19680801)
#data = np.random.randn(30, 30)
for i in range(10):
    data[10][5+i] = -10+i
    data[18][5+i] = 10


cmap = ListedColormap(['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'])
#cmap = ListedColormap(["darkorange", "gold", "lawngreen", "lightseagreen"])
plot_examples([cmap], data)