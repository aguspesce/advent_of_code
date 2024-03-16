def input_parser(fname):
    """Parser the input file as a 2D list"""
    with open(fname) as data:
        schematic = [list(line.strip()) for line in data]
    return schematic

def find_parts(schematic, nline, nele):
    """Find the part position around the symbol"""
    positions = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            new_line, new_ele = nline + i, nele + j
            if 0 <= new_line < len(schematic) and 0 <= new_ele < len(schematic[new_line]):
                element = schematic[new_line][new_ele]
                if element.isnumeric():
                    positions.append((new_line, new_ele))
    return positions

def find_number(schematic, position):
    """Find the number in a given position"""
    nline, nele = position
    start, end = nele, nele
    while start >= 0 and schematic[nline][start].isdigit():
        start -= 1
    while end < len(schematic[nline]) and schematic[nline][end].isdigit():
        end += 1
    number = "".join(schematic[nline][start + 1:end])
    if number:
        schematic[nline][start + 1:end] = ['.'] * (end - start - 1)
        return schematic, int(number)
    else:
        return schematic, 0

def first_part(schematic):
    part_numbers=[]
    for nline, line in enumerate(schematic):
        for nele, ele in enumerate(line):
            # Find symbol
            if not (ele.isnumeric() or ele=="."):
                print(nline, nele, ele)
                # Find position of the number around the symbol
                parts_positions = find_parts(schematic, nline, nele)
                # Find number on these positions
                for position in parts_positions:
                    # print(position)
                    schematic, number = find_number(schematic, position)
                    print(number)
                    if number!="":
                        part_numbers.append(int(number))
    return part_numbers

if __name__ == "__main__":
    # Read input file
    fname = "input.txt"
    schematic = input_parser(fname)
    numbers = first_part(schematic)
    print(sum(numbers))


