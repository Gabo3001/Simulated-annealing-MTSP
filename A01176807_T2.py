import numpy as np
from random import uniform
from random import choice
from math import e

ciudades = [[0,38.3,41.23,7.52,8.74,3.17,2.2,14.89,33.95,47.79,29.6,13.61,8.63,1.09,33.67],
[38.3,0,31.24,25.95,23.46,13.42,5.69,48.21,26.14,4.97,33.09,33.72,29.33,44.33,49.64],
[41.23,31.24,0,49.27,7.39,16.73,32.54,2.65,13.86,35.84,22.34,36.46,4.16,6.99,5.96],
[7.52,25.95,49.27,0,30.04,6.06,45.95,34.29,27.99,8.7,33.21,35.76,28.02,20.17,3.29],
[8.74,23.46,7.39,30.04,0,42.98,1.81,46.14,18.81,28.44,37.58,41.94,35.92,26.35,40.77],
[3.17,13.42,16.73,6.06,42.98,0,44.61,3.88,5.85,41.7,49.07,44.54,22.29,30.41,18.16],
[2.2,5.69,32.54,45.95,1.81,44.61,0,39.09,6.17,7.89,1.55,6.69,3.61,12.93,46.33],
[14.89,48.21,2.65,34.29,46.14,3.88,39.09,0,43.82,35.97,25.31,32.51,31.54,27.65,15.19],
[33.95,26.14,13.86,27.99,18.81,5.85,6.17,43.82,0,37.24,31.96,22.95,30.53,16.34,1.97],
[47.79,4.97,35.84,8.7,28.44,41.7,7.89,35.97,37.24,0,17.05,40.48,43.07,9.43,12.97],
[29.6,33.09,22.34,33.21,37.58,49.07,1.55,25.31,31.96,17.05,0,3.29,15.75,20.86,32.1],
[13.61,33.72,36.46,35.76,41.94,44.54,6.69,32.51,22.95,40.48,3.29,0,7.98,17.47,31.25],
[8.63,29.33,4.16,28.02,35.92,22.29,3.61,31.54,30.53,43.07,15.75,7.98,0,7.13,7.49],
[1.09,44.33,6.99,20.17,26.35,30.41,12.93,27.65,16.34,9.43,20.86,17.47,7.13,0,35.03],
[33.67,49.64,5.96,3.29,40.77,18.16,46.33,15.19,1.97,12.97,32.1,31.25,7.49,35.03,0]]


def generaCiudades():
  ciudades = np.zeros((15, 15))
  for i in range(15):
    for j in range(i, 15):
      if i != j:
        ciudades[i,j] = round(uniform(1, 50), 2)
        ciudades[j,i] = ciudades[i,j]
  return ciudades

def calculaDist(arr):
  dist = 0
  lst=[]
  for i in range(0,15,5):
    lst.append((arr[i:i+5]))
  fst = lst[0] + (lst[0][0],)
  scd = lst[1] + (lst[1][0],)
  trd = lst[2] + (lst[2][0],)
  for i in range(len(fst)-1):
    dist += ciudades[fst[i]-1][fst[i+1]-1]
  for i in range(len(scd)-1):
    dist += ciudades[scd[i]-1][scd[i+1]-1]
  for i in range(len(trd)-1):
    dist += ciudades[trd[i]-1][trd[i+1]-1]
  return round(dist,2)

def generaVecino(tup):
  i = 0
  j = 0
  while i == j :
    i = choice(list(tup))
    j = choice(list(tup))
  auxLst = list(tup)
  auxVal = auxLst[i-1]
  auxLst[i-1] = auxLst[j-1]
  auxLst[j-1] = auxVal
  return tuple(auxLst)

def markovTemp(u0, l, temp):
  u = u0
  cont = 0
  for i in range(l):
    v = generaVecino(u)
    if calculaDist(v) < calculaDist(u):
      u =  v
      cont += 1
    else:
      auxRand = uniform(0,1)
      auxProb = e**-((calculaDist(v) - calculaDist(u))/temp)
      if auxRand  < auxProb:
        u =  v
        cont += 1
  return cont/l


def initTEmp(l, u):
  temp = 0.1
  u0 = u
  rMin = 0.9
  rA = 0
  while rA < rMin:
    rA = markovTemp(u0, l, temp)
    temp *= 1.1
  return temp

u0 = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
l = 50
temp = initTEmp(l, u0)
k = 0
u =  u0
while k < 20:
  for i in range(l):
    v = generaVecino(u)
    if calculaDist(v) < calculaDist(u):
      u =  v
      best = v
    else:
      auxRand = uniform(0,1)
      auxProb = e**-((calculaDist(v) - calculaDist(u))/temp)
      if auxRand  < auxProb:
        u =  v
  k += 1
  temp *= 0.9
print(best)
print(calculaDist(best))
