"""
Script to solve the 1st Day
"""


def read_input(fname):
    """
    Read the file and split the lines.

    Return a list where its elements are strings.
    """
    lines = open(fname, "r").read().splitlines()
    return lines


def first_part(lines):
    """
    Return a list with the total of calories obtained by each Elves.
    """
    # Initialize a empty list to store the calories
    calories_list = [[]]
    # Store each elf food supply in a list
    for line in lines:
        if line.strip():
            calories_list[len(calories_list) - 1].append(int(line))
        else:
            calories_list.append([])

    # Sum each list item to find the total calories for each elf
    # Initialize a empty list to store the total calories
    sum_calories = []
    for calories in calories_list:
        sum_calories.append(sum(calories))
    return sum_calories


def second_part(sum_calories):
    """
    Calculate the total calories obtained by the top three Elves
    carrying the most calories.

    Return a float.
    """
    # Sort the list item
    sum_calories.sort(reverse=True)
    return sum(sum_calories[:3])


def test_first_part():
    """
    Test the first part
    """
    expected_calories_list = [6000, 4000, 11000, 24000, 10000]
    # Solve first part
    # Read the test file
    lines = read_input("test_input")
    # Compare with the expected result
    assert first_part(lines) == expected_calories_list


def test_second_part():
    """
    Test the second part
    """
    expected_top_calories = 45000
    # Solve second part
    # Read the test file
    lines = read_input("test_input")
    # Calculate the total calories for each Elves
    calories_list = first_part(lines)
    # Calculate the total calories for the top 3 Elves
    top_calories = second_part(calories_list)
    # Compare with the expected result
    assert top_calories == expected_top_calories


if __name__ == "__main__":

    # Read input file
    fname = "input"
    lines = read_input(fname)

    # Solve first part
    calories_list = first_part(lines)
    # Find the maximum value in the list
    max_calories = max(calories_list)

    # Solve second part
    top_calories = second_part(calories_list)

    print(
        "Answerers:",
        "\n",
        "- First part: ",
        f"{max_calories}",
        "\n",
        "- Second part: ",
        f"{top_calories}",
    )
