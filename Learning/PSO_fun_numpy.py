import numpy as np
import random
from random import randrange
from numpy import random
# Fitness, pbest and gbest calculation efficiently using numpy
monocytes_x = np.array([50, 25, 75, 12, 62, 37, 87,  6, 56, 31])
monocytes_y = np.array([33, 66, 11, 44, 77, 22, 55, 88,  3, 37])
target = np.array([68, 52])
p = random.randint(80, size = (10,4,2))


def fitness(particles_pos, tar):  # For the calculation of fitness for each particle
    diff = tar - particles_pos
    #print(diff)
    summa = (diff * diff)
    print(summa)
    #summa.sum(axis=2)
    fitness_array = np.sqrt(summa.sum(axis=2))
    return fitness_array


def get_pbest(fitness_value):  # Find out the value and location of pbest of each swarm
    pbestvalue = np.round(np.min(value, axis=1),2)
    pbestloc = np.argmin(value, axis=1)
    print('Swarm pbestloc', pbestloc)
    return pbestvalue, pbestloc

def get_gbest(pbest_val, pbest_loc):  # Find out the value and location of gbest
    gbest_val = np.min(pbest_val)
    gbest_loc = np.argmin(pbest_val)
    #print('particle', particle)
    #print('Swarm gbestloc', particle[[gbest_loc[0]][gbest_loc[1]]])
    return gbest_val, gbest_loc


value = fitness(p, target)
get_pbest_val, get_pbest_loc = get_pbest(value)
#get_gbest_val, get_gbest_loc = get_gbest(get_pbest_val, get_pbest_loc)

