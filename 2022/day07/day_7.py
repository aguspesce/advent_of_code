"""
Script to solve the 7th Day
"""


def first_part(fname):
    """
    Solve the first part.

    Return a int with the total size of the directories with a
    size of at most 100000
    """
    # Load the file
    commands = _read_input(fname)
    # Generate a dictionary with the directories paths and sizes
    dirs = _process_comand(commands)
    # Calculate the total size
    total = 0
    for dir in dirs:
        # Only use the directories with a size of at most 100000
        if dirs[dir] < 100000:
            total += dirs[dir]
    return total


def second_part(fname):
    """
    Solve the second part.

    Return the smallest directory that would free up enough space
    """
    # Load the file
    commands = _read_input(fname)
    # Generate a dictionary with the directories paths and sizes
    dirs = _process_comand(commands)
    # Space required - space unused (total space - space used)
    limit = 30000000 - (70000000 - dirs["/home"])
    # Find the smallest directory to remove
    dirs_to_delete = []
    for dir in dirs:
        if dirs[dir] >= limit:
            dirs_to_delete.append(dirs[dir])
    smallest_dir = min(dirs_to_delete)
    return smallest_dir


def _read_input(fname):
    """
    Read the file.

    Return a list.
    """
    with open(fname, "r") as f:
        commands = f.readlines()
    return commands


def _process_comand(commands):
    """
    Process the command and return a dictionary with the path to the different
    directories and its size
    """
    # Initialize a dictionary to save the directories and size
    dirs = {"/home": 0}
    path = "/home"
    # Process every commands
    for command in commands:
        command = command.strip()
        # Commands start with $
        if command[0] == "$":
            # For "ls", do nothing
            if command[2:4] == "ls":
                pass
            # For "cd", update the path and add it to dirs
            elif command[2:4] == "cd":
                # For "/", go "home"
                if command[5:6] == "/":
                    path = "/home"
                # For "..", go back to the last path
                elif command[5:7] == "..":
                    path = path[0 : path.rfind("/")]
                # For a directory, change path
                else:
                    # Get the directory name
                    dir_name = command[5:]
                    # Add to the path
                    path = path + f"/{dir_name}"
                    # Update dirs dictionary
                    dirs.update({path: 0})

        # When list directories, do nothing
        elif command[0:3] == "dir":
            pass
        # Read the file size and calculate the directory size
        else:
            # Get the file size
            file_size = int(command[: command.find(" ")])
            dir = path
            # Update the size for the parent directory
            for i in range(path.count("/")):
                dirs[dir] += file_size
                dir = dir[: dir.rfind("/")]
    return dirs


def _test_command():
    """
    Check _process_command function
    """
    expected = {
        "/home": 48381165,
        "/home/a": 94853,
        "/home/a/e": 584,
        "/home/d": 24933642,
    }
    commands = [
        "$ cd /\n",
        "$ ls\n",
        "dir a\n",
        "14848514 b.txt\n",
        "8504156 c.dat\n",
        "dir d\n",
        "$ cd a\n",
        "$ ls\n",
        "dir e\n",
        "29116 f\n",
        "2557 g\n",
        "62596 h.lst\n",
        "$ cd e\n",
        "$ ls\n",
        "584 i\n",
        "$ cd ..\n",
        "$ cd ..\n",
        "$ cd d\n",
        "$ ls\n",
        "4060174 j\n",
        "8033020 d.log\n",
        "5626152 d.ext\n",
        "7214296 k\n",
    ]
    assert expected == _process_comand(commands)


def test_first_part():
    """
    Check the first_part function
    """
    expected = 95437
    total = first_part("test_input")
    assert total == expected


def test_second_part():
    """
    Check the second_part function
    """
    expected = 24933642
    smallest = second_part("test_input")
    assert smallest == expected


if __name__ == "__main__":
    # Solve first part
    size_1 = first_part("input")

    # Solve second part
    smallest_dir = second_part("input")
    print(
        "Answers:",
        "\n",
        "- First part: ",
        f"{size_1}",
        "\n",
        "- Second part: ",
        f"{smallest_dir}",
    )
