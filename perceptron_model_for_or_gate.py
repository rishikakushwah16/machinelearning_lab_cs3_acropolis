# -*- coding: utf-8 -*-
"""Perceptron_Model_For_OR_Gate.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JINOFhunX8dU2bkS1tduW2wL7PM01JxJ
"""

class Perceptron:
  def __init__(self, input_size, lr=0.001, epochs=100):
    self.W = np.zeros((input_size+1,1))
    self.epochs = epochs
    self.lr = lr
    self.loss_lst =[]
    
  def activation_fn(self, x):
    return 1 if x >= 0 else 0

  def predict(self, x):
    z = self.W.T.dot(x)
    a = self.activation_fn(z)
    return a

  def fit(self, X, d):
    for _ in range(self.epochs):
      l=0
      for i in range(d.shape[0]):
        x = np.insert(X[i], 0, 1)
        x = x.reshape((3,1))
        y = self.predict(x)
        e = d[i] - y
        l+=e**2
        self.W = self.W + self.lr * e * x
      l=l/4
      self.loss_lst.append(l)





import numpy as np
if __name__ == '__main__':
    X = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])
    d = np.array([0, 1, 1, 1])
 
    model = Perceptron(input_size=2)
    model.fit(X, d)
    print(model.W)

import matplotlib.pyplot as plt
x_axis = [int(x) for x in range(100)]
y_axis= model.loss_lst
plt.plot(x_axis,y_axis)
plt.xlabel("iteration")
plt.ylabel("loss")
plt.show()

