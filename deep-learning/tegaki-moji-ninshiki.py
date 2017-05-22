import numpy as np

# Define Sigmoid Function
def sig(x):
    return 1 / (1 + np.exp(-x))

# Read Test Data
import sys, os
sys.path.append(os.pardir)
import pickle
from dataset.mnist import load_mnist
(x_train, label_train), (x_test, label_test) = load_mnist(normalize=False,flatten=True)

# Display Test Data
number = 0
for i in range(0, 28):
    for j in range(0, 28):
        print("{0:3d}".format(x_test[number][28*i+j]), end=' ')
    print('')
print(label_test[number])
#print(x_test.shape)

'''
# Read Trained Wx and bx Data
with open("sample_weight.pkl", 'rb') as f:
    network = pickle.load(f)
W1, W2, W3 = network['W1'].T, network['W2'].T, network['W3'].T
b1, b2, b3 = network['b1'], network['b2'], network['b3']

#print(W1)
#print(W1.shape)
#print(W2.shape)
#print(W3.shape)
#print(b1.shape)
#print(b2.shape)
#print(b3.shape)
'''

'''
# Calculate and Output Results
z1 = sig( np.dot(W1, x_test[number]/255) + b1 )
z2 = sig( np.dot(W2, z1) + b2 )
z3 = np.dot(W3, z2) + b3
print(z3)
'''

'''
# Evaluate Acuracy
count = 0
for number in range(0, 10000):
    z1 = sig( np.dot(W1, x_test[number]/255) + b1 )
    z2 = sig( np.dot(W2, z1) + b2 )
    z3 = np.dot(W3, z2) + b3
    if (np.argmax(z3) == label_test[number]):
        count = count + 1
print(count)
'''
