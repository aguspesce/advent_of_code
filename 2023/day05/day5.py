def calculate_location(origin_destination_item, number):
    """Return the new position for number according to the map dictionary"""
    for item in origin_destination_item:
        dest_start, source_start, length = item
        # Check if the number is in the source
        if number in range(source_start, source_start + length):
            # Obtain the index in the source
            index_source = range(source_start, source_start + length).index(number)
            # Found the related number in destination
            number_dest = range(dest_start, dest_start + length)[index_source]
            return number_dest
    return number


def read_input(fname):
    """Return seeds as a list and the map as a dictionary"""
    origen_destination = {}
    current_key = None
    with open(fname) as f:
        data = f.read().split("\n")
        seeds = [int(seed) for seed in data[0].split(":")[1].split()]
        for item in data[1:]:
            if ":" in item:
                current_key = item.split(":")[0].strip().lower()
                origen_destination[current_key] = []
            elif item and current_key:
                values = list(map(int, item.split()))
                origen_destination[current_key].append(values)
    return seeds, origen_destination


def first_part(seeds, origin_destination):
    """Return the lower location for a list of seeds according to th map
    dictionary"""
    locations = []
    for seed in seeds:
        for item in origin_destination:
            seed = calculate_location(origin_destination[item], seed)
        locations.append(seed)
    return min(locations)


if __name__ == "__main__":
    # Read input file
    # fname = "exp-data.txt"
    fname = "input.txt"
    seeds, origin_destination = read_input(fname)
    location = first_part(seeds, origin_destination)
    print("The lowest location number is: ", location)
    # total_copies = second_part(cards_list)
    # print("Total of scratchcards: ", total_copies)
