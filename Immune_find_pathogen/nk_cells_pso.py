from matplotlib import colors
import numpy as np
import random
import matplotlib.pyplot as plt
from Modules import Chemotaxis


def mhc_complexes(x, y, chemotaxis):   # Can be used as fitness function for each particle of swarm in PSO or finding sensory value of chemokine around Immune-Cell
    f = ((1 / 9) * (
            chemotaxis[x - 1][y + 1] + chemotaxis[x][y + 1] + chemotaxis[x + 1][y + 1] + chemotaxis[x - 1][y] +
                chemotaxis[x][y] + chemotaxis[x + 1][y] + chemotaxis[x - 1][y - 1] + chemotaxis[x][y - 1] +
                chemotaxis[x + 1][y - 1]))
    return f
# monocytes_x = array([50, 25, 75, 12, 62, 37, 87,  6, 56, 31])
# monocytes_y = array([33, 66, 11, 44, 77, 22, 55, 88,  3, 37])

class Nk_cells:
    p = 0.125

    def __init__(self, arena_size, num_cells):
        self.arena_size = arena_size  # Arena Size Defined by User
        self.num_cells = num_cells  # No of Immune Cells
        self.monocytes_x = []  # Monocytes X location
        self.monocytes_y = []  # Monocytes y location
        self.monocytes_loc = []  # Monocytes location in the form pairs
        self.monocytes_position = np.array([])
        self.monocytes_array = np.zeros((self.arena_size, self.arena_size))  #
        self.monocytes_gradientx = [0] * num_cells
        self.monocytes_gradienty = [0] * num_cells
        self.monokines = np.zeros((self.arena_size, self.arena_size))
        self.cells_presence = [1] * num_cells
        self.monocytesmovedx = list()
        self.monocytesmovedy = list()

    def placement(self):  # Placement of Immune Cell b
        for i in range(self.num_cells):
            x = random.randrange(40, 60)  # Random number generation in X-axis
            y = random.randrange(40, 60)  # Random number generation in Y-axis
            self.monocytes_x.append(x)  # Monocytes X location Updated
            self.monocytes_y.append(y)  # Monocytes y location updated
            # monocytes_x = array([50, 25, 75, 12, 62, 37, 87,  6, 56, 31])
            # monocytes_y = array([33, 66, 11, 44, 77, 22, 55, 88,  3, 37])
            self.monocytes_loc.append(tuple([x, y]))
        return self.monocytes_x, self.monocytes_y

    def gradient(self, chemokines, monokines):
        for i in range(self.num_cells):
            x = self.monocytes_x[i]
            y = self.monocytes_y[i]
            self.monocytes_gradientx[i] = chemokines[x + 1][y] - chemokines[x - 1][y] - 0.005 * monokines[x + 1][y] - \
                                          monokines[x - 1][y]
            self.monocytes_gradienty[i] = chemokines[x][y + 1] - chemokines[x][y - 1] - 0.005 * monokines[x][y + 1] - \
                                          monokines[x][y - 1]
        return self.monocytes_gradientx, self.monocytes_gradienty

    def random_movement(self):  # More exploraion
        self.monocytes_loc.clear()
        for i in range(len(self.monocytes_x)):
            r = random.random()  # random number to move DC
            # print(r)
            if r < Nk_cells.p:  # DC move Upper-Left
                self.monocytes_x[i] = self.monocytes_x[i] - 1
                self.monocytes_y[i] = self.monocytes_y[i] + 1
                # print('Upper-Left')
            elif Nk_cells.p <= r < 2 * Nk_cells.p:  # DC move UP
                self.monocytes_y[i] = self.monocytes_y[i] + 1
                # print('Up')
            elif 2 * Nk_cells.p <= r < 3 * Nk_cells.p:  # DC move Upper-Right
                self.monocytes_x[i] = self.monocytes_x[i] + 1
                self.monocytes_y[i] = self.monocytes_y[i] + 1
                # print('Upper-Right')
            elif 3 * Nk_cells.p <= r < 4 * Nk_cells.p:  # DC move Right
                self.monocytes_x[i] = self.monocytes_x[i] + 1
                # print('Right')
            elif 4 * Nk_cells.p <= r < 5 * Nk_cells.p:  # DC move Down-Rght
                self.monocytes_x[i] = self.monocytes_x[i] + 1
                self.monocytes_y[i] = self.monocytes_y[i] - 1
                # print('Down-Rght')
            elif 5 * Nk_cells.p <= r < 6 * Nk_cells.p:  # DC move Down
                self.monocytes_y[i] = self.monocytes_y[i] - 1
                # print('Down')
            elif 6 * Nk_cells.p <= r < 7 * Nk_cells.p:  # DC move Left-Down
                self.monocytes_x[i] = self.monocytes_x[i] - 1
                self.monocytes_y[i] = self.monocytes_y[i] - 1
                # print('Down-Left')
            elif 7 * Nk_cells.p <= r < 8 * Nk_cells.p:  # DC move Left
                self.monocytes_x[i] = self.monocytes_x[i] - 1
                # print('Left')
            self.monocytes_loc.insert(i, [self.monocytes_x[i], self.monocytes_y[i]])
            # print(self.dcmovedx)
        # print(self.dcmovedy)
        # dendricCells.value()
        return self.monocytes_x, self.monocytes_y, self.monocytes_loc  # Updated Location of DC

    def pso_movement(self, w, c1, c2):
        monocyte_pos = np.array([self.monocytes_x, self.monocytes_y])
        # monocytes_v = (w * monocytes_v) + (c1 * random.random())*(pbest - monocyte_pos ) +
        monocytes_x = self.monocytes_x
        pass

    def arrayupdation(self):  # Macrophages Array Updation
        self.monocytes_array = np.zeros((self.arena_size, self.arena_size))
        for i in range(self.num_cells):  # Macrophages Mask Updated
            self.monocytes_array[self.monocytes_x[i]][self.monocytes_y[i]] = 50
        return self.monocytes_array


