"""
Script to solve the 8th Day
"""


def get_n_columns(data):
    return len(data[0])


def get_n_rows(data):
    return len(data)


def get_scores(fname):
    """
    Return a list with the score for each tree in the grid.
    """
    # Load the data
    data = _read_input(fname)
    # Initialize a list to append the score for each tree
    scores = []
    # Get the score for each tree
    for row in range(1, get_n_rows(data) - 1):
        for col in range(1, get_n_columns(data) - 1):
            scores.append(get_tree_score(row, col, data))
    return scores


def get_tree_score(row, col, data):
    """
    Return a int with the score for a given tree.
    """
    tree_score = (
        _count_left(row, col, data)
        * _count_right(row, col, data)
        * _count_top(row, col, data)
        * _count_bottom(row, col, data)
    )
    return tree_score


def _count_left(row, col, data):
    """
    Calculate the number of visible tree on the left
    """
    count = 0
    for element in data[row][:col][::-1]:
        if element < data[row][col]:
            count += 1
        if element >= data[row][col]:
            count += 1
            break
    return count


def _count_right(row, col, data):
    """
    Calculate the number of visible tree on the right
    """
    count = 0
    for element in data[row][col + 1 :]:
        if element < data[row][col]:
            count += 1
        if element >= data[row][col]:
            count += 1
            break
    return count


def _count_bottom(row, col, data):
    """
    Calculate the number of visible tree on the bottom
    """
    col_trees = [data[r][col] for r in range(get_n_rows(data))]
    count = 0
    for element in col_trees[row + 1 :]:
        if element < data[row][col]:
            count += 1
        if element >= data[row][col]:
            count += 1
            break
    return count


def _count_top(row, col, data):
    """
    Calculate the number of visible tree on the top
    """
    col_trees = [data[r][col] for r in range(get_n_rows(data))]
    count = 0
    for element in col_trees[:row][::-1]:
        if element < data[row][col]:
            count += 1
        if element >= data[row][col]:
            count += 1
            break
    return count


def test_count_functions():
    data = _read_input("test_input")
    assert _count_left(1, 2, data) == 1
    assert _count_right(1, 2, data) == 2
    assert _count_top(1, 2, data) == 1
    assert _count_bottom(1, 2, data) == 2


def test_get_tree_score():
    data = _read_input("test_input")
    assert get_tree_score(1, 2, data) == 4


def test_get_scores():
    expected = [1, 4, 1, 6, 1, 2, 1, 8, 3]
    assert get_scores("test_input") == expected


def _read_input(fname):
    """
    Read the file.

    Return a list.
    """
    with open(fname, "r") as f:
        lines = [[int(n) for n in line.rstrip()] for line in f]
    return lines


if __name__ == "__main__":
    # Solve second part
    scores = get_scores("input")
    max_score = max(scores)

    print(
        "Answerers:",
        "\n",
        "- Second part: ",
        f"{max_score}",
    )
