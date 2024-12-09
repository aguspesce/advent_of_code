def read_file(fname):
    """
    Reads a file and returns a dictionary with the calibration equations    .
    """
    equations = {}
    with open(fname) as file:
        for line in file:
            key, values = line.strip().split(":")
            equations[int(key)] = [int(val) for val in values.strip().split()]
    return equations


def first_part(equations):
    result = []

    for key, numbers in equations.items():
        # Initialize possibles list with the first number (popped from the list)
        possibles = [numbers.pop(0)]
        # Iterate through the remaining numbers
        while numbers:
            curr = numbers.pop(0)
            # Temporary list to hold new possible results from adding and multiplying
            temp = []
            for p in possibles:
                # Add the current value to each possibility
                temp.append(p + curr)
                # Multiply the current value with each possibility
                temp.append(p * curr)
            possibles = temp

        if key in possibles:
            result.append(key)
    return sum(result)


def second_part(equations):
    result = []

    for key, numbers in equations.items():
        # Initialize possibles list with the first number (popped from the list)
        possibles = [numbers.pop(0)]
        # Iterate through the remaining numbers
        while numbers:
            curr = numbers.pop(0)
            # Temporary list to hold new possible results from adding and multiplying
            temp = []
            for p in possibles:
                # Add the current value to each possibility
                temp.append(p + curr)
                # Multiply the current value with each possibility
                temp.append(p * curr)
                temp.append(int(str(p) + str(curr)))
            possibles = temp

        if key in possibles:
            result.append(key)
    return sum(result)


def test_first_part():
    equations = read_file("day07/test")
    value = first_part(equations)
    assert value == 3749


def test_second_part():
    equations = read_file("day07/test")
    value = second_part(equations)
    assert value == 11387


if __name__ == "__main__":
    fname = "day07/input"
    equations = read_file(fname)
    value = first_part(equations)
    print(f"Total calibration results: {value}")
    import time

    equations = read_file(fname)
    start = time.time()
    value = second_part(equations)
    end = time.time()
    print(f"Total calibration results: {value}, {end -start}")
