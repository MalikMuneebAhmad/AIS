import random
import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


a = 0.2  # learning Rate
n = 3  # Number of inputs
m = 3  # Number of hidden Neurons
l = 1  # Number of O/p Neuron

x1 = np.array([0, 0, 0, 0, 1, 1, 1, 1])
x2 = np.array([0, 0, 1, 1]*2)
x3 = np.array([0,1] * 4)
xi = np.array([x1, x2, x3])
y_dk = np.array([0, 1, 1, 0, 1, 0, 0, 1])  # [ydk]

# Step no.1 Initialisation Declaration of weights and Threshold

w_ij = np.random.uniform(-2.4 / n, 2.4 / n, size=(n, m, 2**n))
w_jk = np.random.uniform(-2.4 / n, 2.4 / n, size=(m, 2**n))

theta_j = np.random.uniform(-2.4 / n, 2.4 / n, size=(m, 1))
theta_k = np.random.uniform(-2.4 / n, 2.4 / n, size=(1, l))
p = 1
sum_error = 4
e = list()

while sum_error > 0.01:
    # Step no.2 Activation of back-propagation neural network

    # (a) Calculation of Hidden Layer Output
    y_j = sigmoid((xi * w_ij[:][:]).sum(axis=1) - theta_j)
    #print('Hidden Layer Output', y_j)

    # (b) Calculation of Final Output
    y_k = sigmoid((y_j * w_jk).sum(axis=0) - theta_k)
    #print('Total Actual Output', y_k)

    # Step no.3 Weight Training

    # (a) Error Gradient for the Neuron in the Output layer
    e_k = y_dk - y_k
    #print('Error in Output layer', e_k)
    delta_k = y_k * (1 - y_k) * e_k  # Error Gradient

    # Update the weights at the output neuron
    delta_w_jk = a * (y_j * delta_k)
    w_jk = w_jk + delta_w_jk
    #print('Updated Value of w_jk', w_jk)

    # (b) Calculate the error gradient for the neurons in the hidden layer
    delta_j = y_j * (1-y_j)*(delta_k * w_jk)
    delta_w_ij = np.array([delta_j * x for x in xi])
    w_ij = w_ij + delta_w_ij

    error_sq = e_k * e_k
    sum_error = np.sum(error_sq)
    e.append(sum_error)
    print('Sum of Error in Output layer', sum_error, 'in iterations', p)
    p = p + 1

print('Computed O/P', y_k)
plt.scatter(np.arange(1,p), e, label="circle", color="blue", marker="*", s = 10)
plt.show()


