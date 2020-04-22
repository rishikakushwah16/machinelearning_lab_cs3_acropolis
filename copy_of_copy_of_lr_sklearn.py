# -*- coding: utf-8 -*-
"""Copy of Copy of LR_SKLEARN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cIurxto-SliROzk0rtAzaefwpZHmI6b5
"""

import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score

"""PREPARING THE DATASET"""

data = {'Hours':[2.5,5.1,3.2,8.5,3.5,1.5,9.2,5.5,8.3,2.7,7.7,5.9,4.5,3.3,1.1,8.9,2.5,1.9,6.1,7.4,2.7,4.8,3.8,6.9,7.8], 
        'Scores':[21,47,27,75,30,20,88,60,81,25,85,62,41,42,17,95,30,24,67,69,30,54,35,76,86]} 
  
# Create DataFrame 
student_scores = pd.DataFrame(data) 
  
# Print the output. 
student_scores

"""SEPARATING THE DEPENDENT AND INDEPENDENT VARIABLES"""

X = student_scores.iloc[ : ,   : 1 ].values
Y = student_scores.iloc[ : , 1].values
print(X)
print(Y)

"""SPLITTING THE DATASET INTO TRAIN AND TEST SETS"""

X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size = 1/3, random_state = 0)



"""X_test"""

print(X_train)

print(X_test)

print(Y_train)

plt.scatter(X,Y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

Y_pred = regressor.predict(X_test)

regressor = LinearRegression()
regressor = regressor.fit(X_train, Y_train)

plt.scatter(X_test , Y_test, color = 'red')
plt.plot(X_test , regressor.predict(X_test), color ='blue')

Y_pred = regressor.predict(X_test)
print(Y_pred)

plt.scatter(X_train , Y_train, color = 'green')
plt.plot(X_train , regressor.predict(X_train), color ='red')

plt.scatter(X_test , Y_test, color = 'red')
plt.plot(X_test , regressor.predict(X_test), color ='blue')

print(mean_squared_error(Y_test, Y_pred))
print(r2_score(Y_test, Y_pred))