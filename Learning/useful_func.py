import numpy as np


def list_match(List1, List2):
    check = list()
    # Iterate in the 1st list
    for m in List1:
        # Iterate in the 2nd list
        for n in List2:
            # if there is a match
            if m == n:
                print(m)
                check.append(m)
    return check


def xor(a, b):
    r = list()
    for i in range(len(a)):
        v = a[i] ^ b[i]
        r.insert(i, v)
    return r


def dec(y_array, theta):
    y = list()
    for i in range(4):
        if y_array[i] >= theta:
            y.append(1)
        else:
            y.append(0)
    return y


def dot(K, L):
    if len(K) != len(L):
        return 0
    return sum(i[0] * i[1] for i in zip(K, L))


c = dot([2,5,8],[5,-1,2])

# x1 = [0, 0, 1, 1]
# x2 = [0, 1, 0, 1]
# r = xor(x1, x2)
# print(r)

#a = np.array([0.0, -0.1, 0.2, 0.1])

#e = dec(a, 0.2)
