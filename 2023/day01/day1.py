from os import replace
import re

NUM_MAP = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def find_digit(line):
    """Find digit in the string"""
    num_line = re.findall("[0-9]", line)
    if len(num_line) >= 2:
        digit = int(num_line[0] + num_line[-1])
    else:
        digit = int(num_line[0] + num_line[0])
    return digit


def replace_numbers(line):
    """Map the line and replace coincidence"""
    for key in NUM_MAP:
        line = line.replace(key, key + NUM_MAP[key] + key)
    return line


def part_one(fname):
    """Solve first part"""
    suma = 0
    with open("input.txt") as data:
        for line in data:
            digit = find_digit(line)
            suma += digit
    return suma


def part_two(fname):
    """Solve second part"""
    suma = 0
    with open("input.txt") as data:
        for line in data:
            line = replace_numbers(line)
            digit = find_digit(line)
            suma += digit
    return suma


if __name__ == "__main__":
    # Read input file
    fname = "input.txt"
    solution = part_one(fname)
    print("The sum of all calibration values is:", solution)
    solution2 = part_two(fname)
    print("The sum of all calibration values for second part is:", solution2)
