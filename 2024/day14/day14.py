import re

import matplotlib.pyplot as plt
import numpy as np


def read_initial_conditions(fname):
    """
    Reads the initial conditions from a file and returns them as a list of tuples.
    Each tuple contains a position (px, py) and velocity (vx, vy).
    """
    initial_conditions = []
    with open(fname, "r") as file:
        lines = file.readlines()
    # Match lines with the format: p=<px>,<py> v=<vx>,<vy>
    for line in lines:
        match = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line.strip())
        if match:
            # Convert matched values into integers and append to the list
            px, py, vx, vy = map(int, match.groups())
            initial_conditions.append(((px, py), (vx, vy)))
    return initial_conditions


def new_position(start_position, velocity, time, grid_height, grid_width):
    """
    Calculates the new position of a robot after a certain amount of time
    based on its initial position and velocity.
    """
    x = (start_position[0] + velocity[0] * time) % grid_width
    y = (start_position[1] + velocity[1] * time) % grid_height
    return x, y


def first_part(initial_conditions, time, grid_height, grid_width):
    """
    Calculates the safety factor based on the number of robots in each quadrant
    of the grid at a given time.
    Excludes robots that are in the middle of the grid.
    """
    quadrants = [0, 0, 0, 0]
    for condition in initial_conditions:
        start_position = condition[0]
        velocity = condition[1]

        # Calculate the new position of the robot after the given time
        x, y = new_position(start_position, velocity, time, grid_height, grid_width)

        # Exclude robots located at the center (middle) of the grid
        if x == grid_width // 2 or y == grid_height // 2:
            continue
        # Update the count of robots in the appropriate quadrant
        if x < grid_width // 2 and y < grid_height // 2:
            quadrants[0] += 1  # Top-left quadrant
        elif x >= grid_width // 2 and y < grid_height // 2:
            quadrants[1] += 1  # Top-right quadrant
        elif x < grid_width // 2 and y >= grid_height // 2:
            quadrants[2] += 1  # Bottom-left quadrant
        elif x >= grid_width // 2 and y >= grid_height // 2:
            quadrants[3] += 1  # Bottom-right quadrant

    # Calculate the product of robot counts in all quadrants
    safety_factor = 1
    for count in quadrants:
        safety_factor *= count

    return safety_factor


def second_part(initial_conditions, times, grid_height, grid_width):
    """
    Simulates the movement of robots on a grid, checking for valid positions
    (no collisions).
    The simulation runs until a valid configuration of robot positions is found, and
    the positions are plotted.
    """
    # Initialize time
    time = 0
    while True:
        # Increment time with each iteration
        time += 1
        # Set to store the positions of robots
        positions = set()
        # Assume the configuration is valid unless proven otherwise
        valid = True

        print(time)
        for condition in initial_conditions:
            # extract initial conditions
            start_position = condition[0]
            velocity = condition[1]
            # Calculate the new position of the robot after the given time
            x, y = new_position(start_position, velocity, time, grid_height, grid_width)

            # If the position already exists, a collision occurs, and we stop the
            # simulation for this time
            if (x, y) in positions:
                valid = False
                break
            # Add the new position to the set of positions
            positions.add((x, y))

        # If all positions are unique (no collision), plot the positions and return the
        # results
        if valid:
            print(f"Number of valid positions: {len(positions)}")
            # Plot positions on the grid
            plt.plot([key[0] for key in positions], [key[1] for key in positions], "*")
            plt.xlim(0, grid_width)
            plt.ylim(0, grid_height)
            plt.title(f"Time: {time}")
            plt.show()
            return time, positions


def test_first_part():
    init_cond = read_initial_conditions("./day14/test")
    value = first_part(init_cond, 100, 7, 11)
    assert value == 12


def test_new_position():
    new = new_position((2, 4), (2, -3), 5, 7, 11)
    assert new == (1, 3)


if __name__ == "__main__":
    fname = "./day14/input"
    init_cond = read_initial_conditions(fname)
    value = first_part(init_cond, 100, 103, 101)
    print(f"The safety factor after exactly 100 seconds is: {value}")
    time, positions = second_part(init_cond, 10, 103, 101)
    print(f"Seconds: {time}")
