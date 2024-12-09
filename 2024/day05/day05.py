def read_file(fname):
    """Reads the input file and parses it into rules and updates."""
    rules, updates = {}, []
    with open(fname) as file:
        for line in file:
            line = line.strip()
            if "|" in line:
                line = line.split("|")
                if line[0] not in rules:
                    rules[line[0]] = [line[1]]
                else:
                    rules[line[0]].append(line[1])
            else:
                updates.append(line.split(","))
    return rules, updates[1:]


def a_lower_than_b(a, b, rules):
    """Checks if 'a' is less than 'b' according to the rules."""
    if a not in rules:
        return False
    return b in rules[a]


def quick_sort(rules, update, low, high):
    """Sorts the 'update' list using quicksort algorithm, based on the ordering rules."""
    if high - low <= 0 or low < 0:
        return
    pivote = update[high]
    i = low
    for j in range(low, high):
        if a_lower_than_b(update[j], pivote, rules):
            update[i], update[j] = update[j], update[i]
            i += 1
    update[i], update[high] = update[high], update[i]

    quick_sort(rules, update, low, i - 1)
    quick_sort(rules, update, i + 1, high)


def is_sorted(update, rules):
    """Checks if the 'update' list is sorted according to the rules."""
    for i in range(len(update) - 1):
        if not a_lower_than_b(update[i], update[i + 1], rules):
            return False
    return True


def second_part(rules, updates):
    value = 0
    for update in updates:
        if not is_sorted(update, rules):
            quick_sort(rules, update, 0, len(update) - 1)
            value += int(update[len(update) // 2])
            assert is_sorted(update, rules)
    return value


def first_part(rules, updates):
    value = 0
    for update in updates:
        if is_sorted(update, rules):
            value += int(update[len(update) // 2])
    return value


def test_first_part():
    rules, updates = read_file("./day05/test_input.txt")
    assert first_part(rules, updates) == 143


def test_quick_sort():
    rules = {0: [1, 2, 3], 1: [2, 3], 2: [3]}
    update = [3, 1, 2, 0]
    quick_sort(rules, update, 0, 3)
    assert update == [0, 1, 2, 3]
    update = [1, 3, 2, 0]
    quick_sort(rules, update, 0, 3)
    assert update == [0, 1, 2, 3]


def test_second_part():
    rules, updates = read_file("./day05/test_input.txt")
    assert second_part(rules, updates) == 123


if __name__ == "__main__":
    filename = "day05/input.txt"
    rules, updates = read_file(filename)

    value = first_part(rules, updates)
    print(f"The middle page number from those correctly updates is: {value}")

    value = second_part(rules, updates)
    print(f"The middle page number from those incorrectly updates is: {value}")
