import numpy as np
import random
from random import randrange
import matplotlib.pyplot as plt
import math
#from numpy import random


# Initial Location of Swarm Center/ Monocytes (These points are obtained by using Halton Distribution)
monocytes_x = np.array([50, 25, 75, 12, 62, 37, 87,  6, 56, 31])
monocytes_y = np.array([33, 66, 11, 44, 77, 22, 55, 88,  3, 37])

particle = np.zeros(80).reshape(10,4,2)
target = [68, 52]
particle_x = list()  # list of all x-co-ordinates
particle_y = list()  # list of all y-co-ordinates
wmin = 0.7
wmax = 0.9
n_iterations = 20
w = np.linspace(wmin, wmax, n_iterations)  # LDIWM implementation
c1 = 2
c2 = 1
velocity_particle = np.ones(80).reshape(10,4,2)*0.2
G = np.array([6, 1])


def neighbor_particle(no_member, mono_x, mono_y):  # Function to place neighboring element of a Swarm
    swarm_x = list()
    swarm_y = list()
    for i in range(no_member):
        swarm_x.append(mono_x + ((-1) ** (bool(random.getrandbits(1)))) * randrange(3,6))
        swarm_y.append(mono_y + ((-1) ** (bool(random.getrandbits(1)))) * randrange(3,6))
    swarm_loc = [[i, j] for i, j in zip(swarm_x, swarm_y)]
    swarm_loc.append([mono_x, mono_y])
    print('swarm loc', swarm_loc)
    return swarm_x, swarm_y, swarm_loc


def fitness(particles_pos, target):  # For the calculation of fitness for each particle
    fitness_array = np.zeros(40).reshape(10, 4)
    for idx in np.ndindex(particles_pos.shape[:2]):
        member = particles_pos[idx]
        fitness_array[idx] = round(math.sqrt(((target[0] - member[0])**2) + ((target[1] - member[1])**2)), 3)
    return fitness_array

'''def fitness(particles_pos, target):  # For the calculation of fitness for each particle
    diff = target - particles_pos
    summa = (diff * diff)
    summa.sum(axis = 2)
    fitness_array = np.sqrt(summa)
    return fitness_array'''



def get_pbest(fitness_value):  # Find out the value and location of pbest of each swarm
    pbestloc = list()  # Location of best local particle
    pbestvalue = list()  # values of best local particle
    result = list()
    for swarm_no in np.ndindex(fitness_value.shape[:1]):
        swarm_fitness = fitness_value[swarm_no]
        member_loc = np.argmin(fitness_value[swarm_no]) # location where minimum value exist
        pbestloc.append([swarm_no[0], member_loc])
        swarm_min = np.amin(swarm_fitness) # Find out min value
        pbestvalue.append(swarm_min)
    print('Swarm pbestloc', pbestloc)
    return pbestvalue, pbestloc


def get_gbest(pbest_val, pbest_loc):  # Find out the value and location of gbest
    gbest_val = np.min(pbest_val)
    a = np.argmin(pbest_val)
    gbest_loc = np.array(pbest_loc[a])
    print('particle', particle)
    #print('Swarm gbestloc', particle[[gbest_loc[0]][gbest_loc[1]]])
    return gbest_val, gbest_loc


def update_velocity(w, c1, c2, v, G, pbest_loc, s, k):
    r1 = np.array([random.random()] * 4).reshape(4,1)
    r2 = np.array([random.random()] * 4).reshape(4,1)
    P = particle[pbest_loc[s][0]][pbest_loc[s][1]]
    #print('P', P)
    X = particle[s]
    v[s] = (w * v[s]) + (c1 * r1) * (P-X) + (c2 * r2) * (G-X)
    return v


for j in range(10):  # Loop to Store location of all particles
    swarm_x, swarm_y, particle[j] = neighbor_particle(3, monocytes_x[j], monocytes_y[j])
    particle_x = particle_x + swarm_x
    particle_y = particle_y + swarm_y

#for x in np.nditer(particle[:, ::2]):
  #print(x)
# x = random.rand(3, 5)  Creating an array of random number

for k in range(n_iterations):
    val = fitness(particle, target)
    #print('Fitness value is ', val)
    pbest_value, pbest_loc = get_pbest(val)
    gbest_value, gbest_loc = get_gbest(pbest_value, pbest_loc)

    for s in range(10):
        # Update global best
        gle = particle[gbest_loc[0]][gbest_loc[1]]
        print("gbest", gle)
        velocity_particle = update_velocity(w[k], c1, c2, velocity_particle, gle, pbest_loc, s, k)
        particle = particle + velocity_particle

particle_plot = particle.reshape(40,2)
#plt.scatter(er[0:40,0],er[0:40,1], color = 'red')
plt.scatter(target[0], target[1], color = 'black')
plt.scatter(monocytes_x,monocytes_y)
plt.scatter(particle_x, particle_y, color = 'red')
plt.show()