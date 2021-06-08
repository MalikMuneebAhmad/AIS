import matplotlib.pyplot as plt
from Modules import Bacteria
from Modules import Chemotaxis
import numpy as np

arena_x = 100
arena_y = 100
num_bac = 10
is_alive = [1] * 10

for i in range(20):
    if i == 0:
        # Creation of Bacteria object
        bac = Bacteria(arena_x, arena_y, num_bac)
        bac_x, bac_y = bac.cluster(5, [50, 50])  # Placement of Bacteria in the arena

        # Creation of Bacteria chemotaxis for chemokines
        a = Chemotaxis(arena_x, arena_y, num_bac)
        chemo_array = a.chemo_attractants(bac.is_alive, bac_x, bac_y)  # Array updation of chemokines
    else:
        plt.title('Bacteria and Chemotaxis Plot ' + str(i))
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.imshow(chemo_array)
        bac.arrayupdation('r*')
        plt.show()
        bac_x, bac_y = bac.move(2)  # Movement of Bacteria by step_size = 2
        chemo_array = a.chemo_attractants(is_alive, bac_x, bac_y)  # Array updation of chemokines
