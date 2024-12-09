def read_file(fname):
    """Reads a file and creates a 2D map representation."""
    map = []
    with open(fname) as file:
        for line in file:
            map.append([li for li in line.strip()])
    return map


class guard:
    """A class representing a guard that moves in a map."""

    def get_guard_initial_pos(self, map):
        """Finds and sets the initial position and direction of the guard in the map."""
        rows, cols = len(map), len(map[0])
        for i in range(rows):
            for j in range(cols):
                if map[i][j] == "^":
                    # Set the guard's initial position and direction
                    self.irow, self.jcol, self.direction = i, j, map[i][j]

    def new_position(self):
        """Calculates the new position of the guard based on its current direction.

        The new row and column of the guard after moving in the current direction.
        """
        if self.direction == "^":
            return self.irow - 1, self.jcol
        if self.direction == ">":
            return self.irow, self.jcol + 1
        if self.direction == "<":
            return self.irow, self.jcol - 1
        if self.direction == "v":
            return self.irow + 1, self.jcol

    def turn(self):
        """
        Turns the guard 90 degrees to the rigth.

        The new direction the guard will face after turning.
        """
        if self.direction == "^":
            return ">"
        if self.direction == ">":
            return "v"
        if self.direction == "<":
            return "^"
        if self.direction == "v":
            return "<"

    def moveit(self, map):
        """
        Moves the guard based on its current position and direction.

        True if the move was successful, False if the guard hits a wall or goes
        out of bounds.
        """
        # Calculate the new position for the guard
        new_irow, new_jcol = self.new_position()

        # Check if the new position is out of bounds
        if new_irow < 0 or new_irow > len(map) - 1:
            return False
        if new_jcol < 0 or new_jcol > len(map[0]) - 1:
            return False

        # Check if the new position is a wall
        if map[new_irow][new_jcol] == "#":
            # Turn the guard
            self.direction = self.turn()
        else:
            # Move the guard to the new position
            self.irow, self.jcol = new_irow, new_jcol
            map[new_irow][new_jcol] = "x"
        return True


def test_get_guard_position():
    map = read_file("day06/test")
    guardia = guard()
    guardia.get_guard_initial_pos(map)
    assert [guardia.irow, guardia.jcol, guardia.direction] == [6, 4, "^"]


def test_first_part():
    map = read_file("day06/test")
    visited = first_part(map)
    assert visited == 41


def first_part(map):
    guardia = guard()
    guardia.get_guard_initial_pos(map)

    # Move the guard until no more moves are possible
    moved = True
    while moved:
        moved = guardia.moveit(map)

    # Count the number of visited positions (marked by "x")
    visied = sum([line.count("x") for line in map])
    return visied


if __name__ == "__main__":
    fname = "day06/input"
    map = read_file(fname)
    value = first_part(map)
    print(f"It visied: {value} ")
