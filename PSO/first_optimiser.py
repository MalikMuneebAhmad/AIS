import random
import numpy as np

W = 0.4
c1 = 0.8
c2 = 0.9    

n_iterations = int(input("Inform the number of iterations: "))
target_error = float(input("Inform the target error: "))
n_particles = int(input("Inform the number of particles: "))


class Particle:
    def __init__(self):  # will be used for placing random macrophages
        self.position = np.array([((-1) ** (bool(random.getrandbits(1))) * random.random() * 50) + 50,
                                  ((-1) ** (bool(random.getrandbits(1))) * random.random() * 50) + 50])
        #self.position = np.array(round(random.random()*100),round(random.random()*100))
        self.pbest_position = self.position
        self.pbest_value = float('inf')
        self.velocity = np.array([0, 0])

    def __str__(self):
        print("I am at ", self.position, " meu pbest is ", self.pbest_position)

    def move(self):  # update the position of macrophage
        self.position = self.position + self.velocity


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

    def set_gbest(self): # FIND THE BEST GLOBAL CANDIDATE FROM ONE SWARM (GLOBAL MINIMA)
        for particle in self.particles:
            best_fitness_cadidate = self.fitness(particle)
            if self.gbest_value > best_fitness_cadidate:
                self.gbest_value = best_fitness_cadidate
                self.gbest_position = particle.position

    def move_particles(self): # UPDATE THE VELOCITIES OF AGENTS OR SWARMS
        for particle in self.particles:
            global W
            new_velocity = (W * particle.velocity) + (c1 * random.random()) * (
                        particle.pbest_position - particle.position) + \
                           (random.random() * c2) * (self.gbest_position - particle.position)
            particle.velocity = new_velocity
            particle.move()  # METHOD USED FROM particles CLASS TO UPDATE LOCATION

    def arrayupdation(self):
         pass



search_space = Space(1, target_error, n_particles)  # OBJECT CREATED OF CLASS SPACE
particles_vector = [Particle() for _ in range(search_space.n_particles)]  # OBJECT CREATED OF CLASS SPACE
search_space.particles = particles_vector
search_space.print_particles()

iteration = 0
while iteration < n_iterations:
    search_space.set_pbest()
    search_space.set_gbest()

    if abs(search_space.gbest_value - search_space.target) <= search_space.target_error:
        break

    search_space.move_particles()
    iteration += 1

print("The best solution is: ", search_space.gbest_position, " in n_iterations: ", iteration)
