from os import path
import numpy as np

def findpaths(graph, node, record, paths):
  if node == "end":
    record.append(node)
    paths.append(record)
  elif node.islower() and node in record:
    record.append(node)
    paths.append(record)
  else:
    record.append(node)
    children = graph[node]
    for child in children:
      findpaths(graph, child, record[:], paths)
  return paths

def findpaths_p2(graph, node, record, paths, special):
  if node == "end":
    record.append(node)
    paths.append(record)
    return paths
  if node.islower() and node in record:
    if node == special and sum([1 if i == node else 0 for i in record]) < 2:
      carryonoldsport = True
    else:
      record.append(node)
      paths.append(record)
      return paths
  record.append(node)
  children = graph[node]
  for child in children:
    findpaths_p2(graph, child, record[:], paths, special)
  return paths

connections = {}
with open("data/day12_data.txt", "r") as f:
  for line in f.readlines():
    line = line.strip()
    key = line.split("-")[0]
    val = line.split("-")[-1]
    if key not in list(connections.keys()):
      connections[key] = [val]
    else:
      connections[key].append(val)
    if val not in list(connections.keys()):
      connections[val] = [key]
    else:
      connections[val].append(key)

# remove starts from dict keys
for key in connections:
  if "start" in connections[key]:
    connections[key].remove("start")


print(connections)

paths = findpaths(connections, "start", [], [])

score = 0
for p in paths:
  if p[-1] == "end":
    score += 1

print(score)

p2list = []
for cave in list(connections.keys()):
  if cave.islower() and cave not in ["start", "end"]:
    paths_p2 = findpaths_p2(connections, "start", [], [], cave)
    for p in paths_p2:
      if p[-1] == "end":
        p2list.append(",".join(p))

print(len(set(p2list)))