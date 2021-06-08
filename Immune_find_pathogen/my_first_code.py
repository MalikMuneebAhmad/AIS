# Bismillah-ir-Rahman-ir-Rahim
import matplotlib.pyplot as plt
import numpy as np
from Modules import Bacteria
from Modules import DendricCells
from Modules import Chemotaxis
from Modules import Immune_cells
from Modules import Inflammation

#arena_x = int(input('Enter number of arena x-axis -->  '))
#arena_y = int(input('Enter number of arena x-axis -->  '))
initial = 0
arena_x = 100
arena_y = 100
types_bac = 3
type_im_cell = 1
bac_x = [[] for _ in range(types_bac)]
bac_y = [[] for _ in range(types_bac)]
bac_loc1 = [[] for _ in range(types_bac)]
num_bac = [10, 12, 8]
is_alive = [[1] * i for i in num_bac]
exp_area_bac = [3, 5, 4]
bac_plac = [[20, 20], [20, 80], [70, 70]]
chemo_array = [np.array([]) for _ in range(types_bac)]
int_damage = [np.array([]) for _ in range(types_bac)]
marker = ['r*', 'g*', 'y*']
no_im_cells = 0
activation = 0
mono_array = np.zeros([arena_x, arena_y]) # To just decalare, will be used later
total_maturity = []

for i in range(50):  # Main Loop
    print('Iteration No. ', i)
    if i == 0:  # for initialization of dendric-Cell, bacteria and chemotaxis of bacteria
        # dendric Cell object created
        dendric = DendricCells(arena_x, arena_y)
        no_dc, dc_x, dc_y = dendric.placement(0.01)

        # Bacteria objest created
        bac_pop = [Bacteria(arena_x, arena_y, num) for num in num_bac]

        # Chemotaxis of Bacteria
        bac_chem = [Chemotaxis(arena_x, arena_y, num) for num in num_bac]  # Object

        for type_bac in range(types_bac): # for placement and chemo array of each bacteria
            bac_x[type_bac], bac_y[type_bac], bac_loc1[type_bac] = bac_pop[type_bac].cluster(exp_area_bac[type_bac], bac_plac[type_bac])
            chemo_array[type_bac] = bac_chem[type_bac].chemo_attractants(is_alive[type_bac], bac_x[type_bac], bac_y[type_bac])  # Array updation of chemokines

        # Initialization of Inflammation object
        measure_inflam = Inflammation(types_bac, num_bac)
        inflam = measure_inflam.perc_inflam(num_bac)
        #print('Initial Inflammation', inflam)

    else:  # Main Loop after Initialization
        if activation >= 1 and initial == 0:  # Condition to initialize Innate Immune Response
            no_im_cells = 12
            imm_alive = [1] * no_im_cells
            im_cell = Immune_cells(arena_x, arena_y, no_im_cells)
            im_cellx, im_celly = im_cell.cluster(3, [50, 50])

            # Initialization of Monokine of Immune Cell
            mac_chem = Chemotaxis(arena_x, arena_y, no_im_cells)
            mono_array = mac_chem.chemo_attractants(imm_alive, im_cellx, im_celly)  # Array updation of Monokines
            initial = 1

        dendric.scanning()  # Dendric Cell movement

        for type_bac in range(types_bac):  # detection of pathogen and danger signal by DC
            #print('bac_loc1[type_bac]',bac_loc1[type_bac])
            dendric.detect_pathogen(bac_loc1[type_bac])  # detection of pathogen
            bac_x[type_bac], bac_y[type_bac], bac_loc1[type_bac] = bac_pop[type_bac].move('Active')  # Bacteria movement in by stepsize = 1
            chemo_array[type_bac] = bac_chem[type_bac].chemo_attractants(is_alive[type_bac], bac_x[type_bac], bac_y[type_bac])  # Array updation of chemokines
            int_damage[type_bac] = bac_pop[type_bac].internal_cellular_effect(3, 2)
            dendric.maturity_danger1(int_damage[type_bac])  # Detection of Danger signal

        if initial == 1: # After activation
            #if (inflam > 0.5) and i > 90:
                #print('Call for T-Cell')
            print('Total Maturity', sum(total_maturity))
            mono_array = mac_chem.chemo_attractants(imm_alive, im_cellx, im_celly)  # Array updation of Monokines
            grad = im_cell.gradient(sum(chemo_array), mono_array)
            im_cellx, im_celly = im_cell.random_movementall(grad)
            #mono_array = mac_chem.chemo_attractants(imm_alive, im_cellx, im_celly)  # Array updation of Monokines
            for type_bac in range(types_bac):
                bac_pop[type_bac].num_bac, bac_pop[type_bac].bacteria_x, bac_pop[type_bac].bacteria_y, bac_pop[type_bac].is_alive = im_cell.kill_bac(bac_pop[type_bac].num_bac, bac_x[type_bac], bac_y[type_bac], bac_pop[type_bac].is_alive)
                print('Bacteria alive', len(bac_pop[type_bac].is_alive))
            inflam = measure_inflam.perc_inflam([len(bac_pop[i].is_alive) for i in range(types_bac)])
            print('Current Inflammation', inflam)

        total_maturity = dendric.commulative_maturity()
        activation = len([i for i in total_maturity if i > 1])
        print('Activation--', activation)
        plt.title('Maturation of DCs and Random movement of Bacteria ' + ' ' + str(i))
        plt.xlabel('DCY')
        plt.ylabel('DCX')
        mask = sum(chemo_array) + mono_array
        plt.imshow(mask, origin='lower')
        dendric.arrayupdation()  # Plot of DC

        # Plot of bacteria
        for type_bac in range(types_bac):
            bac_pop[type_bac].arrayupdation(marker[type_bac])  # Bacteria plot

        # plot of immune Cell
        if initial == 1:  # To avoid Error if immune Cell was not active
            im_cell.arrayupdation()  # Immune_cell Plot
        plt.pause(0.5)
        plt.show()
        dendric.movetocenter()  # Center movement of DC_cell

measure_inflam.plot_inflam()  # To show plot of inflammation