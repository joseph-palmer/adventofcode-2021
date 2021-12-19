import numpy as np

def check_larger(x1, x2):
    # return 1 if preceding value (x1) is less than current value (x2)
    # return 0 if not
    if x2 > x1:
        return 1
    else:
        return 0

def get_total_larger(x):
    # run check_larger on entire data frame to get a 1 or 0 score for each pair
    # sum the pairs to get the total number of measurments larger than the previous
    larger = [
        check_larger(x[i-1], x[i])
        for i in range(1, len(x))
    ]
    return sum(larger)

def compare_windows(x1, x2, x3, x4):
    if sum([x1, x2, x3]) < sum([x2, x3, x4]):
        return 1
    else:
        return 0

def sliding_3_window(x):
    larger = [
        compare_windows(x[i-3], x[i-2], x[i-1], x[i])
        for i in range(3, len(x))
    ]
    return sum(larger)

# run check of part 1 to ensure it works
testdata = np.array([199, 200, 208, 210, 200, 207, 240, 269, 260, 263])
test_p1_correct_answer = 7
assert(get_total_larger(testdata) == test_p1_correct_answer)

# calculate part 1 on actual data
data = np.genfromtxt("data/day1_data.txt")
print(get_total_larger(data))

# test part 2
test_p2_correct_answer = 5
assert(test_p2_correct_answer == sliding_3_window(testdata))

# calculate part 2
print(sliding_3_window(data))
