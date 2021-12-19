import numpy as np


def calc_age_faster(y, days):
  # record how many are at each number of days old - index indicates days old
  # the value is how many at that day old
  ages = [0]*9
  for i in y:
    ages[i] += 1
  # loop through the days
  for i in range(days):
    # record how many are about to split
    x = ages[0]
    # move individuals at each day to day-1 (index-1) and add the number of
    # splitting lanternfish (those at day 0) to the last position in the ages
    ages = ages[1:] + [x]
    # add the number of lantern fish that split to day 6 as they continue living
    ages[6] += x
  # the number in each age thus are now the total number of lantern fish
  return sum(ages)

def calc_age(y, days):
  for i in range(days):
    zeros = np.where(y==0)
    idx = np.where(y>0)
    y[idx] = y[idx] - 1
    if len(zeros[0]) > 0:
      y[zeros] = 6
      y = np.append(y, np.array([8]*len(zeros[0])))
  return y

def test_code():
  testinput = np.array([3, 4, 3, 1, 2])
  res1 = len(calc_age(np.copy(testinput), 18))
  res1_p2 = calc_age_faster(testinput, 18)
  res2 = len(calc_age(np.copy(testinput), 80))
  res3 = calc_age_faster(testinput, 256)
  assert(res1 == 26)
  assert(res2 == 5934)
  assert(res1_p2 == 26)
  assert(res3 == 26984457539)


# test code part 1
test_code()

# part 1 result
x = np.genfromtxt("data/day6_data.txt", delimiter = ",")
p1 = len(calc_age(np.copy(x), 80))
print(p1)

# part 2 result
p2 = calc_age_faster(x.astype(int), 256)
print(p2)

# my part 2 stuff

