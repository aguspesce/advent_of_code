import re


def read_file(fname):
    """Read the file as string"""
    with open(fname) as f:
        file = f.read()
    return file


def find_expression(file, pattern):
    """Find all occurrences of the pattern"""
    expressions = re.findall(pattern, file)
    return expressions


def mul(expression):
    """Make the multiplication"""
    expression = expression[4:-1]
    first, second = expression.split(",")
    if len(first) <= 3 and len(second) <= 3:
        return int(first) * int(second)


def first_part(file, pattern):
    # Find the matches
    expressions = find_expression(file, pattern)
    # Make multiplication and add in the value
    value = 0
    for expression in expressions:
        value += mul(expression)
    return value


def second_part(file, pattern):
    expressions = find_expression(file, pattern)
    value = 0
    # Flag to evaluate the multiplication
    add_value = True
    for expression in expressions:
        if expression == "do()":
            # Change flag to true to make multiplications
            add_value = True
        elif expression == "don't()":
            # Change flag to false to dont make the multiplication
            add_value = False
        elif add_value is True:
            # If flag is true, make the multiplication and add results
            value += mul(expression)
    return value


def test_first_part():
    file = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    pattern = r"mul\(\d+,\d+\)"
    assert first_part(file, pattern) == 161


def test_second_part():
    file = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    pattern = r"do\(\)|don\'t\(\)|mul\(\d+,\d+\)"
    assert second_part(file, pattern) == 48


if __name__ == "__main__":
    filename = "day03/input.txt"
    file = read_file(filename)

    pattern = r"mul\(\d+,\d+\)"
    value = first_part(file, pattern)
    print(f"Result of the multiplications: {value}")

    pattern = r"do\(\)|don\'t\(\)|mul\(\d+,\d+\)"
    value = second_part(file, pattern)
    print(f"Result of the multiplications: {value}")
