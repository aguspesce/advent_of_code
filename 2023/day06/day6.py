def read_input(fname):
    with open(fname) as f:
        for line in f:
            if line.startswith("Time"):
                times = line.split(":")[1]
                times = times.strip().split()
            else:
                distances_race = line.split(":")[1]
                distances_race = distances_race.strip().split()
    return times, distances_race


def get_win_options(time, distance_race):
    min_time_hold = 0
    distance = 0
    while distance <= distance_race:
        min_time_hold += 1
        distance = min_time_hold * (time - min_time_hold)
    max_time_hold = time - min_time_hold
    win_options = len(range(min_time_hold, max_time_hold + 1))
    return win_options


def first_part(times, distances_race):
    times = [int(ele) for ele in times]
    distances_race = [int(ele) for ele in distances_race]

    win_options = 1
    for time, distance in zip(times, distances_race):
        win_options *= get_win_options(time, distance)
    return win_options


def second_part(times, distances_race):
    time = int("".join(times))
    distance = int("".join(distances_race))

    return get_win_options(time, distance)


if __name__ == "__main__":
    # Read input file
    # fname = "exp-data.txt"
    fname = "input.txt"
    times, distances_race = read_input(fname)
    result = first_part(times, distances_race)
    print("The  multiplication of the number of way to win is: ", result)
    result2 = second_part(times, distances_race)
    print("The  multiplication of the number of way to win is: ", result2)
    # total_copies = second_part(cards_list)
    # print("Total of scratchcards: ", total_copies)
    # print("Total of scratchcards: ", total_copies)
