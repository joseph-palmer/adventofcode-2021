import numpy as np

def foldup(data, y):
  up = data[:y, :]
  down = data[y+1:, :]
  down = np.flip(down, axis=0)
  return up + down

def foldleft(data, x):
  left = data[:, :x]
  right = data[:, x+1:]
  right = np.flip(right, axis = -1)

  return left + right

# load data
data = np.genfromtxt("data/day13_data.txt", delimiter = ",").astype(int)

# set up matrix
jmax = data[:, 0].max() + 1
imax = data[:, -1].max() + 1
df = np.zeros((imax, jmax))
df[(data[:, -1], data[:, 0])] = 1

# folding instructions
foldinstructions = """fold along x=655
fold along y=447
fold along x=327
fold along y=223
fold along x=163
fold along y=111
fold along x=81
fold along y=55
fold along x=40
fold along y=27
fold along y=13
fold along y=6"""

# start folding p1
folded_data = df
for line in foldinstructions.split("\n"):
  if "y=" in line:
    folded_data = foldup(folded_data, int(line.split("y=")[-1].rstrip()))
  elif "x=" in line:
    folded_data = foldleft(folded_data, int(line.split("x=")[-1].rstrip()))

# covert to string to see it
res = ""
for row in range(folded_data.shape[0]):
  rowstring = "".join(["#" if i > 0 else "." for i in folded_data[row,:]])
  res += rowstring + "\n"

print(res)
visibledots = len(np.where(folded_data > 0)[0])
print(visibledots)