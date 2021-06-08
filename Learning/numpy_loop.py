import numpy as np

# Update value in an array using "nditer"
a = np.zeros(80).reshape(10,4,2)
arr = np.arange(24).reshape(4, 3, 2)
dist = np.arange(20).reshape(10, 2)
val = np.array([[21, 26, 31, 26],[48, 49, 40, 45],[44, 37, 39, 41],[60, 52, 52, 56],[20, 20, 28, 25],
       [44, 48, 41, 43], [17, 100, 16, 19], [72, 65, 69, 71], [46, 54, 45, 50], [43, 38, 36, 39]])
arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
pbest_values = np.array([32.558, 47.854, 46.174, 61.392, 30.15, 48.104, 24.083, 73.348, 55.362, 46.519])
w = 0.4
c1 = 2
c2 = 2
velocity_particle = np.ones(80).reshape(10,4,2)*0.4
P = np.array([ -27.3164154, -114.56392617])
# change the dtype to 'float64'


def index_iter(ar):  # Function to change values of each array
    for x in np.nditer(ar, op_flags=['readwrite']):
        x[...] = x - 1
    return ar


def get_index(arra, target):  # Loop through index of Array
    dist = np.zeros(12).reshape(4, 3)
    for idx in np.ndindex(arra.shape[:2]):
        point = arra[idx]
        dist[idx] = (point[0] - target[0]) + (point[1] - target[1])
        print(idx, arra[idx], dist[idx])
    return arra, dist


def get_pbest(arra):  # Loop through index of Array
    #pbest = np.arange(20).reshape(10, 2)
    loc = list()
    final = list()
    result = list()
    for idx in np.ndindex(arra.shape[:1]):
        a = arra[idx]
        result = np.argmax(arra[idx])
        swarm_max = np.amax(a)
        final.append(swarm_max)
        loc.append([idx[0], result])
    print(final, loc)
    return final, loc


def get_gbest(arra):
    gbest_val = np.max(arra)
    gbest_loc =np.argmax(arra)
    return gbest_val, gbest_loc


def maturity_value(x):
    switcher = {
        0.0: 10,  # Value for Immature
        0.45: 30,  # Value for Semi-mature
        0.90: 50,  # Value for Fully mature
        1.35: 70,  # value when fully saturated
    }
    return switcher.get(x, "Invalid maturity value")


def week(i):
    switcher = {
        0: 'Sunday',
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday'
    }
    return switcher.get(i, "Invalid day of week")

def update_velocity(w, c1, c2, v, G, pbest_loc, s, k):
    r1 = np.array([random.random()] * 4).reshape(4,1)
    r2 = np.array([random.random()] * 4).reshape(4,1)
    P = particle[pbest_loc[s][0]][pbest_loc[s][1]]
    X = particle[s]
    v[s] = (w * v[s]) + (c1 * r1) * (P-X) + (c2 * r2) * (G-X)
    return v
# To access the index of an entry
#for idx, x in np.ndenumerate(a):
    #print('DC number {0} and maturation value {1}'.format(idx, x))



#print(maturity_value(0.45))

pbest_v, location = get_pbest(val)
gbest_v, gbest_loc = get_gbest(pbest_v)
#index_iter(a)
#get_index(arr, [8, 9])
