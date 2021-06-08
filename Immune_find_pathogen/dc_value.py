import matplotlib.pyplot as plt
import numpy as np
from Modules import Bacteria
from Modules import DendricCells
from Modules import Chemotaxis

arena_x = 60
arena_y = 10
types_bac = 1
num_bac = 2
is_alive = [1] * num_bac

for i in range(50):
    print(i)
    if i == 0:  # for initialization
        # dendric Cell object created
        print('Start of Code')
        dendric = DendricCells(arena_x, arena_y)
        no_dc, dc_x, dc_y = dendric.placement(0.01)

        bac = Bacteria(arena_x, arena_y, num_bac)
        bac_x, bac_y, bac_loc1 = bac.cluster(1, [5, 5])

        bac_chem = Chemotaxis(arena_x, arena_y, num_bac)
        chemo_array = bac_chem.chemo_attractants(is_alive, bac_x, bac_y)

    else:
        dendric.scanning()  # Dendric Cell movement
        #bac.move(1)
        if i < 18:
            bac.bacteria_x[0] += 3
            bac.bacteria_x[1] += 3
        chemo_array = bac_chem.chemo_attractants(is_alive, bac.bacteria_x, bac_y)
        int_damage = bac.internal_cellular_effect(3, 2)
        bac_loc = [[bac.bacteria_x[i], bac_y[i]] for i in range(num_bac)]
        dendric.detect_pathogen(bac_loc)
        danger = dendric.maturity_danger1(int_damage)
        total_maturity = dendric.commulative_maturity()
        print('Total Maturity', total_maturity)
        plt.title('DC value for linear moving bacteria' + ' ' + str(i))
        plt.xlabel('DCY')
        plt.ylabel('DCX')
        plt.imshow(chemo_array, origin='lower')
        dendric.arrayupdation()  # Plot of DC
        bac.arrayupdation('r*')  # Bacteria plot
        for i in range(7):
            plt.text(5, (2 + 9*i), danger[i])
        plt.pause(0.5)
        plt.show()