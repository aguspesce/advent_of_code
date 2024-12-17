def read_file(fname):
    """Reads a file containing the garden and returns it as a 2D array."""
    with open(fname) as file:
        input_data = [line.strip() for line in file]
    return input_data


def get_area(group):
    """Calculate the area of a group of connected cells"""
    # Area is the number of cells in the group
    area = len(group)
    return area


def get_current_garden(map, coord, visited):
    """
    Explore the 2D array from a starting coordinate, marking connected cells and
    calculating perimeter/area.

    Return the visited position array, perimeter and area.
    """
    # Directions to explore (right, left, down, up)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # Dimensions of the 2D array
    rows, cols = len(map), len(map[0])
    # Starting position
    row, col = coord
    # Define the type of letter at the starting coordinate (defines the group)
    letter = map[row][col]

    # Initialize perimeter, list to hold the coordinate of the group and stack
    # for the search
    perimeter = 0
    group = []
    stack = [(row, col)]

    # Explore the array
    while stack:
        # Pop the next coordinate to explore
        row, col = stack.pop()
        # Skip if the cell position is already in the group
        if (row, col) in group:
            continue
        # Add the current cell position to the group and  mark the cell as visited
        group.append((row, col))
        visited[row][col] = True

        # Explore adjacent cells
        for dy, dx in directions:
            # Calculate new coordinates
            new_row, new_col = row + dy, col + dx
            # Check if the new coordinates are within bounds and if it belongs to the
            # same group. IF it is True, add it to the stack to explore later
            if (
                0 <= new_row < rows
                and 0 <= new_col < cols
                and map[new_row][new_col] == letter
            ):
                stack.append((new_row, new_col))
            else:
                # Increment perimeter if it's a boundary cell
                perimeter += 1
    # Get the area of the group
    area = get_area(group)

    return visited, perimeter, area


def first_part(map):
    # Get the dimensions of the 2D array
    nrows, ncols = len(map), len(map[0])
    # Initialize the visited map and the list to store the price of each group
    visited = [[False for _ in range(ncols)] for row in range(nrows)]
    price = []

    for row in range(nrows):
        for col in range(ncols):
            # If the cell is not visited yet, it's the start of a new group
            if not visited[row][col]:
                visited, perimeter, area = get_current_garden(map, (row, col), visited)
                # Add the price (area * perimeter) to the list
                price.append(area * perimeter)
            else:
                # Skip cells that have already been visited
                continue
    return price


def test_get_current_garden():
    map = [
        ["a", "a", "a", "c"],
        ["a", "b", "c", "d"],
        ["b", "b", "c", "c"],
        ["e", "e", "e", "c"],
    ]
    visited = [[False for _ in range(4)] for row in range(4)]
    expected = visited.copy()
    expected[0][0], expected[1][0], expected[0][1], expected[0][2] = (
        True,
        True,
        True,
        True,
    )
    visited, _, _ = get_current_garden(map, (0, 0), visited)
    assert visited == expected

    map = [
        ["o", "o", "o", "o", "o"],
        ["o", "x", "o", "x", "o"],
        ["o", "o", "o", "o", "o"],
        ["o", "x", "o", "x", "o"],
        ["o", "o", "o", "o", "o"],
    ]
    visited = [[False for _ in range(5)] for row in range(5)]
    _, perimeter, area = get_current_garden(map, (0, 0), visited)
    assert (perimeter, area) == (36, 21)


def test_first_part():
    map = [
        ["o", "o", "o", "o", "o"],
        ["o", "x", "o", "x", "o"],
        ["o", "o", "o", "o", "o"],
        ["o", "x", "o", "x", "o"],
        ["o", "o", "o", "o", "o"],
    ]
    assert sum(first_part(map)) == 772


if __name__ == "__main__":
    map = read_file("./day12/input")
    prices = first_part(map)
    print(f"The total price is {sum(prices)}")
