# https://adventofcode.com/2024/day/1

with open('input.txt', 'r') as file:
    raw_input = file.read()
    lines = raw_input.splitlines()

# --- Part 1 --- #

string_pairs = [line.split() for line in lines]

pairs = [[int(string_pair[0]), int(string_pair[1])] for string_pair in string_pairs]

row1 = [pair[0] for pair in pairs]
row2 = [pair[1] for pair in pairs]

sorted_row1 = sorted(row1)
sorted_row2 = sorted(row2)

diff_row = [abs(sorted_row1[i] - sorted_row2[i]) for i in range(len(row1))]
diff_sum = sum(diff_row)

print(diff_sum)

# ---------

similarity = 0
for num1 in row1:
    similarity += num1 * row2.count(num1)

print(similarity)
