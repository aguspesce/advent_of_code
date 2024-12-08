from functools import cmp_to_key


def read_file(fname):
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


def is_valid_update(rules, update):
    for i in range(len(update) - 1):
        if update[i] not in rules:
            return False
        else:
            if update[i + 1] not in rules[update[i]]:
                return False
    return True


def first_part(rules, updates):
    value = 0
    for update in updates:
        if is_valid_update(rules, update):
            value += int(update[len(update) // 2])
    return value


def test_first_part():
    rules, updates = read_file("./day05/test_input.txt")
    assert first_part(rules, updates) == 143


# def test_second_part():
#     rules, updates = read_file("./day05/test_input.txt")
#     assert second_part(rules, updates) == 123


if __name__ == "__main__":
    filename = "day05/input.txt"
    rules, updates = read_file(filename)

    value = first_part(rules, updates)
    print(f"The middle page number from those correctly updates is: {value}")

    value = second_part(rules, updates)
