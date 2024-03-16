def read_movements(fname):
    """
    Return a list with the movements
    """
    with open(fname, "r") as f:
        lines = f.readlines()
    moves = [[line[0], int(line[2:-1])] for line in lines]
    return moves


def rope_snaps(moves, n_knots=1):
    """
    Return a list with the positions of the tail of the rope
    """
    # Initialize the position of the knots. They are overlap.
    # The element 0 is the head and the last one is the tail
    knots_position = [[0, 0] for _ in range(n_knots + 1)]
    # Initialize a list to save the tail positions
    tail_positions = []
    # Update the knots positions according to the movements
    for move in moves:
        direction, value = move[0], move[1]
        for _ in range(value):
            # Move the first knot (head)
            knots_position[0] = _move_head(knots_position[0], direction)
            # Move the other knots
            for knot in range(1, n_knots + 1):
                knots_position[knot] = _move_tail(
                    knots_position[knot], knots_position[knot - 1]
                )
            # Add tail position in the list
            if knots_position[-1] not in tail_positions:
                tail_positions.append(knots_position[-1].copy())
    return tail_positions


def test_rope_snaps():
    """
    Check the rope_snaps function
    """
    # File names
    files = ["test_input", "test_input_2"]
    # knots number
    n_knots = [1, 9]
    # Expected results
    expected = [13, 36]
    # Check the function
    for file, knots, value in zip(files, n_knots, expected):
        moves = read_movements(file)
        tail_positions = rope_snaps(moves, knots)
        assert len(tail_positions) == value


def _move_head(head, direction):
    """
    Function to update the head position.

    Return a list
    """
    # Dictionary with the direction sign
    directions_dics = {"R": (0, 1), "L": (0, -1), "U": (1, 1), "D": (1, -1)}
    # Set the axis and the sign to update the head
    axis, sign = directions_dics[direction]
    # Update the position
    head[axis] += sign * 1
    return head


def test_move_head():
    """
    Check _move_head function
    """
    assert _move_head([0, 0], "R") == [1, 0]


def _move_tail(tail, head):
    """
    Update the knots position according to the head movement.

    Return a list with the updated tail position.
    """
    if (abs(head[0] - tail[0]) <= 1) and (abs(head[1] - tail[1]) <= 1):
        return tail
    # Horizontal movement
    if (abs(head[0] - tail[0]) > 1) and (head[1] == tail[1]):
        tail[0] += sign_function(head[0] - tail[0])
    # Vertical movement
    if (abs(head[1] - tail[1]) > 1) and (head[0] == tail[0]):
        tail[1] += sign_function(head[1] - tail[1])
    # Diagonal movement
    if (abs(head[0] - tail[0]) >= 1) and (abs(head[1] - tail[1]) >= 1):
        # diagonal movement
        tail[0] += sign_function(head[0] - tail[0])
        tail[1] += sign_function(head[1] - tail[1])
    return tail


def test_move_tail():
    """
    Check the _move_tail function
    """
    # Check horizontal movement
    assert _move_tail([0, 0], [2, 0]) == [1, 0]
    # Check vertical movement
    assert _move_tail([0, 0], [0, 2]) == [0, 1]
    # Check diagonal movement
    assert _move_tail([0, 0], [1, 2]) == [1, 1]


def sign_function(value):
    """
    Return a sign of a given value
    """
    if value > 0:
        return 1
    else:
        return -1


def test_sign_function():
    """
    Check the sign function
    """
    values = [-2, 2]
    expected = [-1, 1]
    for value, exp in zip(values, expected):
        assert sign_function(value) == exp


if __name__ == "__main__":
    # Read movements
    moves = read_movements("input")

    # Solve first part
    tail_positions = rope_snaps(moves, n_knots=1)
    len_tail_positions = len(tail_positions)

    # Solve second part
    tail_positions_2 = rope_snaps(moves, n_knots=9)
    len_tail_positions_2 = len(tail_positions_2)

    print(
        "Answers:",
        "\n",
        f"First part: {len_tail_positions}",
        "\n" f"Second part: {len_tail_positions_2}",
    )
