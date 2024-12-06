# https://adventofcode.com/2024/day/2

with open('input.txt', 'r') as file:
    raw_input = file.read()
    lines = raw_input.splitlines()

# --- Part 1 --- #

reports = [[int(level) for level in line.split()] for line in lines]


def all_positive(xs):
    return all(x > 0 for x in xs) or all(x > 0 for x in xs)


def all_negative(xs):
    return all(x < 0 for x in xs) or all(x > 0 for x in xs)


def all_same_sign(xs):
    return all_positive(xs) or all_negative(xs)


def get_diffs(xs):
    return [xs[i + 1] - xs[i] for i in range(len(xs) - 1)]


def is_safe_part_1(report):
    diffs = get_diffs(report)
    return all(0 < abs(diff) <= 3 for diff in diffs) and all_same_sign(diffs)


number_of_safe_reports = len([report for report in reports if is_safe_part_1(report)])
print(number_of_safe_reports)


# --- Part 2 --- #


def is_safe_part_2(report):
    if is_safe_part_1(report):
        return True

    for i in range(len(report)):
        new_report = report.copy()
        new_report.pop(i)
        if is_safe_part_1(new_report):
            return True
    return False


number_of_safe_reports = len([report for report in reports if is_safe_part_2(report)])
print(number_of_safe_reports)
