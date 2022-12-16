"""
Script to solve the 3th Day
"""


def first_part(fname):
    """
    Return a list with the priorities for each item that appears in the
    compartments.
    """
    # Read the file
    lines = _read_input(fname)
    # Initialize a list tho store the priorities
    values = []
    for line in lines:
        # Split the line in 2 compartment
        comp_1, comp_2 = _get_compartment(line)
        # Find the common letter
        letter = _find_commmon_letter([set(comp_1), set(comp_2)])
        # Append the priority value of the given letter
        values.append(_letter_to_priority(letter[0]))
    return values


def second_part(fname):
    """
    Return a list with the item type that corresponds to the badges of
    each three-Elf group.
    """
    # Read the file
    lines = _read_input(fname)
    # Initialize a list to store the priorities
    values = []
    for i in range(0, len(lines), 3):
        # Generate group of 3 lines
        group = [set(line) for line in lines[i : i + 3]]
        # Find the common letter
        letter = _find_commmon_letter(group)
        # Append the priority value of the given letter
        values.append(_letter_to_priority(letter[0]))
    return values


def _read_input(fname):
    """
    Read the file and split the lines.

    Return a list where its elements are strings.
    """
    with open(fname, "r") as f:
        return f.read().splitlines()


def _get_compartment(line):
    """
    Return 2 string that represent 2 compartment
    """
    comp_1, comp_2 = line[: len(line) // 2], line[len(line) // 2 :]
    return comp_1, comp_2


def _find_commmon_letter(compartments):
    """
    Return a list with the common letter for a group of compartments
    """
    return list(set.intersection(*compartments))


def _letter_to_priority(letter):
    """
    Return a float with the priority value for a given letter
    """
    # priority list rankings
    priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return priority.find(letter) + 1


def test_get_compartment():
    """
    Check function
    """
    expected_comp = ("vJrwpWtwJgWr", "hcsFMMfFFhFp")
    line = "vJrwpWtwJgWrhcsFMMfFFhFp"
    comps = _get_compartment(line)
    for expected, comp in zip(expected_comp, comps):
        assert comp == expected


def test_find_common_letter():
    """
    Check the function
    """
    expected_letter = "p"
    comp_1, comp_2 = "vJrwpWtwJgWr", "hcsFMMfFFhFp"
    common_letter = _find_commmon_letter([set(comp_1), set(comp_2)])
    assert common_letter[0] == expected_letter


def test_letter_to_priority():
    """
    Check the letter to priority function
    """
    expected_priorities = [1, 26, 27, 52]
    letters = ["a", "z", "A", "Z"]
    for priority, letter in zip(expected_priorities, letters):
        assert _letter_to_priority(letter) == priority


if __name__ == "__main__":

    # Solve first part
    priorities_values_1 = first_part("input")

    # Solve the second part
    priorities_values_2 = second_part("input")

    print(
        "Answerers:",
        "\n",
        "- First part: ",
        f"{sum(priorities_values_1)}",
        "\n",
        "- Second part: ",
        f"{sum(priorities_values_2)}",
    )
