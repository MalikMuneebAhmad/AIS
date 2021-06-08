import numpy
import matplotlib.pyplot as plt

dc_loc = [(5, 4), (5, 14), (5, 24), (3, 33), (5, 44), (4, 53), (5, 64), (5, 74), (4, 83), (3, 94), (13, 4), (13, 13), (13, 23), (13, 34), (13, 44), (13, 54), (14, 63), (15, 74), (15, 85), (13, 95), (25, 4), (24, 13), (25, 25), (24, 35), (23, 44), (23, 53), (23, 65), (25, 74), (25, 83), (25, 94), (34, 5), (33, 15), (35, 23), (33, 34), (33, 43), (34, 53), (35, 65), (33, 73), (34, 85), (35, 95), (43, 3), (43, 15), (43, 25), (43, 35), (44, 45), (45, 54), (45, 65), (43, 74), (44, 85), (44, 95), (53, 4), (55, 15), (55, 23), (55, 34), (55, 45), (55, 54), (55, 64), (55, 75), (55, 85), (55, 95), (63, 4), (65, 15), (63, 25), (65, 35), (65, 45), (63, 55), (65, 63), (63, 74), (64, 83), (63, 95), (74, 5), (73, 14), (73, 24), (75, 35), (73, 44), (75, 55), (73, 63), (74, 75), (75, 83), (75, 95), (85, 4), (85, 14), (85, 25), (84, 35), (83, 45), (83, 53), (83, 64), (85, 75), (84, 85), (84, 95), (93, 5), (93, 13), (95, 24), (93, 35), (95, 45), (95, 53), (95, 65), (93, 75), (95, 84), (93, 95)]
bac_detected = [[43, 25]]
dc_position = numpy.zeros((100, 100))
dc_loc = list(map(tuple, dc_loc))
bac_detected = list(map(tuple, bac_detected))
immature = set(dc_loc) - set(bac_detected)
immature = list(map(list, immature))
bac_detected = list(map(list, bac_detected))
for i in range(len(immature)):  # Arrayupdation for Immature DCs representation
    dc_position[immature[i][0]][immature[i][1]] = 70
for j in range(len(bac_detected)):  # Arrayupdation for mature DCs representation
    dc_position[bac_detected[j][0]][bac_detected[j][1]] = 106
plt.title('DCs Movement and Bacteria and Maturation of DCs' + ' ' + str(i))
plt.xlabel('DCX')
plt.ylabel('DCY')
plt.imshow(dc_position)