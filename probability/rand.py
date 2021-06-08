import random

l = list()
for i in range(50):
    x = (-1) ** bool(random.getrandbits(1))
    l.append(x)

print(l)