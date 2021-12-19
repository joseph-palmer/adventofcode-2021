import pandas as pd

def load_data(fpath):
  """
  load the position data from file

  Args:
      string: The path to the file to load
  Returns:
      pd.dataframe: A two column list of the data (direction and extent)
  """
  data = pd.read_csv(fpath, header = None, delimiter = " ")
  return data

def sum_rows_for_direction(data, direction, multiplier = 1):
  """Sum rows in column 1 based on column 1 matching the direction argument
  multiplier allows the sum to work on subraction

  Args:
      pd.dataframe: A two column list of the data (direction and extent)
      direction (string): the direction to calculate for
      multiplier (int, optional): to multiply the data for, set to -1 for
      subtracting. Defaults to 1.

  Returns:
      pd.dataframe: A two column list of the data (direction and extent)
  """
  only_direction_data = data[data.iloc[:, 0] ==  direction]
  return sum(only_direction_data.iloc[:, 1] * multiplier)

def calc_horizontal_and_depth(data):
  """calculate the horizontal movement, depth and their multiple

  Args:
      pd.dataframe: A two column list of the data (direction and extent)

  Returns:
      pd.dataframe: A two column list of the data (direction and extent)
  """
  horizontal, up, down = [
    sum_rows_for_direction(data, i[0], i[1])
    for i in [("forward", 1), ("up", -1), ("down", 1)]
  ]
  return (horizontal, up + down, horizontal*(up + down))

def cal_horizontal_and_depth_correct_for_aim(data):
  """Calculate the horizontal movement and depth, corrected for aim

  Args:
      pd.dataframe: A two column list of the data (direction and extent)

  Returns:
      pd.dataframe: A two column list of the data (direction and extent)
  """
  horizontal = sum_rows_for_direction(data, "forward")
  data["aim"] = 0

  # for each row, if a direction is down then increase the aim by the movement
  # if the direction is up then decrease the aim by the movement
  # change the index for all rows following the one in operation
  updown_index = data.index[data[0] != "forward"].tolist()
  for i in updown_index:
    df = data.iloc[i].values
    if df[0] == "down":
      data.loc[i:, "aim"] = data.loc[i:, "aim"] + df[1]
    elif df[0] == "up":
      data.loc[i:, "aim"] = data.loc[i:, "aim"] - df[1]

  # multiply the aim by the movement for forward rows and sum the resulting
  # columns
  data["d"] = data.iloc[:, 1].values * data["aim"].values
  depth = data[data.iloc[:, 0] == "forward"]["d"].sum()
  return (horizontal, depth, horizontal*depth)

def test_calculations():
  """Test the functions work as desired
  """
  data = load_data("data/day2_test_data.txt")
  actual_horizontal = 15
  actual_depth = 10
  horizontal, depth, hdprod = calc_horizontal_and_depth(data)
  assert(actual_horizontal == horizontal)
  assert(actual_depth == depth)
  assert(actual_horizontal*actual_depth == hdprod)

  actual_horizontal = 15
  actual_depth = 60
  horizontal, depth, hdprod = cal_horizontal_and_depth_correct_for_aim(data)
  assert(actual_horizontal == horizontal)
  assert(actual_depth == depth)
  assert(actual_horizontal*actual_depth == hdprod)


def main():
  """Advent of code day two task solution

  Returns:
      int: exit code
  """
  # run test to ensure code works as expected
  test_calculations()

  # run analysis on full data
  data = load_data("data/day2_data.txt")
  horizontal, depth, hdprod = calc_horizontal_and_depth(data)
  print(f"Horizontal = {horizontal}\nDepth = {depth}\nProduct: {hdprod}")

  # run corrected analyses
  horizontal, depth, hdprod = cal_horizontal_and_depth_correct_for_aim(data)
  print("After correction:")
  print(f"Horizontal = {horizontal}\nDepth = {depth}\nProduct: {hdprod}")

  return 0

if __name__ == "__main__":
  main()