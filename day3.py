import pandas as pd
import numpy as np

def calc_energy_usage(x):
  gamma_bits, epsilon_bits = [
    np.array(calc_gamma_epsilon(x, b))
    for b in [True, False]
  ]
  gamma_dec, epsilon_dec = [
    bit2decimal(i)
    for i in [gamma_bits, epsilon_bits]
  ]
  return (gamma_dec*epsilon_dec, gamma_bits, epsilon_bits)

def bit2decimal(bitsequence):
  return bitsequence.dot(2**np.arange(bitsequence.size)[::-1])

def get_bit(x, most_common = True):
  counts = np.bincount(x)
  if len(counts) == 1:
    counts = np.array([counts[0], 0])
  if most_common:
    if counts[0] == counts[1]:
      return 1
    return np.argmax(counts)
  else:
    return np.argmin(counts)

def calc_gamma_epsilon(x, most_common):
  return [
    get_bit(x[:, i].astype(int), most_common = most_common)
    for i in range(np.shape(x)[1])
  ]

def test_p1(x):
  assert(calc_energy_usage(x)[0] == 198)

def calc_gen_rating(x, checktype = True):
  data2check = x
  for i in range(x.shape[1]):
    bit = calc_gamma_epsilon(data2check, checktype)[i]
    check_next = []
    for row in data2check:
      if row[i] == bit:
        check_next.append(row)
    data2check = np.array(check_next)
    if data2check.shape[0] < 2:
      data2check = data2check[0, :]
      break

  return bit2decimal(data2check)

def test_p2(x):
  res = np.prod(
    [
      calc_gen_rating(x, i)
      for i in [True, False]
    ]
  )
  assert(res == 230)

def test_workflow():
  testdata = np.genfromtxt("data/day3_test_data.txt", delimiter=1)
  test_p1(testdata)
  test_p2(testdata)

test_workflow()

data = np.genfromtxt("data/day3_data.txt", delimiter=1)
print(calc_energy_usage(data)[0])

print(
  np.prod(
    [
      calc_gen_rating(data, i)
      for i in [True, False]
    ]
  )
)