"""
Script to solve the 5th Day
"""


def first_part(fname):
    """
    Return a int whit the number of total overlaps
    """
    # Read the file
    lines = _read_input(fname)
    score = 0
    # Evaluate the overlap and add a point to the score
    for line in lines:
        line = line.strip().split(",")
        elf_1, elf_2 = line[0].split("-"), line[1].split("-")
        if _overlap(elf_1, elf_2):
            score += 1
    return score


def second_part(fname):
    # Read the file
    lines = _read_input(fname)
    score = 0
    # Evaluate the overlap and add a point to the score
    for line in lines:
        line = line.strip().split(",")
        elf_1, elf_2 = line[0].split("-"), line[1].split("-")
        if _partial_overlap(elf_1, elf_2):
            score += 1
    return score


def _partial_overlap(elf_1, elf_2):
    # Convert str to int
    elf_1 = [int(element) for element in elf_1]
    elf_2 = [int(element) for element in elf_2]
    overlap = (elf_1[0] <= elf_2[0] <= elf_1[1]) or (elf_2[0] <= elf_1[0] <= elf_2[1])
    return overlap


def _overlap(elf_1, elf_2):
    """
    Return a True/False after evaluate a condition to find overlap
    """
    # Convert str to int
    elf_1 = [int(element) for element in elf_1]
    elf_2 = [int(element) for element in elf_2]
    overlap = (elf_1[0] >= elf_2[0] and elf_1[1] <= elf_2[1]) or (
        elf_2[0] >= elf_1[0] and elf_2[1] <= elf_1[1]
    )
    return overlap


def _read_input(fname):
    """
    Read the file.

    Return a list with the assignment pairs.
    """
    with open(fname, "r") as f:
        return f.readlines()


if __name__ == "__main__":
    # Solve first part
    solution = first_part("input")

    # Solve second part
    solution_2 = second_part("input")

    print(
        "Answerers:",
        "\n",
        "- First part: ",
        f"{solution}",
        "\n",
        "- Second part: ",
        f"{solution_2}",
    )
