import numpy as np

def tryget(data, i, j):
  if i < 0 or j < 0:
    return ([np.nan, np.nan], np.nan)
  try:
    result = ([i, j], data[i, j])
  except IndexError:
    result = ([np.nan, np.nan], np.nan)
  return result

def get_cross(data, i, j):
  x = data[i, j]
  bellow = tryget(data, i+1, j)
  above = tryget(data, i-1, j)
  left = tryget(data, i, j-1)
  right = tryget(data, i, j+1)
  cross = np.array([bellow[-1], above[-1], left[-1], right[-1]])
  cross_index =  np.array([bellow[0], above[0], left[0], right[0]])
  cross_index = cross_index[~(np.isnan(cross_index).any(axis=1))]
  cross = cross[~np.isnan(cross)]
  cross_index = np.column_stack((cross_index, cross))
  if x < min(cross):
    return (x, cross_index, cross)
  return (-1, cross_index, cross)

def depth_first_search(data, start, visited = None):
  if visited is None:
    visited = set()
  visited.add("_".join([str(i) for i in start]))
  check = get_cross(data, start[0], start[-1])[1]
  check = check[np.where(check[:, -1] != 9)].astype(int)
  for next in check:
    checkcode = "_".join([str(i) for i in list(next[:2])])
    if checkcode not in visited:
      depth_first_search(data, list(next[:2]), visited)
  return visited

data = np.genfromtxt("data/day9_test_data.txt", delimiter = 1).astype(int)
data = np.genfromtxt("data/day9_data.txt", delimiter = 1).astype(int)


print(data)

lowpoint_sum = 0
basin_sizes = []
for i in range(data.shape[0]):
  for j in range(data.shape[-1]):
    result = get_cross(data, i, j)
    lowpoint_sum += result[0] + 1
    if result[0] + 1 > 0:
      basin_size = depth_first_search(data, [i, j])
      basin_sizes.append(len(basin_size))

print(lowpoint_sum)
largest_3 = sorted(basin_sizes)[-3:]
product_basins = 1
for i in largest_3:
  product_basins *= i

print(product_basins)