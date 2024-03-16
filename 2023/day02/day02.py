from dataclasses import dataclass

MAX_CUBES = {"red": 12, "green": 13, "blue": 14}


@dataclass
class Set:
    """Create a game dataclass"""

    red: int
    blue: int
    green: int

    def is_possible(self):
        """Return if a set is possible"""
        if (
            self.red > MAX_CUBES["red"]
            or self.blue > MAX_CUBES["blue"]
            or self.green > MAX_CUBES["green"]
        ):
            return False
        return True


@dataclass
class Game:
    """Create a set data class"""

    game_id: int
    game_sets: list[Set]

    def is_possible(self):
        """Return if the game is possible"""
        if all([gset.is_possible() for gset in self.game_sets]) is False:
            return False
        return True

    def game_power(self):
        """Return the game power"""
        max_red = max([val.red for val in self.game_sets])
        max_blue = max([val.blue for val in self.game_sets])
        max_green = max([val.green for val in self.game_sets])
        return max_red * max_blue * max_green


def input_parser(fname):
    """Parser the input file as a dataclass"""
    games = []
    with open(fname) as data:
        for line in data:
            game_id, game_sets = line.split(": ")
            game_id = game_id.replace("Game ", "")
            game_sets_list = []
            for gset in game_sets.split(";"):
                red, green, blue = 0, 0, 0
                for cubes in gset.strip().split(","):
                    count, color = cubes.strip().split(" ")
                    if color == "red":
                        red = int(count)
                    elif color == "blue":
                        blue = int(count)
                    else:
                        green = int(count)
                set_i = Set(red, blue, green)
                game_sets_list.append(set_i)
            games.append(Game(int(game_id), game_sets_list))
    return games


def part_one(games):
    """Solve first part"""
    result = sum([game.game_id for game in games if game.is_possible()])
    return result


def part_two(games):
    """Solve second part"""
    power_sum = 0
    for game in games:
        power_sum += game.game_power()
    return power_sum


if __name__ == "__main__":
    # Read input file
    fname = "input.txt"
    games = input_parser(fname)
    result = part_one(games)
    print("The sum of the IDs of those games is: ", result)
    result2 = part_two(games)
    print("the sum of the power of these sets is: ", result2)
