from Modules import Bacteria
from Modules import Chemotaxis
from Modules import Immune_cells
import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib import animation
import random


def fitness(cells_loc, target):  # For the calculation of fitness for each particle
    fitness_array = list()
    for i, cell_loc in enumerate(cells_loc):
        fitness_array.append(round(math.sqrt(((target[0] - cell_loc[0])**2) + ((target[1] - cell_loc[1])**2)), 3))
    #print('dist', fitness_array)
    return fitness_array


arena_x = 50
arena_y = 50
num_bac = 2 # number of bacteria
is_alive = [1] * num_bac
no_im_cells = 6
imm_alive = [1] * no_im_cells

bac = Bacteria(arena_x, arena_y, num_bac) # Creating bacteria Instant
bac_x, bac_y, bac_loc = bac.cluster(1, [2, 25])  # Placement of Bacteria in the arena
#bac_x, bac_y, bac_loc = bac.cluster(0, [5, 15])  # Placement of Bacteria in the arena
bac_chem = Chemotaxis(arena_x, arena_y, num_bac)  # Creating bacteria chemokine instance

im_cell = Immune_cells(arena_x, arena_y, no_im_cells)  # Creating immune Cell Instant
im_cellx, im_celly = im_cell.cluster(3, [25, 25])  # Cluster placement of immune_cell
im_cell.monocytes_x = [10, 25, 40, 10, 25, 40]  # Update of immune Cell according to our required condition
im_cell.monocytes_y = [12, 12, 12, 37, 37, 37]

# Initialization of Monokine of Immune Cell
mac_chem = Chemotaxis(arena_x, arena_y, no_im_cells)


for j in range(20):
    if j % 1 == 0 and j < 35:
        #bac_x[0] += 1
        #print(bacy)
        bac.move('Active')
        #print('Bacy', bac_y)
    bac_loc = [[bac_x[i], bac_y[i]] for i in range(num_bac)]
    internal_damage = bac.internal_cellular_effect(3, 2)
    chem_array = bac_chem.chemo_attractants(bac_x, bac_y, 0.125, 0.02, 0.25)
    #bac_chem.again_chemo(bac_x, bac_y)
    #mono_array = mac_chem.chemo_attractants(imm_alive, im_cell.monocytes_x, im_cell.monocytes_y)  # Array updation of Monokines
    mono_array = np.zeros([arena_x, arena_y])
    #print('Chemo_array', chem_array)
    grad = im_cell.gradient(chem_array, mono_array)
    cellx, celly = im_cell.random_movementall(grad)
    mac_loc = [[cellx[i], celly[i]] for i in range(no_im_cells)]
    im = chem_array + mono_array
    plt.title('Single Immune Cell Movement = ' + str(j))
    plt.xlabel('Y')
    plt.ylabel('X')
    plt.imshow(chem_array, origin='lower')
    #images = [plt.imshow(chem, origin='lower') for _ in range(N)]  # image to animate
    bac.arrayupdation('r*')
    im_cell.arrayupdation()
    plt.show()
    plt.pause(0.5)
    dist = fitness(mac_loc, bac_loc[0])
    #print('fitness', sum(dist))
    #anim = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=20, blit=True)
    #plt.show()

plt.title('Single Immune Cell Movement = ' + str(j))
plt.xlabel('Y')
plt.ylabel('X')
plt.imshow(im, origin='lower')
bac.arrayupdation('r*')
im_cell.arrayupdation()
plt.pause(0.5)
plt.show()