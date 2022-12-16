"""
Script to solve the 5th Day
"""


def first_part(fname):
    """
    Solve the first part.

    Return a int with the marker value
    """
    # Read the file
    line = _read_input(fname)
    # Find the marker
    marker = _find_marker(line, 4)
    return marker


def second_part(fname):
    """
    Solve the second part.

    Return a int with the marker value
    """
    # Read the file
    line = _read_input(fname)
    # Find the marker
    marker = _find_marker(line, 14)
    return marker


def _find_marker(line, offset=4):
    """
    Find the marker.

    Return a int.
    """
    for i in range(0, len(line) - offset - 1):
        char = line[i : i + offset]
        if len(char) == len(set(char)):
            marker = i + offset
            break
    return marker


def _read_input(fname):
    """
    Read the file.

    Return a list.
    """
    with open(fname, "r") as f:
        line = [*f.readline().strip()]
    return line


def test_find_marker():
    expected_4 = [7, 5]
    expected_14 = [19, 23]
    lines = ["mjqjpqmgbljsphdztnvjfqwrcgsmlb", "bvwbjplbgvbhsrlpgdmjqwftvncz"]
    for line, value in zip(lines, expected_4):
        line = [*line]
        assert _find_marker(line, 4) == value
    for line, value in zip(lines, expected_14):
        line = [*line]
        assert _find_marker(line, 14) == value


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
