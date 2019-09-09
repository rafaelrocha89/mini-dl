# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 15:08:27 2019

@author: Rafael Rocha
"""

import numpy as np
from sklearn.metrics import mean_squared_error

x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
t = np.array([[0],[1],[1],[0]])

D = np.size(x,1)
N = np.size(x,0)
M = 5
K = 1

b = np.ones([N,1]) # Bias
xb = np.concatenate([b, x], axis=1) # Entrada com bias

print(np.concatenate([xb,t], axis=1))

w1 = np.random.rand(M,D+1)
w2 = np.random.rand(K,M+1)

a = np.matmul(w1, xb.T)
z = np.tanh(a)

b = np.ones([1,N]) # Bias
zb = np.concatenate([b, z]) # Entrada com bias

y = np.matmul(w2, zb)

print('\n')
print(np.concatenate([t,y.T], axis=1))

# Sum-of-squares error
sse = 0.5*np.sum((y-t.T)**2)

print('\n')
#print(mean_squared_error(t, y.T))
print(sse)

deltak = y-t.T
deltaj = (1-(zb**2))*np.sum(w2*deltak.T)