def read_file(fname):
    """Reads a file containing the grid and returns it as a 2D array."""
    with open(fname) as file:
        input_data = [list(map(int, line.strip())) for line in file]
    return input_data


def find_height(map, row, col):
    """
    This function searches for all possible endpoints starting from a given position
    (row, col) on the map, where each endpoint is a cell with the value of 9.
    It does this by checking all neighboring cells in the map to see if they have
    incremented values, and it tracks all valid paths to the endpoints.
    """
    # Directions for moving in the grid (up, down, left, right)
    directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "righ": (0, 1)}
    nrow = len(map)
    ncol = len(map[0])

    endpoints = []
    current = [(row, col)]

    # Explore the grid systematically to find all the path to a 9
    while current:
        row, col = current.pop(0)
        current_value = map[row][col]
        next_value = current_value + 1

        # Check all four directions
        for dir in directions:
            nextv = (row + directions[dir][0], col + directions[dir][1])
            # Ensure the next position is in the map and matches the next value
            if (
                0 <= nextv[0] < nrow
                and 0 <= nextv[1] < ncol
                and map[nextv[0]][nextv[1]] == next_value
            ):
                # If the next value is 9, it's an endpoint.
                # Otherwise, add the next position to the queue for further exploration
                if next_value == 9:
                    endpoints.append(nextv)
                else:
                    current.append(nextv)
    return endpoints


def first_part(map):
    nrow, ncol = len(map), len(map[0])
    score = 0

    # Iterate over every cell in the map
    for row in range(nrow):
        for col in range(ncol):
            # Find a trail-head and find the associated path to a 9
            if map[row][col] == 0:
                endpoints = find_height(map, row, col)
                score += len(set(endpoints))
    return score


def second_part(map):
    nrow, ncol = len(map), len(map[0])
    score = 0

    # Iterate over every cell in the map
    for row in range(nrow):
        for col in range(ncol):
            if map[row][col] == 0:
                endpoints = find_height(map, row, col)
                score += len(endpoints)
    return score


def test_first_part():
    map = [[0, 1, 2, 3], [1, 2, 3, 4], [8, 7, 6, 5], [9, 8, 7, 6]]
    assert first_part(map) == 1
    map = [
        [8, 9, 0, 1, 0, 1, 2, 3],
        [7, 8, 1, 2, 1, 8, 7, 4],
        [8, 7, 4, 3, 0, 9, 6, 5],
        [9, 6, 5, 4, 9, 8, 7, 4],
        [4, 5, 6, 7, 8, 9, 0, 3],
        [3, 2, 0, 1, 9, 0, 1, 2],
        [0, 1, 3, 2, 9, 8, 0, 1],
        [1, 0, 4, 5, 6, 7, 3, 2],
    ]
    assert first_part(map) == 36


def test_second_part():
    map = [
        [9, 9, 9, 9, 9, 0, 1],
        [9, 9, 4, 3, 2, 1, 9],
        [9, 9, 5, 9, 9, 2, 9],
        [9, 9, 6, 5, 4, 3, 9],
        [9, 9, 7, 9, 9, 4, 9],
        [1, 1, 8, 7, 6, 5, 9],
        [1, 1, 9, 1, 1, 1, 1],
    ]
    assert second_part(map) == 3

    map = [
        [8, 9, 0, 1, 0, 1, 2, 3],
        [7, 8, 1, 2, 1, 8, 7, 4],
        [8, 7, 4, 3, 0, 9, 6, 5],
        [9, 6, 5, 4, 9, 8, 7, 4],
        [4, 5, 6, 7, 8, 9, 0, 3],
        [3, 2, 0, 1, 9, 0, 1, 2],
        [0, 1, 3, 2, 9, 8, 0, 1],
        [1, 0, 4, 5, 6, 7, 3, 2],
    ]

    assert second_part(map) == 81


if __name__ == "__main__":
    map = read_file("./day10/input")
    score = first_part(map)
    print(f" The sum of the scores of all trailheads is: {score}")

    score = second_part(map)
    print(f" The sum of the ratings of all trailheads is: {score}")
