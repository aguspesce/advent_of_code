import copy

# Directions mapping: up (^), down (v), left (<), right (>)
dirs = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
}


def load_data(fname):
    """
    Loads the grid and movement instructions from a file. Return a tuple containing
    the grid and the movements
    """
    movements = []
    grid = []
    with open(fname) as file:
        for line in file:
            line = line.strip()
            if len(line) > 1:
                if line[0] == "#":
                    # Adding grid lines to the grid list
                    grid.append(list(line))
                else:
                    # Adding movement instructions to the list
                    movements.append(line)
    # Combine all movement instructions into a single string
    movements = list("".join(movements))
    return grid, movements


def find_robot(grid):
    """
    Finds the position of the robot in the grid. Return the row and column indices of
    the robot in the grid.
    """
    for line in range(len(grid)):
        for ele in range(len(grid[line])):
            if grid[line][ele] == "@":
                return (line, ele)


def update_grid(grid, neighbors, move):
    """
    Updates the grid by moving objects in the direction specified by `move`.
    """
    update_grid = copy.deepcopy(grid)
    for neighbor in neighbors:
        # Calculate the position of the item before the movement
        before = (neighbor[0] - dirs[move][0], neighbor[1] - dirs[move][1])
        # Update the position of each element in the neighbors list
        update_grid[neighbor[0]][neighbor[1]] = grid[before[0]][before[1]]
    return update_grid


def moving(grid, moves):
    """
    Simulates robot movement on the grid based on the given movement instructions.
    """
    for move in moves:
        # Find the initial position of the robot
        robot_initial = find_robot(grid)

        # Calculate the next position of the robot based on the direction
        next_position = (
            robot_initial[0] + dirs[move][0],
            robot_initial[1] + dirs[move][1],
        )

        # Move the robot to an empty space (".")
        if grid[next_position[0]][next_position[1]] == ".":
            grid[robot_initial[0]][robot_initial[1]] = "."
            grid[next_position[0]][next_position[1]] = "@"
        # Skip the move if it's a wall ("#")
        elif grid[next_position[0]][next_position[1]] == "#":
            continue
        # If it's a box ("O"), simulate box movement
        elif grid[next_position[0]][next_position[1]] == "O":
            neighbors = [next_position]
            to_check = [next_position]
            while to_check:
                next_position = to_check.pop()
                next_next_position = (
                    next_position[0] + dirs[move][0],
                    next_position[1] + dirs[move][1],
                )
                # Stop checking if we encounter a wall
                if grid[next_next_position[0]][next_next_position[1]] == "#":
                    break
                # If the next space is another box, add it to the check list
                elif grid[next_next_position[0]][next_next_position[1]] == "O":
                    to_check.append(next_next_position)
                    neighbors.append(next_next_position)
                # If the next space is empty, add it to the neighbors to update
                elif grid[next_next_position[0]][next_next_position[1]] == ".":
                    neighbors.append(next_next_position)
                    grid = update_grid(grid, neighbors, move)
                    grid[robot_initial[0]][robot_initial[1]] = "."
    return grid


def resize_grid(grid):
    """
    Resizes the grid by replacing each element with a larger equivalent.
    """
    resize_dir = {
        "#": "##",
        "O": "[]",
        ".": "..",
        "@": "@.",
    }
    new_grid = [list("".join(resize_dir[ele] for ele in line)) for line in grid]
    return new_grid


def first_part(grid, moves):
    """
    Solves the first part of the problem.
    """
    grid = moving(grid, moves)
    gps_value = 0

    # Iterate through the grid to find all boxes ("O") and calculate their GPS value
    for line in range(len(grid)):
        for ele in range(len(grid[line])):
            if grid[line][ele] == "O":
                value = line * 100 + ele
                gps_value += value
    return gps_value


def test_first_part():
    grid, moves = load_data("./day15/test2")
    value = first_part(grid, moves)
    assert value == 10092


def test_moving():
    expected = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", ".", "O", ".", "O", ".", "O", "O", "O", "#"],
        ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
        ["#", "O", "O", ".", ".", ".", ".", ".", ".", "#"],
        ["#", "O", "O", "@", ".", ".", ".", ".", ".", "#"],
        ["#", "O", "#", ".", ".", ".", ".", ".", "O", "#"],
        ["#", "O", ".", ".", ".", ".", ".", "O", "O", "#"],
        ["#", "O", ".", ".", ".", ".", ".", "O", "O", "#"],
        ["#", "O", "O", ".", ".", ".", ".", "O", "O", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ]
    grid, moves = load_data("./day15/test2")
    grid = moving(grid, moves)
    assert grid == expected


if __name__ == "__main__":
    fname = "./day15/input"
    grid, moves = load_data(fname)
    value = first_part(grid, moves)
    print(f"The sum of all the boxes GPS is: {value}")
