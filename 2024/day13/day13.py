import re


def get_data(fname):
    """
    Process the input file, return in a suitable format as:
    {Price tuple: (Button A tuple, Button b tuple)}
    """
    REGEX = (
        r"Button A: X\+(\d+), Y\+(\d+)\s*"
        r"Button B: X\+(\d+), Y\+(\d+)\s*"
        r"Prize: X=(\d+), Y=(\d+)"
    )
    # Open and read the input file
    with open(fname) as file:
        data = file.read()

    # Find all matches in the data
    matches = re.findall(REGEX, data)

    # Return a dictionary
    return {
        (int(match[4]), int(match[5])): (
            (int(match[0]), int(match[1])),
            (int(match[2]), int(match[3])),
        )
        for match in matches
    }


def find_movements(key, machines):
    """
    Solve the system of equations to determine the number of times button A and button
    B need to be pressed in order to win the prize at the given key (prize location).
    """
    prize = key
    # Button A configuration (X, Y)
    buttom_a = machines[key][0]
    # Button B configuration (X, Y)
    buttom_b = machines[key][1]

    # Solve the system of equations using linear algebra
    times_b = (buttom_a[0] * prize[1] - buttom_a[1] * prize[0]) / (
        buttom_a[0] * buttom_b[1] - buttom_a[1] * buttom_b[0]
    )
    times_a = (prize[0] - buttom_b[0] * times_b) / buttom_a[0]

    return times_a, times_b


def first_part(machines):
    """
    Calculate the total number of tokens required to win the prize.

    The number of tokens is calculated based on how many times button A and button B
    need to be pressed to win the prize
    """
    tokens = 0
    for key in machines:
        times_a, times_b = find_movements(key, machines)
        # Check if both times_a and times_b are valid non-negative integers within
        # the range [0, 100]
        if (
            100 >= times_a >= 0
            and 100 >= times_b >= 0
            and times_a.is_integer()
            and times_b.is_integer()
        ):
            # Add the number of tokens required for this machine's configuration
            tokens += times_a * 3 + times_b
    return tokens


def second_part(machines):
    """
    Calculate the total number of tokens required to win the prize, with a modification
    to the prize locations.
    """
    # Change the keys of the dictionary
    new_machines = {}
    for key in machines:
        # Shift prize locations by a large constant
        new_key = (key[0] + 10000000000000, key[1] + 10000000000000)
        new_machines[new_key] = machines[key]

    tokens = 0
    for key in new_machines:
        times_a, times_b = find_movements(key, new_machines)
        # Only add tokens if the solution is valid
        if times_a.is_integer() and times_b.is_integer():
            tokens += times_a * 3 + times_b
    return tokens


def test_first_part():
    machines = {
        (8400, 5400): ((94, 34), (22, 67)),
        (12748, 12176): ((26, 66), (67, 21)),
        (7870, 6450): ((17, 86), (84, 37)),
        (18641, 10279): ((69, 23), (27, 71)),
    }
    assert first_part(machines) == 480


def test_find_movements():
    machines = {
        (8400, 5400): ((94, 34), (22, 67)),
        (12748, 12176): ((26, 66), (67, 21)),
        (7870, 6450): ((17, 86), (84, 37)),
    }

    expected = {
        (8400, 5400): (80, 40),
        (12748, 12176): (141.4045407636739, 135.3952528379773),
        (7870, 6450): (38, 86),
    }
    for key in machines:
        assert expected[key] == find_movements(key, machines)


if __name__ == "__main__":
    machines = get_data("./day13/input")
    coins = first_part(machines)
    print(f"Total of tokens to win in the first part is {coins}")

    coins = second_part(machines)
    print(f"Total of tokens to win in the second part is {coins}")
