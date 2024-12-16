def read_file(fname):
    """Reads a file and return the stones as a list"""
    with open(fname) as file:
        return file.readline().split()


def split(stone):
    """Split or convert the stone according in the rules"""
    # If the stone is 0 return 1
    if stone == 0:
        return 1

    # If the stone has an even number of digits, it is split into two equal parts.
    str_stone = str(stone)
    ndigit = len(str_stone)
    if ndigit % 2 == 0:
        stone1 = int(str_stone[: ndigit // 2])
        stone2 = int(str_stone[ndigit // 2 :])
        return (stone1, stone2)
    else:
        # If the number of digits is odd, return the stone multiplied by 2024.
        return stone * 2024


def blink(stone, times):
    """
    Make the blinking process of a stone a given number of times.
    Return a dictionary where keys are stone values and values are
    the count of those stones.
    """
    # Start with the initial stone.
    current_track = {stone: 1}

    for _ in range(times):
        new_track = {}

        # For each stone in the current track, determine how it splits or multiplies.
        for current_stone in current_track:
            new_stones = split(current_stone)
            # If the stone splits into two smaller stones, update the new track.
            if isinstance(new_stones, tuple):
                # Add the stone count to the new track
                for new_stone in new_stones:
                    if new_stone in new_track:
                        new_track[new_stone] += current_track[current_stone]
                    else:
                        new_track[new_stone] = current_track[current_stone]
            else:
                # If the stone does not split, update the new track
                if new_stones in new_track:
                    new_track[new_stones] += current_track[current_stone]
                else:
                    new_track[new_stones] = current_track[current_stone]

        # Update the current track for the next blink.
        current_track = new_track

    return current_track


def first_part(stones, times):
    number_stones = 0

    # For each stone, make the blinking process and sum up the results.
    for stone in stones:
        # Get the stone counts after blinks
        track = blink(int(stone), times)
        # Add the count of each stone type.
        number_stones += sum([i for _, i in track.items()])

    return number_stones


def test_blink():
    stone, times = 0, 7
    expected = {4: 4, 0: 3, 8: 3, 20: 1, 24: 1, 9: 1, 6: 1}
    assert blink(stone, times) == expected


def test_first_part():
    stones = [125, 17]
    times = 6
    assert first_part(stones, times) == 22


if __name__ == "__main__":
    stones = read_file("./day11/input")
    value = first_part(stones, 25)
    print(f"Number of stone after 25 blinks: {value}")

    value = first_part(stones, 75)
    print(f"Number of stone after 75 blinks: {value}")