class Space:
    def __init__(self, target, target_error, n_particles):
        self.target = target
        self.target_error = target_error
        self.n_particles = n_particles
        self.particles = []
        self.gbest_value = float('inf')
        self.gbest_position = np.array([random.random() * 50, random.random() * 50])

    def print_particles(self):
        for particle in self.particles:
            particle.__str__()

    def fitness(self, particle):  # MEASURE THE FITNESS OF EQUATION X2 + Y2 +1
        return particle.position[0] ** 2 + particle.position[1] ** 2 + 1

    def set_pbest(self):  # FIND THE BEST LOCAL CANDIDATE FROM ONE SWARM (lOCAL MINIMA)
        for particle in self.particles:
            fitness_cadidate = self.fitness(particle)
            if particle.pbest_value > fitness_cadidate:
                particle.pbest_value = fitness_cadidate
                particle.pbest_position = particle.position

    def set_gbest(self):  # FIND THE BEST GLOBAL CANDIDATE FROM ONE SWARM (GLOBAL MINIMA)
        for particle in self.particles:
            best_fitness_cadidate = self.fitness(particle)
            if self.gbest_value > best_fitness_cadidate:
                self.gbest_value = best_fitness_cadidate
                self.gbest_position = particle.position

    def move_particles(self):  # UPDATE THE VELOCITIES OF AGENTS OR SWARMS
        for particle in self.particles:
            global W
            new_velocity = (W * particle.velocity) + (c1 * random.random()) * (
                    particle.pbest_position - particle.position) + \
                           (random.random() * c2) * (self.gbest_position - particle.position)
            particle.velocity = new_velocity
            particle.move()  # METHOD USED FROM particles CLASS TO UPDATE LOCATION


'''arena = 100
bac = Chemotaxis(arena, 10)  # Object for chemokines is created
chemo = bac.chemo_attractants([1, 0, 1, 0, 1, 1, 0, 1, 1, 1], [7, 11, 12, 17, 11, 12, 19, 17, 13, 13],
                              [81, 81, 73, 80, 76, 81, 80, 79, 79, 79])

# Object for monocytes is created

monocytes = Nk_cells(arena, 10)  # Object for monocytes is created
mono_x, mono_y = monocytes.placement()  # Monocytes are placed
mono_loca = monocytes.arrayupdation()  # Array of monocytes is updated

# Object for monokines is created

a = Chemotaxis(arena, 10)
monokines = a.chemo_attractants([1] * 10, mono_x, mono_y)

gradientx = monocytes.gradient(chemo, monokines)

for t in range(10):
    plt.title('Monocytes Movement ' + str(t))
    plt.xlabel('Monocytes-X')
    plt.ylabel('Monocytes-Y')
    plt.imshow(mono_loca + monokines + chemo)
    plt.show()
    mono_x, mono_y, mono_location = monocytes.random_movement()
    monokines = a.chemo_attractants([1] * 10, mono_x, mono_y)  # Monokines of Immune Cell
    mono_loca = monocytes.arrayupdation()  # Array of monocytes is updated'''
