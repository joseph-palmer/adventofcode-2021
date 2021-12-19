import numpy as np

def load_bingo_sheets(path):
  with open(path, "r") as f:
    data = f.readlines()
  bingosheets = {}
  dict_index = 0
  c = 0
  for row in data:
    key = f"sheet_{dict_index}"
    if c == 5:
      dict_index = dict_index+1
      c = 0
      continue
    c+=1
    introw = list(map(int, row.split()))
    if key not in list(bingosheets.keys()):
      bingosheets[key] = [introw]
    else:
      bingosheets[key].append(introw)
  return bingosheets

def check_sheet(sheet, check_numbers):
  index = np.where(np.isin(sheet, check_numbers))
  sheet[index] = 0
  colsum = np.sum(sheet, axis = 1)
  rowsum = np.sum(sheet, axis = 0)
  sheet_sum = np.concatenate((rowsum, colsum))
  check = sheet_sum[sheet_sum < 1]
  if len(check):
    return (1, sheet)
  else:
    return (0, 0)

datapath = "data/day4_bingo_card_data.txt"

bingosheets = load_bingo_sheets(datapath)
bingonumbers = np.genfromtxt(
  "data/day4_bingo_numbers.txt", delimiter = ","
).astype(int)

final_scores = []
check_numbers = bingonumbers[:4]
for number in bingonumbers[4:]:
  check_numbers = np.append(check_numbers, number)
  for sheet in list(bingosheets):
    new_sheet = check_sheet(
      np.array(bingosheets[sheet]), check_numbers
    )
    if new_sheet[0]:
      final_scores.append((sheet, new_sheet[-1].sum() * number))
      del bingosheets[sheet]

print(final_scores)
