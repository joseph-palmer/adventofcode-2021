import numpy as np


def calc_fuel(x):
  limits = np.array(
    [[i for i in range(min(x), max(x)+1)]] * len(x)
  ).T
  diff = abs(x - limits)
  cost = diff.sum(axis=1)
  return (cost.min(), x[cost.argmin()])

# test code
tst = np.array([16,1,2,0,4,2,7,1,2,14])
assert(calc_fuel(tst)[0] == 37)

def calc_fuel_p2(x):
  limits = np.array(
    [[i for i in range(min(x), max(x)+1)]] * len(x)
  ).T
  diff = abs(x - limits)
  diff = 1/2*(diff+1)*(diff)
  cost = diff.sum(axis=1)
  return (cost.min(), x[cost.argmin()])

# test code
tst = np.array([16,1,2,0,4,2,7,1,2,14])
assert(calc_fuel(tst)[0] == 37)
assert(calc_fuel_p2(tst)[0] == 168)


data = np.genfromtxt("data/day7_data.txt", delimiter = ",").astype(int)

print(
  calc_fuel(data),
  calc_fuel_p2(data)
)