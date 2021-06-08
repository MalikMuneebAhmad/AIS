# Bismillah-ir-Rahman-ir-Rahim
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

from Modules import Chemotaxis
from Modules import Nk_cells
from Modules import DendricCells
from Modules import Bacteria


def plot_examples(colormaps, data):
    n = len(colormaps)
    fig, axs = plt.subplots(1, n, constrained_layout=False, squeeze=False)
    for [ax, cmap] in zip(axs.flat, colormaps):
        psm = ax.pcolormesh(data, cmap=cmap, rasterized=True, vmin=-0, vmax=100)
        fig.colorbar(psm, ax=ax)
    plt.show()


arena = 100
num_bac = 12
num_mac = 5
is_alive = [1] * num_bac
dc_im = np.zeros((arena, arena))
macrophage_array = np.zeros((arena, arena))
monok_array = np.zeros((arena, arena))
danger_mat = np.zeros((arena, arena))
plac_mac = 1
cmap = ListedColormap(["darkorange", "gold", "lawngreen", "lightseagreen"])


for i in range(8):  # Main Loop
    print(i)
    if i == 0:  # Initialisation of objects
        # dendric Cell object created
        dendric = DendricCells(arena)
        im, DCx, DCy = dendric.placement()

        # Bacteria objest created
        bac = Bacteria(arena, num_bac, is_alive)
        bac_x, bac_y, bac_loc1 = bac.placement()

        # Chemotaxis of Bacteria
        bac_chemokine = Chemotaxis(arena, num_bac)
        chemo_array = bac_chemokine.chemo_attractants(is_alive, bac_x, bac_y)  # Array updation of chemokines

    else:
        if i == 6 or 12 or 18:  # Condition to check Bacteria die will work or not
            is_alive = [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1]
    dendric.scanning()  # Dendric Cell movement
    bac_pre, index = dendric.detect_pathogen(bac_loc1)
    pam_mat = dendric.maturity_pamps()
    if len(bac_pre) != 0 or plac_mac == 1:
        bac_pre = list(map(list, bac_pre))
        if plac_mac == 1:
            # Initialisation of AIIS and Macrophages
            # bac_pre = list(map(list, bac_pre))
            mac = Nk_cells(arena, num_mac)
            mono_x, mono_y = mac.placement()
            mac_monokine = Chemotaxis(arena, num_mac)  # Object for monokines is created
            plac_mac = 2
        else:
            # bac_pre = list(map(list, bac_pre))
            macrophage_array = mac.arrayupdation()
            monok_array = mac_monokine.chemo_attractants([1] * num_mac, mono_x, mono_y)

            # Creating object for monokines for macrophges

    bac_x, bac_y, bac_loc1 = bac.move(2)  # Bacteria movement in by stepsize = 1
    chemo_array = bac_chemokine.chemo_attractants(is_alive, bac_x, bac_y)  # Array updation of chemokines
    danger_mat = dendric.maturity_danger(chemo_array)
    dendric.maturity_pamps()
    total_maturity = dendric.commulative_maturity()


    bacteria_im = bac.arrayupdation()  # Array Updation of Bacteria
    dc_im = dendric.arrayupdation()  # Dendric Cell Mask

    z = dc_im + bacteria_im + chemo_array + macrophage_array + monok_array  # Addition of Dendric Cell and Bacteria mask a
    plt.title('DCs Movement and Bacteria and Maturation of DCs' + ' ' + str(i))
    plt.xlabel('DCY')
    plt.ylabel('DCX')
    plt.gcf()
    plt.cla()
    plt.imshow(z)
    plt.show()
    plt.pause(0.5)


    dendric.movetocenter()  # Center movement of DC_cell
    # norm = [float(i)/(2*max(gh)) for i in gh]

# For Plotting data at end of Code
plt.figure(2)
plt.title('Sensor Value')
plt.xlabel('Y')
plt.ylabel('X')
plt.plot(total_maturity)
plt.show()
plot_examples([cmap], z)
