


from types import coroutine
from typing import Counter


dpath = "data/day10_data.txt"

with open(dpath, "r") as f:
  data = [i.rstrip() for i in f.readlines()]

openers = ["(", "[", "{", "<"]
closers = [")", "]", "}", ">"]
scores = [3, 57, 1197, 25137]
match = {closers[i] : openers[i] for i in range(len(openers))}
illegal_score = {closers[i] : [0, scores[i]] for i in range(len(openers))}

p2list = []
for line in data:
  corrupt = False
  stack = []
  for char in line:
    if char in openers:
      stack.insert(0, char)
    else:
      if match[char] == stack[0]:
        stack.pop(0)
      else:
        illegal_score[char][0] += 1
        corrupt = True
        break
  if not corrupt:
    res = 0
    for s in stack:
      res = res * 5
      res += [i[0] for i in enumerate([""]+openers) if s == i[-1]][0]
    p2list.append(res)


mididx = int((len(p2list)-1)/2)
print(sorted(p2list)[mididx])


for k in illegal_score:
  print(k, illegal_score[k])

print(
  sum([illegal_score[k][0]*illegal_score[k][-1]
  for k in list(illegal_score.keys())])
)

