def read_file(fname):
    reports = []
    with open(fname) as file:
        for line in file:
            line = line.strip().split(" ")
            reports.append(line)
    return reports


def is_sorted(nums):
    """Check if the report is sorted"""
    # Check if the list is increasing
    increasing = all(int(nums[i]) <= int(nums[i + 1]) for i in range(len(nums) - 1))
    # Check if the list is decreasing
    decreasing = all(int(nums[i]) >= int(nums[i + 1]) for i in range(len(nums) - 1))
    return increasing or decreasing


def check_diff(report):
    """Check id the differences are 1, 2 or 3"""
    for i in range(len(report) - 1):
        diff = abs(int(report[i + 1]) - int(report[i]))
        if diff not in [1, 2, 3]:
            return False

    return True


def first_part(reports):
    """Find how many safe reports are"""
    value = 0
    for report in reports:
        if is_sorted(report):
            if check_diff(report):
                value += 1
    return value


def second_part(reports):
    """Find how many safe reports are"""
    value = 0
    for report in reports:
        if is_sorted(report) and check_diff(report):
            value += 1
        else:
            for i in range(len(report)):
                new_report = report.copy()
                del new_report[i]
                if is_sorted(new_report):
                    if check_diff(new_report):
                        value += 1
                        break
    return value


def test_first_part():
    reports = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]
    assert first_part(reports) == 2


def test_second_part():
    reports = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]
    assert second_part(reports) == 4


if __name__ == "__main__":
    filename = "day02/input.txt"
    reports = read_file(filename)

    value = first_part(reports)
    print(f"The number of safe reports is: {value}")

    value = second_part(reports)
    print(f"The number of safe reports is: {value}")
