"""
Script to solve the 5th Day
"""


def first_part(fname):
    """
    Solution of the first part of the problem.

    Return a string.
    """
    file = _read_input(fname)
    # Create a list with the columns to accommodate the crate according to the
    # first lines of the file
    stacks = _initial_stacks_arange(file)
    # Make the crate movements according to the file
    stacks = _crate_mover_9000(file, stacks)
    # Create a list with last element of each columns into the stacks
    solution = [column[-1] for column in stacks]
    # Create a string from the list
    solution = "".join(solution)
    return solution


def second_part(fname):
    """"""
    file = _read_input(fname)
    # Create a list with the columns to accommodate the crate according to the
    # first lines of the file
    stacks = _initial_stacks_arange(file)
    # Make the crate movements according to the file
    stacks = _crate_mover_9001(file, stacks)
    # Create a list with last element of each columns into the stacks
    solution = [column[-1] for column in stacks]
    # Create a string from the list
    solution = "".join(solution)
    return solution


def _crate_mover_9001(file, stacks):
    """
    Move the crates according to the movements of the file.

    Return the stacks as a list with the new configuration of the crate in the
    columns.
    """
    # Set up a flag
    read_move = False
    for line in file:
        if line == "":
            read_move = True
            continue
        if not read_move:
            continue
        if line[0] == "m":
            move = line.split(" ")
            cuantity, from_stack, to_stack = tuple(int(move[i]) for i in (1, 3, 5))
            # Add the crates to one column of the list and remove them from the
            # other column
            stacks[to_stack - 1].extend(stacks[from_stack - 1][-cuantity:])
            stacks[from_stack - 1] = stacks[from_stack - 1][:-cuantity]
    return stacks


def _crate_mover_9000(file, stacks):
    """
    Move the crates according to the movements of the file.

    Return the stacks as a list with the new configuration of the crate in the
    columns.
    """
    # Set up a flag
    read_move = False
    for line in file:
        if line == "":
            read_move = True
            continue
        if not read_move:
            continue
        # Make the movement.
        if line[0] == "m":
            move = line.split(" ")
            # Set up the movements
            cuantity, from_stack, to_stack = tuple(int(move[i]) for i in (1, 3, 5))
            for i in range(cuantity):
                # Remove the last element
                tmp = stacks[from_stack - 1].pop()
                # Append this element to the other column
                stacks[to_stack - 1].append(tmp)
    return stacks


def _initial_stacks_arange(file):
    """
    Generate the stacks and arrange the crate according to the first lines of
    the file.

    Return a list with the crate in each columns as lists.
    """
    # Find the number of stacks from the file
    for line in file:
        # Find the line where the first element is 1
        if line[1] == "1":
            n_columns = int(line.strip()[-1])
            break
    # Create a list with n_number of stacks as list
    stacks = [[] for _ in range(n_columns)]
    # Read first lines and fill the stacks
    for line in file:
        if line[1] == "1":
            break
        for column in range(n_columns):
            # Calculate the index of the crate that corresponds to each stacks
            index = 4 * column + 1
            # Add the crate in the stacks
            if index < len(line) and line[index] != " ":
                stacks[column].append(line[index])
    # Reverse the order of the elements in each stack
    stacks = [column[::-1] for column in stacks]
    return stacks


def _read_input(fname):
    """
    Read the file.

    Return a list with the assignment pairs.
    """
    with open(fname, "r") as f:
        return f.read().splitlines()


def test_initial_stacks_arange():
    expected = [["Z", "N"], ["M", "C", "D"], ["P"]]
    file = _read_input("test_input")
    assert _initial_stacks_arange(file) == expected


def test_crate_mover_9000():
    expected = [["C"], ["M"], ["P", "D", "N", "Z"]]
    file = _read_input("test_input")
    assert _crate_mover_9000(file, [["Z", "N"], ["M", "C", "D"], ["P"]]) == expected


def test_crate_mover_9001():
    expected = [["M"], ["C"], ["P", "Z", "N", "D"]]
    file = _read_input("test_input")
    assert _crate_mover_9001(file, [["Z", "N"], ["M", "C", "D"], ["P"]]) == expected


if __name__ == "__main__":
    # Solve first part
    solution = first_part("input")

    # Solve second part
    solution_2 = second_part("input")

    print(
        "Answerers:",
        "\n",
        "- First part: ",
        f"{solution}",
        "\n",
        "- Second part: ",
        f"{solution_2}",
    )
