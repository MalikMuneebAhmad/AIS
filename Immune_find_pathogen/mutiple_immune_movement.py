from Modules import Bacteria
from Modules import Chemotaxis
from Modules import Nk_cells
import matplotlib.pyplot as plt
import numpy as np
import random


def inflammation(cellx, celly, bac_loc):
    im_cell_array = np.array([[cellx[i], celly[i]] for i in range(len(im_cellx))])
    infl = np.sum((im_cell_array - np.array(bac_loc))**2)
    return infl


np.seterr(divide='ignore', invalid='ignore')

arena_x = 50
arena_y = 50
num_bac = 1  # number of bacteria
is_alive = [1] * num_bac
no_im_cells = 5
imm_alive = [1] * no_im_cells

bac = Bacteria(arena_x, arena_y, num_bac) # Creating bacteria Instant
bac_x, bac_y, bac_loc = bac.cluster(0, [5, 15])  # Placement of Bacteria in the arena
bac_chem = Chemotaxis(arena_x, arena_y, num_bac)

im_cell = Nk_cells(arena_x, arena_y, no_im_cells)  # Creating immune Cell Instant
im_cellx, im_celly = im_cell.cluster(3, [25, 25])  # Cluster placement of immune_cell
im_cell.monocytes_x = [20, 20, 20, 30, 30]  # Update of immune Cell according to our required condition
im_cell.monocytes_y = [15, 30, 45, 23, 38]

# Initialization of Monokine of Immune Cell
mac_chem = Chemotaxis(arena_x, arena_y, no_im_cells)


for j in range(50): # Main Loop
    if j % 1 == 0 and j < 20:
        bac_y[0] += 1
        #print(bacy)
        #bac_loc = [[bacx[i], bacy[i]] for i in range(len(bacx))]
    chem_array = bac_chem.chemo_attractants(is_alive, bac_x, bac_y)
    #mono_array = mac_chem.chemo_attractants(imm_alive, im_cell.monocytes_x, im_cell.monocytes_y)  # Array updation of Monokines
    mono_array = np.zeros([arena_x, arena_y])
    grad = im_cell.gradient(chem_array, mono_array)
    im_cellx, im_celly = im_cell.random_movementall(grad)
    bac.bacteria_x, bac.bacteria_y, bac.is_alive = im_cell.kill_bac(bac_x, bac_y, bac.is_alive)
    im = chem_array + mono_array
    print('Alive', bac.is_alive)
    plt.title('Immune Cells Movement = ' + str(j))
    plt.xlabel('Y')
    plt.ylabel('X')
    plt.imshow(im, origin='lower')
    im_cell.arrayupdation()
    bac.arrayupdation('r*')
    plt.pause(0.5)
    plt.show()