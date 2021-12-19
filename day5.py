from typing import Sequence
import numpy as np
import matplotlib.pyplot as plt

testdatapath = "data/day5_data.txt"

with open(testdatapath, "r") as f:
  data = f.readlines()

data = [i.strip().split(" -> ") for i in data]

raw_coords = np.array(data)

tmp = np.column_stack(
  (np.array([i.split(",") for i in raw_coords[:,0]]).astype(int),
  np.array([i.split(",") for i in raw_coords[:,1]]).astype(int))
)

shape = (max(tmp[:,-1]+1), max(tmp[:,0]+1))

coord_system = np.zeros(shape)

# create coord system
for row in tmp:
  if row[1] == row[3] or row[0] == row[2]:
    start = row[:2]
    stop = row[2:]
    idx = np.where(start == stop)[0][0]
    constant = start[idx]
    variables = set(start).symmetric_difference(stop)
    if len(variables) < 2:
      variables = [stop[0], list(variables)[0]]
    if idx == 0:
      res = [
        np.array([constant, i]) for i in range(min(variables)+1, max(variables))
      ]
    else:
      res = [
        np.array([i, constant]) for i in range(min(variables)+1, max(variables))
      ]
    change = [np.flip(i) for i in [start] + res + [stop]]
    for c in change:
      coord_system[c[0], c[1]] = coord_system[c[0], c[1]] + 1
  else:
    # y = mx+b
    m = (row[1]-row[3])/(row[0]-row[2])
    b = (row[0]*row[3] - row[1]*row[2])/(row[0]-row[2])
    xs = [row[0], row[2]]
    xvals = list(range(min(xs), max(xs)+1))
    yvals = [int(m*x_+b) for x_ in xvals]
    coords = [[j, i] for i, j in zip(xvals, yvals)]
    for c in coords:
      coord_system[c[0], c[1]] = coord_system[c[0], c[1]] + 1



overlaps = np.where(coord_system > 1)
print(len(overlaps[0]))
print(len(overlaps[-1]))

# print(coord_system)

# plt.matshow(coord_system)
# plt.show()