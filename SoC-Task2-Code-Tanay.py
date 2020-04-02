# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T4fZlxRzHrvBsWhTn_r08WzdWTkYTLLe
"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline

import matplotlib.pyplot as plt
import random
import time
from random import seed
import numpy as np

from random import randint

run = 0
xxaxis = []
yyaxis = []

for j in range(1000):
  print(j)
  seed(time.time())

  array = np.zeros(10000)
  array[4999] = 1
  niters = 0
  # xaxis = [0]
  # yaxis = [1]

  while(True):
    niters += 1			
    count = 0
    set1 = np.random.randint(0, 9999, 5)		#create 2 arrays of size 5 each to swap indices
    set2 = np.random.randint(0, 9999, 5)
    for i in range(5):
      temp = array[set1[i]]
      array[set1[i]] = array[set2[i]]
      array[set2[i]] = temp

    for _ in range(10000):
      if array[_] == 1:
        v1 = random.random()
        v2 = random.random()				#changing the entry to 1 with 0.35 probability
        if v1<=0.35:
          array[(_ + 9999)%10000] = 1
        if v2<=0.35:
          array[(_ + 1)%10000] = 1
    
    for _ in range(10000):
      count += array[_]
    # xaxis.append(niters)
    # yaxis.append(count)
    if count == 10000:
      break

  xxaxis.append(j+1)
  yyaxis.append(niters) 
  
plt.plot(xxaxis, yyaxis)
plt.xlabel("#run")
plt.ylabel("#iterations")
print(np.mean(yyaxis))
print ("iterations needed", niters)
plt.savefig("SoC -Plot2-Tanay.jpg")

import numpy as np
import matplotlib.pyplot as plt
import random
from random import seed
from random import randint
import time
from scipy.signal import savgol_filter



xaxis = []
x_axis = [0]
yaxis = []
seed(time.time())
nones = [1]
array = np.zeros(10000)
array[4999] = 1
iters = 0

while(True):
  iters += 1
  set1 = np.random.randint(0, 9999, 5)
  set2 = np.random.randint(0, 9999, 5)
  for _ in range(5):
    temp = array[set1[_]]
    array[set1[_]] = array[set2[_]]
    array[set2[_]] = temp
  
  for _ in range(10000):
    if array[_] == 1:
      val1 = random.random()
      val2 = random.random()
      if val1<= 0.35:
        array[(_ + 9999)%10000] = 1
      if val2<= 0.35:
        array[(_ + 1)%10000] = 1
      
  count = 0
  for _ in range(10000):
    count += array[_]
  x_axis.append(iters)
  xaxis.append(iters)
  nones.append(count)
  yaxis.append(count - nones[iters-1])
  if count >= 10000: 
    break


plt.plot(xaxis, yaxis)
plt.xlabel("iteration")
plt.ylabel("dy/dx")
yhat = savgol_filter(yaxis, 51, 2)
plt.plot(xaxis, yhat, color = 'red')
plt.savefig("SoC=Plot3-Tanay.jpg")
maxder = np.amax(yhat)
index = np.where(yhat == np.amax(yhat))
print("max derivative occurs at", index, " with value ", maxder)

xaxis = []
x_axis = [0]
yaxis = []
seed(time.time())
nones = [1]
array = np.zeros(10000)
array[4999] = 1
iters = 0

while(True):
  iters += 1
  set1 = np.random.randint(0, 9999, 5)
  set2 = np.random.randint(0, 9999, 5)
  for _ in range(5):
    temp = array[set1[_]]
    array[set1[_]] = array[set2[_]]
    array[set2[_]] = temp
  
  for _ in range(10000):
    if array[_] == 1:
      val1 = random.random()
      val2 = random.random()
      if val1<= 0.35:
        array[(_ + 9999)%10000] = 1
      if val2<= 0.35:
        array[(_ + 1)%10000] = 1
      
  count = 0
  for _ in range(10000):
    count += array[_]
  x_axis.append(iters)
  xaxis.append(iters)
  nones.append(count)
  yaxis.append(count - nones[iters-1])
  if count >= 10000: 
    break


plt.plot(xaxis, yaxis)
plt.xlabel("iteration")
plt.ylabel("#1's")
# yhat = savgol_filter(yaxis, 51, 2)
# plt.plot(xaxis, yhat, color = 'red')
plt.savefig("SoC=Plot1-Tanay.jpg")
print("Iterations required", iters)
# maxder = np.amax(yhat)
# index = np.where(yhat == np.amax(yhat))
# print("max derivative occurs at", index, " with value ", maxder)

