def read_program(fname):
    """
    Return a list with the program lines as list
    """
    with open(fname, "r") as f:
        program = f.read().splitlines()
    program = [line.split(" ") for line in program]
    return program


def test_read_instructions():
    """
    Check _read_instructions function
    """
    lines_list = read_program("test_input")
    assert lines_list == [["noop"], ["addx", "3"], ["addx", "-5"]]


def check_cycle(cycle, x, x_values):
    """
    Return a list called x_values with the x values if the cycle is in cycles_to_check
    """
    cycles_to_check = [20, 60, 100, 140, 180, 220]
    if cycle in cycles_to_check:
        x_values.append(x)
    return x_values


def test_check_cycle():
    """
    Check check_cycle function
    """
    cycles = [20, 60, 50]
    xs = [3, 10, 20]
    x_values = []
    expected = [3, 10]
    for cycle, x in zip(cycles, xs):
        x_values = check_cycle(cycle, x, x_values)
    assert x_values == expected


def calculate_signal(x_values):
    cycles_to_check = [20, 60, 100, 140, 180, 220]
    signal = [x * cycle for x, cycle in zip(x_values, cycles_to_check)]
    return sum(signal)


def test_calculate_signal():
    expected = 13140
    x_values = [21, 19, 18, 21, 16, 18]
    assert calculate_signal(x_values) == expected


# Read the program lines
program_lines = read_program("input")

# Initialize cycle counter and x_register
cycle, x_register = 1, 1
# Initialize a list to save the x values
x_values = []

# Run the program lines and save the value of x for given cycles
for line in program_lines:
    # If line is noop, doesn't do anything and increase cycle
    if line[0] == "noop":
        cycle += 1
        # Check if cycle is in cycles_to_check and add x_register in x_values list
        x_values = check_cycle(cycle, x_register, x_values)
    # If line is addx, add this value to x_register and increase cycle
    if line[0] == "addx":
        cycle += 1
        # Check if cycle is in cycles_to_check and add x_register in x_values list
        x_values = check_cycle(cycle, x_register, x_values)
        cycle += 1
        # Increase x_register
        x_register += int(line[1])
        # Check if cycle is in cycles_to_check and add x_register in x_values list
        x_values = check_cycle(cycle, x_register, x_values)

print(x_values)

signal = calculate_signal(x_values)

print(f"Solution first part: {signal}")
