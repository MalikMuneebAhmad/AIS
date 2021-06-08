import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_axes([0.05, 0.05, 0.95, 0.95])


def d():
    save = np.zeros(50)
    c = list()
    for i in range(50):
        x = random.random()
        save[i] = x
    result = list(np.round(save, 1))
    for j in range(1,11):
        c1 = result.count(j/10)
        c.append(c1)
    return c


# Randomly generated Data
ob1 = d()

#Plot of histogram of data
ax.bar(list(range(1, 11)), ob1)
plt.show()

# Kernel Density Estimation Plot
#sns.kdeplot(ob1, shade=True, bw=0.5)
#plt.show()

# Kernel Density Estimation Plot
sns.distplot(ob1, rug=True, hist=True)
plt.show()


