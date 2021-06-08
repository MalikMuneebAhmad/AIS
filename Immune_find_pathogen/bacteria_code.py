import random
import numpy
x = random.randrange(4, 96)
y = random.randrange(4, 96)
bactx = list(range(x-2,x+3))
bacty = list(range(y-2,y+3))
bacteria_position1 = numpy.zeros((100,100))
bacteria_loc = list()
new_bacteria_loc = list()
#bacteria_position[15][15] = 50
n = 0
for i in range(5):
    for j in range(5):
        o = bactx[i]
        p = bacty[j]
        bacteria_loc.insert(n,[o,p])
        n += 1
        #bacteria_position[i][j] = 30

new_bacteria_loc += random.sample(bacteria_loc, 10)

for k in range(10):
    bacteria_position1[new_bacteria_loc[k][0]][new_bacteria_loc[k][1]] = 30