# Bismillah-ir-Rahman-ir-Rahim
import matplotlib.pyplot as plt
import numpy as np
from Modules import Bacteria
from Modules import DendricCells
from Modules import Chemotaxis
from Modules import Nk_cells

#arena_x = int(input('Enter number of arena x-axis -->  '))
#arena_y = int(input('Enter number of arena x-axis -->  '))
initial = 0
arena_x = 80
arena_y = 70
types_bac = 3
type_im_cell = 1
bac_x = [[] for _ in range(types_bac)]
bac_y = [[] for _ in range(types_bac)]
bac_loc1 = [[] for _ in range(types_bac)]
num_bac = [10, 12, 8]
is_alive = [[1] * i for i in num_bac]
exp_area_bac = [3, 5, 4]
bac_plac = [[20, 30], [20, 70], [70, 60]]
chemo_array = [np.array([]) for _ in range(types_bac)]
no_im_cells = 0
danger_mat = np.array([])
activation = 0
monok = np.zeros([arena_x, arena_y]) # To just decalare, will be used later
mat = [0] * 100
total_maturity = []

for i in range(200):
    print(i)
    if i == 0:  # for initialization
        # dendric Cell object created
        print('Start of Code')
        dendric = DendricCells(arena_x, arena_y)
        no_dc, dc_x, dc_y = dendric.placement(0.005)


        # Bacteria objest created
        bac_pop = [Bacteria(arena_x, arena_y, num) for num in num_bac]
        bac_x[0], bac_y[0], bac_loc1[0] = bac_pop[0].cluster(exp_area_bac[0], bac_plac[0])
        #bac = Bacteria(arena_x, arena_y, num_bac[0])
        #bac_x, bac_y, bac_loc1 = bac_pop[].cluster(exp_area_bac[0], bac_plac[0])

        # Chemotaxis of Bacteria
        bac_chem = [Chemotaxis(arena_x, arena_y, num) for num in num_bac]  # Object
        chemo_array[0] = bac_chem[0].chemo_attractants(is_alive[0], bac_x[0], bac_y[0])  # Array updation of chemokines

    else:  # Main Loop after Initialization
        if activation >= 1 and initial == 0:  # Condition to initialize Innate Immune Response
            no_im_cells = 8
            imm_alive = [1] * no_im_cells
            im_cell = Nk_cells(arena_x, arena_y, no_im_cells)
            im_cellx, im_celly = im_cell.cluster(3, [30, 40])

            # Initialization of Monokine of Immune Cell
            mac_chem = Chemotaxis(arena_x, arena_y, no_im_cells)
            mono_array = mac_chem.chemo_attractants(imm_alive, im_cellx, im_celly)  # Array updation of Monokines
            initial = 1
        dendric.scanning()  # Dendric Cell movement
        mat = dendric.detect_pathogen(bac_loc1[0])
        #print('Maturity', mat)
        bac_x[0], bac_y[0], bac_loc1[0] = bac_pop[0].move('Active')  # Bacteria movement in by stepsize = 1
        chemo_array[0] = bac_chem[0].chemo_attractants(is_alive[0], bac_x[0], bac_y[0])  # Array updation of chemokines
        danger_mat = dendric.maturity_danger(chemo_array[0])

        if bac_pop[0].is_alive != 0 and initial == 1:
            print('Total Maturity', sum(total_maturity))
            grad = im_cell.gradient(chemo_array[0], mono_array)
            im_cellx, im_celly = im_cell.random_movementall(grad)
            bac_pop[0].bacteria_x, bac_pop[0].bacteria_y, bac_pop[0].is_alive = im_cell.kill_bac(bac_x[0], bac_y[0], bac_pop[0].is_alive)
            mono_array = mac_chem.chemo_attractants(imm_alive, im_cellx, im_celly)  # Array updation of Monokines
            print('Bacteria alive', len(bac_pop[0].is_alive))

        total_maturity = dendric.commulative_maturity()
        activation = len([i for i in total_maturity if i > 1])
        print('Total Maturity', activation)
        plt.title('Maturation of DCs and Random movement of Bacteria ' + ' ' + str(i))
        plt.xlabel('DCY')
        plt.ylabel('DCX')
        plt.imshow(chemo_array[0], origin='lower')
        dendric.arrayupdation()  # Plot of DC
        bac_pop[0].arrayupdation('r*')  # Bacteria plot
        if initial == 1:  # To avoid Error
            im_cell.arrayupdation()  # Immune_cell Plot
        plt.pause(0.5)
        plt.show()
        dendric.movetocenter()  # Center movement of DC_cell


