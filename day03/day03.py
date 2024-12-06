# https://adventofcode.com/2024/day/3
import re

with open('input.txt', 'r') as file:
    raw_input = file.read()

# --- Part 1 --- #

multiply_regex = r"mul\((\d+),(\d+)\)"
matches = re.findall(multiply_regex, raw_input)

total = 0
for match in matches:
    total += int(match[0]) * int(match[1])
print(total)

# --- Part 2 --- #

only_normal = re.sub('[^A-Za-z0-9(),]+', '', raw_input)
matches = re.findall(multiply_regex, only_normal)

new_total = 0

do_parts = only_normal.split("do()")
for do_part in do_parts:
    only_do_part = do_part.split("dont()")[0]
    matches = re.findall(multiply_regex, only_do_part)
    for match in matches:
        new_total += int(match[0]) * int(match[1])

print(new_total)
