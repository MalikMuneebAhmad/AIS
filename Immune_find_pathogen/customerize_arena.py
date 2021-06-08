from Modules import DendricCells
from Modules import Bacteria
import matplotlib.pyplot as plt

import math

arena_x = 100
arena_y = 90
dc_density = 0.01
num_bac1 = 8
mode_bac1 = 'active'
dendric = DendricCells(arena_x, arena_y)
no_dc, dc_centerx, dc_centery = dendric.uniform(0.01)
bac_1 = Bacteria(arena_x, arena_y, mode_bac1)
bac_1.bacteria_x, bac_1.bacteria_y = bac_1.cluster(num_bac1, 7, [40, 40])
print(dendric.cell_x)
#bac1_x, bac1_y = bac_1.move('Active')

plt.title('Flexible arena size')
plt.xlim(0, arena_y)
plt.ylim(0, arena_x)
plt.xlabel('Y')
plt.ylabel('X')
plt.plot(dc_centery, dc_centerx, 'b.')
bac_1.arrayupdation('r*')
#bac_1.arrayupdation('r*')
plt.show()