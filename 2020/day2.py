

valid_passwords = []
valid_passwords_p2 = []
for line in open("day2_data.txt"):
  l = line.rstrip()
  pw = l.split(": ")[-1]
  target = l.split(":")[0][-1]
  occurance_range = l.split(" ")[0]
  ocuurance_min = int(occurance_range.split("-")[0])
  occurance_max = int(occurance_range.split("-")[-1])
  target_occurance = sum(
    [1 if char == target else 0 for char in pw]
  )
  if target_occurance >= ocuurance_min \
    and target_occurance <= occurance_max:
    valid_passwords.append(pw)
  if pw[ocuurance_min-1] == target:
    if pw[occurance_max-1] != target:
      valid_passwords_p2.append(pw)
  elif pw[occurance_max-1] == target:
    valid_passwords_p2.append(pw)

print(len(valid_passwords))
print(len(valid_passwords_p2))