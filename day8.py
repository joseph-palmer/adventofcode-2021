from typing import Sequence
import numpy as np

seg1 = ""
seg4 = ""

def str2num(seg):
  global seg1, seg4
  if len(seg) == 2:
    seg1 = seg
    return 1
  elif len(seg) == 4:
    seg4 = seg
    return 4
  elif len(seg) == 3:
    return 7
  elif len(seg) == 7:
    return 8
  elif len(seg) == 6:
    if seg1[0] in seg and seg1[-1] in seg:
      if len(set(seg).intersection(set(seg4))) == 3:
        return 0
      else:
        return 9
    else:
      return 6
  elif len(seg) == 5:
    if seg1[0] in seg and seg1[-1] in seg:
      return 3
    elif len(set(seg).intersection(set(seg4))) == 3:
        return 5
    else:
      return 2

conversion_dict = {
  2 : 1,
  4 : 4,
  3 : 7,
  7 : 8
}

datapath = "data/day8_test_data.txt"
datapath = "data/day8_data.txt"

total = 0
total_sum = 0
for line in open(datapath):
  output = line.rstrip().split(" | ")[-1]
  input = line.rstrip().split(" | ")[0]
  seglen = [len(seg) for seg in output.split(" ")]
  total += len([i for i in seglen if i in list(conversion_dict.keys())])
  segvals = [
    conversion_dict[i]
    if i in list(conversion_dict.keys()) else 0
    for i in seglen
  ]
  inputlist = input.split(" ")
  inputlist.sort(key = len)
  resdict = {
    "".join(sorted(v)) : str2num(v) for v in inputlist
  }
  result = [resdict["".join(sorted(k))] for k in output.split(" ")]
  res = "".join([str(i) for i in result])
  total_sum += int(res)

print(total, total_sum)