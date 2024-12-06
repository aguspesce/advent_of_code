def read_file(fname):
    with open(fname) as file:
        return file.readlines()


data = [
    "MMAMXXSSMM",
    "MSMSMXMAAX",
    "MAXAAASXMM",
    "SMSMSMMAMX",
    "XXXAAMSMMA",
    "XMMSMXAAXX",
    "MSAMXXSSMM",
    "AMASAAXAMA",
    "SSMMMMSAMS",
    "MAMXMASAMX",
]


def first_part(data):
    nrow, ncol = len(data), len(data[0])
    value = 0

    # Add horizontal lines
    lines = data.copy()

    # Add the vertical lines
    for i in range(ncol):
        lines.extend(["".join([row[i] for row in data])])
    value += sum([line.count("XMAS") for line in lines])
    value += sum([line.count("SAMX") for line in lines])

    # left-top to right-bottom
    diagonals = {}
    for index in range(ncol):
        diagonals[index] = "".join([data[i][i + index] for i in range(nrow - index)])
        diagonals[-index] = "".join([data[i + index][i] for i in range(nrow - index)])

    value += sum([diagonals[line].count("XMAS") for line in diagonals])
    value += sum([diagonals[line].count("SAMX") for line in diagonals])
    #
    # 0 09 18 27 ...90  i 9-i      0 9
    # 1 08 17 26 ...80  i 9-i-1  0 8
    # 2 07 16 25    70  i 9-i-2  0 7
    #
    # 0  09 18 27 ... 90  i   9-i  0 9
    # -1 19 28 37 ... 91  i+1 9-i  0 8
    # -2 29 38 47 ... 92  i+2 9-i  0 7

    diagonals_2 = {}
    for index in range(ncol):
        diagonals_2[index] = "".join(
            [data[i][nrow - 1 - index - i] for i in range(nrow - index)]
        )
        diagonals_2[-index] = "".join(
            [data[i + index][nrow - 1 - i] for i in range(nrow - index)]
        )
    value += sum([diagonals_2[line].count("XMAS") for line in diagonals_2])
    value += sum([diagonals_2[line].count("SAMX") for line in diagonals_2])
    return value


if __name__ == "__main__":
    filename = "day04/input.txt"
    data = read_file(filename)
    print(data)
    value = first_part(data)
    print(value)
