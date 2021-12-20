
data = []
for line in open("day1_data.txt"):
  data.append(int(line.rstrip()))

idat, jdat, kdat = [[]]*3
for i in data:
  for j in data:
    for k in data:
      if i+j+k == 2020:
        idat.append(i)
        jdat.append(j)
        kdat.append(k)

targets = set(idat+jdat+kdat)

res = 1
for val in targets:
  res *= val

print(targets, res)