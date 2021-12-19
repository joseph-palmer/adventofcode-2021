import numpy as np

# Doesn't work. Needs something more complex. Implement an A* algorithm or graph
# search
def getminpath(data):
  cost = np.full(data.shape, np.nan)
  first_row = data[0,:]
  first_col = data[:,0]

  for i in range(len(first_row)):
    cost[0, i] = sum(first_row[:i+1])
  for j in range(len(first_col)):
    cost[j, 0] = sum(first_col[:j+1])

  for i in range(1, cost.shape[0]):
    for j in range(1, cost.shape[-1]):
      cost[i, j] = data[i, j] + min(cost[i-1, j], cost[i, j-1])

  answer = cost[data.shape[0]-1, data.shape[-1]-1] #- data[0, 0]
  return answer

path = "data/day15_data.txt"
data = np.genfromtxt(path, delimiter = 1)

minpath = getminpath(data)
print(minpath)