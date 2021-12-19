
def getrules(path):
  with open(path, "r") as f:
    raw = [l.rstrip() for l in f.readlines()]
    splitkey = " -> "
  return {
    k.split(splitkey)[0] : k.split(splitkey)[-1]
    for k in raw
  }

def getdata(path):
  with open(path, "r") as f:
    data = [l.rstrip() for l in f.readlines()]
  return "".join(data)

def build_polymer(step = 1):
  rules = getrules("data/day14_rules.txt")
  df = getdata("data/day14_data.txt")
  pairs = [i + j for i, j in zip(list(df), list(df)[1:])]
  pair_record = {pair : 0 for pair in rules.keys()}
  for p in pairs:
    pair_record[p] += 1

  while step > 0:
    tmp_pair_record = {pair : 0 for pair in rules.keys()}
    for p in pair_record:
      if pair_record[p] > 0:
        newpairs = [f"{p[0]}{rules[p]}", f"{rules[p]}{p[-1]}"]
        for np in newpairs:
          tmp_pair_record[np] += pair_record[p]

    pair_record = tmp_pair_record.copy()
    elements = {el : 0 for el in set(rules.values())}
    elements[df[-1]] += 1
    for p in pair_record:
      elements[p[0]] += pair_record[p]
    step -= 1

  return elements

def main():
  record =  build_polymer(40)
  # get most and least common element
  print(record)
  maxval = 0
  minval = 9.9e100
  for key in record:
    if record[key] > maxval:
      maxval = record[key]
    if record[key] < minval:
      minval = record[key]

  print(sum(record.values()), maxval, minval, maxval - minval)


if __name__ == "__main__":
  main()
