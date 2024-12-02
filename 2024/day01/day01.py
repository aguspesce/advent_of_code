def open_file(filename):
    # Read file and separate in left and right list
    list_left, list_right = [], []
    with open(filename, "r") as file:
        for line in file:
            values = line.split()
            list_left.append(int(values[0]))
            list_right.append(int(values[1]))
    return list_left, list_right


def first_part(list_left, list_right):
    # Sort the element of the lists
    list_left = sorted(list_left)
    list_right = sorted(list_right)

    # Calculate the distance
    distance = sum(abs(left - right) for left, right in zip(list_left, list_right))

    return distance


def second_part(list_left, list_right):
    # Sort the element of the lists
    list_left = sorted(list_left)
    list_right = sorted(list_right)

    # Count number of aparitions
    score = sum(list_right.count(left) * left for left in list_left)

    return score


def test_first_part():
    list_left = [3, 4, 2, 1, 3, 3]
    list_right = [4, 3, 5, 3, 9, 3]
    distance = first_part(list_left, list_right)
    assert distance == 11


def test_second_part():
    list_left = [3, 4, 2, 1, 3, 3]
    list_right = [4, 3, 5, 3, 9, 3]
    score = second_part(list_left, list_right)
    assert score == 31


if __name__ == "__main__":
    filename = "./input_1.txt"
    list_left, list_right = open_file(filename)

    distance = first_part(list_left, list_right)
    print(f"Total distance between the lists is: {distance}")

    score = second_part(list_left, list_right)
    print(f"The similar score is: {score}")
