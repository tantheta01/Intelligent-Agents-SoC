# -*- coding: utf-8 -*-
"""SoC-Assn2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BBpJPZFLRjD_qhfPwgLMuevKATMKFgxw
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
import random
from random import randint
from random import seed
import time
from scipy.signal import savgol_filter
# %matplotlib inline

"""# **Calculating 1's per iteration**"""

seed(time.time())

Xaxis = [0]
Yaxis = [1]
numit = 0
array = np.zeros([120, 125], dtype = int)
array[60, 63] = 1
while(True):
  numit += 1
  l1 = np.random.randint(0, 119, 16)
  l2 = np.random.randint(0, 124, 16)
  for x in range(8):
    temp = array[l1[x], l2[x]]
    array[l1[x], l2[x]] = array[l1[x+8], l2[x+8]]
    array[l1[x+8], l2[x+8]] = temp
  
  inds = []
  for i in range(120):
    for j in range(125):
      if array[i, j] == 1:
        inds.append([i, j])
  
  for ind in inds:
    for i in range(3):
      for j in range(3):
        if(random.random() <= 0.25):
          array[(ind[0] + i + 119)%120, (ind[1] + j + 124)%125] = 1
        if(random.random() <= 0.08):
          array[(ind[0] + 2*i + 118)%120, (ind[1] + j + 123)%125] = 1


  nones = 0
  for x in np.nditer(array):
    nones += x
  Xaxis.append(numit)
  print(nones)
  Yaxis.append(nones)
  if(nones == 15000):
    break

print("Number of iterations required are", numit)
plt.plot(Xaxis, Yaxis)
plt.xlabel("#iterations")
plt.ylabel("#1's")
plt.savefig("SoC-Assn2-Plot1.jpg")

Xaxis = []
Yaxis = []
for _ in range(1000):
  print(_)
  array = np.zeros([120, 125], dtype = int)
  array[60, 63] = 1
  numit = 0
  while(True):
    numit += 1
    l1 = np.random.randint(0, 119, 16)
    l2 = np.random.randint(0, 124, 16)
    for x in range(8):
      temp = array[l1[x], l2[x]]
      array[l1[x], l2[x]] = array[l1[x+8], l2[x+8]]
      array[l1[x+8], l2[x+8]] = temp
    
    inds = []
    for i in range(120):
      for j in range(125):
        if array[i, j] == 1:
          inds.append([i, j])
    
    for ind in inds:
      for i in range(3):
        for j in range(3):
          if(random.random() <= 0.25):
            array[(ind[0] + i + 119)%120, (ind[1] + j + 124)%125] = 1
          if(random.random() <= 0.08):
            array[(ind[0] + 2*i + 118)%120, (ind[1] + j + 123)%125] = 1


    nones = 0
    for x in np.nditer(array):
      nones += x
    if(nones == 15000):
      break
  Xaxis.append(_ + 1)
  Yaxis.append(numit)

plt.plot(Xaxis, Yaxis)
print(np.mean(Yaxis))

plt.xlabel("#runs")
plt.ylabel("#iterations")
plt.savefig("Soc-Assn2-Plot2.jpg")

"""# **_Getting dy/dx_**"""

Xaxis = [0]
Yaxis = [1]
YY = []
XX = []
numit = 0
array = np.zeros([120, 125], dtype = int)
array[60, 63] = 1
while(True):
  numit += 1
  l1 = np.random.randint(0, 119, 16)
  l2 = np.random.randint(0, 124, 16)
  for x in range(8):
    temp = array[l1[x], l2[x]]
    array[l1[x], l2[x]] = array[l1[x+8], l2[x+8]]
    array[l1[x+8], l2[x+8]] = temp
  
  inds = []
  for i in range(120):
    for j in range(125):
      if array[i, j] == 1:
        inds.append([i, j])
  
  for ind in inds:
    for i in range(3):
      for j in range(3):
        if(random.random() <= 0.25):
          array[(ind[0] + i + 119)%120, (ind[1] + j + 124)%125] = 1
        if(random.random() <= 0.08):
          array[(ind[0] + 2*i + 118)%120, (ind[1] + j + 123)%125] = 1


  nones = 0
  for x in np.nditer(array):
    nones += x
  Xaxis.append(numit)
  XX.append(numit)
  YY.append(nones - Yaxis[numit-1])
  # print(nones)
  Yaxis.append(nones)
  if(nones == 15000):
    break

print(max(YY))
plt.plot(XX, YY)
Yhat = savgol_filter(YY, 5, 1)
plt.plot(XX, Yhat, color = 'red')
plt.xlabel("#iterations")
plt.ylabel("d#1's/diter")

plt.savefig("SoC-Assn2-Plot3.jpg")
