"""
Script to solve the 8th Day
"""


def get_n_columns(data):
    return len(data[0])


def get_n_rows(data):
    return len(data)


def first_part(fname):
    """
    Solve the first part.
    """
    data = _read_input(fname)
    visible_trees = (len(data) + len(data[0])) * 2 - 4
    print(visible_trees)
    for row in range(1, get_n_rows(data) - 1):
        for col in range(1, get_n_columns(data) - 1):
            if is_visible(row, col, data):
                visible_trees += 1
    return visible_trees


def is_visible(row, col, data):
    if (
        _for_left(row, col, data)
        or _for_rigth(row, col, data)
        or _for_top(row, col, data)
        or _for_bottom(row, col, data)
    ):
        return True
    return False


def _for_left(row, col, data):
    """
    Return True if the tree is visible, else return False.
    """
    for element in data[row][:col]:
        if data[row][col] <= element:
            return False
    return True


def _for_rigth(row, col, data):
    for element in data[row][col + 1 :]:
        if data[row][col] <= element:
            return False
    return True


def _for_bottom(row, col, data):
    col_trees = [data[r][col] for r in range(get_n_rows(data))]
    for element in col_trees[row + 1 :]:
        if data[row][col] <= element:
            return False
    return True


def _for_top(row, col, data):
    col_trees = [data[r][col] for r in range(get_n_rows(data))]
    for element in col_trees[:row]:
        if data[row][col] <= element:
            return False
    return True


def _read_input(fname):
    """
    Read the file.

    Return a list.
    """
    with open(fname, "r") as f:
        lines = [[int(n) for n in line.rstrip()] for line in f]
    return lines


def test_for_side_function():
    data = _read_input("test_input")
    assert _for_left(0, 3, data) == True
    assert _for_left(1, 3, data) == False

    assert _for_rigth(1, 2, data) == True
    assert _for_rigth(0, 1, data) == False

    assert _for_top(2, 0, data) == True
    assert _for_top(3, 1, data) == False

    assert _for_bottom(2, 0, data) == True
    assert _for_bottom(2, 2, data) == False


def test_is_visible():
    data = _read_input("test_input")
    assert is_visible(0, 3, data) == True
    assert is_visible(1, 3, data) == False


def test_first_part():
    assert first_part("test_input") == 21


if __name__ == "__main__":
    # Solve first part
    visible_trees = first_part("input")
    # Solve second part
    print(
        "Answerers:",
        "\n",
        "- First part: ",
        f"{visible_trees}",
    )
