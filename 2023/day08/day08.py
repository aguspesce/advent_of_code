import re
import numpy as np


def parser_input(fname):
    """Return instructions and nones from the input file"""
    with open(fname) as f:
        f = f.read().split("\n")
    # Create a list with the instructions. Replace R for 1 and L for 0
    instuctions = f[0].replace("R", "1").replace("L", "0")
    instuctions = [int(i) for i in instuctions]
    # Create dictionary with the nodes
    nodes = {}
    for line in f[1:]:
        if line != "":
            key, node = line.split("=")
            nodes[key.strip()] = re.sub(r"[^\w]", " ", node).strip().split()
    return instuctions, nodes


def first_part(instructions, nodes):
    """Return the number of steps to go from 'AAA' to 'ZZZ' following the
    instructions"""
    n_steps = 0
    current_node = "AAA"
    while not current_node == "ZZZ":
        for ins in instructions:
            current_node = nodes[current_node][ins]
            n_steps += 1
    return n_steps


def second_part(instructions, nodes):
    number_steps = []
    # Look how many steps are necessary to go from a node that ends with A
    # to get to one ending in Z
    for item in nodes.keys():
        n_steps = 0
        if item.endswith("A"):
            current_node = item
            while current_node.endswith("Z") is False:
                for ins in instructions:
                    current_node = nodes[current_node][ins]
                    n_steps += 1
            number_steps.append(n_steps)
    # Find lower common multiple between all the number of steps
    lcm = 1
    for steps in number_steps:
        lcm = np.lcm(lcm, steps)
    return lcm


if __name__ == "__main__":
    # fname = "exp-data.txt"
    fname = "input.txt"
    instuctions, nodes = parser_input(fname)
    result = first_part(instuctions, nodes)
    print("The number of steps is: ", result)
    result2 = second_part(instuctions, nodes)
    print("The number of steps is: ", result2)
