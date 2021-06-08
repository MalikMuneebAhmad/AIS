import numpy as np
import itertools
import matplotlib.pyplot as plt

# Calculation and placing distance value around a point
def chessboard_distance(region, rob_loc):
    arena = np.zeros(10000).reshape(100,100)
    nei_x = np.array(range(rob_loc[0]-region, rob_loc[0]+region+1))
    nei_y = np.array(range(rob_loc[1]-region, rob_loc[1]+region+1))
    nei_loc = np.array(list(itertools.product(nei_x, nei_y)))
    print(nei_loc)
    for idx in np.ndindex(nei_loc.shape[:1]):
        single_nei = nei_loc[idx]
        print(single_nei)
        arena[single_nei[0]][single_nei[1]] = min([region - abs(single_nei[0] - rob_loc[0]),  region - abs(single_nei[1] - rob_loc[1])])
        #print(arena)
    return arena, nei_loc


arena, loc = chessboard_distance(5,[75,50])
plt.imshow(arena, origin='lower')
plt.show()

