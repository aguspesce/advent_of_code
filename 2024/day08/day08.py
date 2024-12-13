import itertools


def read_file(fname):
    """Reads a file containing the grid and returns it as a 2D array."""
    with open(fname) as file:
        input_data = [list(line.strip()) for line in file]
    return input_data


class Grid_map:
    """
    A class representing a grid map that contains antennas and computes antinode
    pairs based on antenna positions.
    """

    def __init__(self, grid):
        self.grid = grid
        self.nrow = len(grid)
        self.ncol = len(grid[0])
        self.antenas = {}

    def find_antenas(self):
        """
        Finds all antennas in the grid and stores their positions.
        """
        for row in range(self.nrow):
            for col in range(self.ncol):
                element = self.grid[row][col]
                if element != ".":
                    if element not in self.antenas:
                        self.antenas[element] = [(row, col)]
                    else:
                        self.antenas[element].append((row, col))

    def antinode_pair(self, position1, position2):
        """Calculates the antinode pair for two positions in the grid."""
        row1, col1 = position1[0], position1[1]
        row2, col2 = position2[0], position2[1]

        dr = row2 - row1
        dc = col2 - col1

        return (row1 - dr, col1 - dc), (row1 + 2 * dr, col1 + 2 * dc)

    def antinode_on_map(self, antinode):
        """Checks if the calculated antinode is within the bounds of the grid."""
        if antinode[0] < 0 or antinode[0] > self.nrow - 1:
            return False
        if antinode[1] < 0 or antinode[1] > self.ncol - 1:
            return False
        return True

    def all_antinode(self, antena_key):
        """Computes all antinode for a specific antenna."""
        antinodes = []
        combination = list(itertools.combinations(self.antenas[antena_key], 2))

        # Generate antinode pairs for each combination of antenna positions
        for comb in combination:
            antinode1, antinode2 = self.antinode_pair(comb[0], comb[1])
            if self.antinode_on_map(antinode1):
                antinodes.append(antinode1)
            if self.antinode_on_map(antinode2):
                antinodes.append(antinode2)
        return antinodes


def test_grid_map():
    map = [
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", "a", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", "a", ".", ".", ".", "."],
        [".", ".", ".", "a", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", "A", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    ]
    grid = Grid_map(map)
    grid.find_antenas()
    antenas = grid.antenas
    assert antenas["a"] == [(3, 4), (4, 5), (5, 3)]
    assert antenas["A"] == [(7, 5)]
    assert grid.all_antinode("A") == []
    assert grid.all_antinode("a") == [(2, 3), (5, 6), (1, 5), (7, 2), (3, 7), (6, 1)]


def test_first_part():
    map = read_file("./day08/test")
    assert first_part(map) == 14


def first_part(map):
    grid = Grid_map(map)
    grid.find_antenas()
    antenas_keys = grid.antenas.keys()
    antinodes = []
    for key in antenas_keys:
        antinodes.extend(grid.all_antinode(key))

    antinodes = set(antinodes)
    return len(antinodes)


if __name__ == "__main__":
    fname = "./day08/input"
    map = read_file(fname)
    value = first_part(map)
    print(f"unique locations within the bounds of the map contain an antinode: {value}")
