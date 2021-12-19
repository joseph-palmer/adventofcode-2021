import numpy as np
from numpy.core.numeric import full

def get_adj(data, i, j):
  return data[
    max(0, i-1):min(data.shape[0], i+2), max(0, j-1):min(data.shape[-1], j+2)
  ]

dpath = "data/day11_test_data.txt"
data = np.genfromtxt(dpath, delimiter=1).astype(int)
print(data)

nflashes = 0

iter = 0
notsinc = True
while notsinc:
  iter += 1
# for iter in range(100):
  data[::] = data + 1
  used = []
  fullpowered = np.where(data > 9)
  while len(fullpowered[0]) > len(used):
    for i, j in zip(fullpowered[0], fullpowered[1]):
      marker = "_".join([str(i), str(j)])
      if marker not in used:
        used.append(marker)
        subdat = get_adj(data, i, j)
        subdat += 1
    fullpowered = np.where(data > 9)
  flashed = np.where(data > 9)
  data[flashed] = 0
  nflashes += len(flashed[0])
  if len(np.unique(data)) < 2:
    notsinc = False

print(nflashes, iter)
print(data)