from input_handler import convert_input
from chiton_handler import Chiton
import numpy as np


def create_chiton_map(data):
    """
    Takes a list of strings. For each string in the list, creates a Chiton object for each numerical character in the
    string and appends it to a row list. After a string is fully processed, that row is appended to a list to create
    a two-dimensional list. Returns the two-dimensional list.
    """

    chiton_map = convert_input(data)

    chitons = []

    for r in range(len(chiton_map)):
        row = []
        for c in range(len(chiton_map[0])):
            row.append(Chiton(r, c, chiton_map[r][c]))
        chitons.append(row)

    chitons[0][0].distance = 0

    return chitons


def create_chiton_cave(data):
    chiton_strings = convert_input(data)
    wrap_dict = {
        10: 1,
        11: 2,
        12: 3,
        13: 4
    }

    # iterate map vertically
    cave_strings = chiton_strings.copy()
    for i in range(1, 5):
        for r in range(len(chiton_strings)):
            new_row = ''
            for c in range(len(chiton_strings[0])):
                new_num = int(cave_strings[r][c]) + i
                if new_num in wrap_dict.keys():
                    new_num = wrap_dict[new_num]
                new_row += str(new_num)
            cave_strings.append(new_row)

    # then iterate horizontally
    for r in range(len(cave_strings)):
        for i in range(1, 5):
            for c in range(len(chiton_strings[0])):
                new_num = int(cave_strings[r][c]) + i
                if new_num in wrap_dict.keys():
                    new_num = wrap_dict[new_num]
                cave_strings[r] += str(new_num)

    chitons = []

    for r in range(len(cave_strings)):
        row = []
        for c in range(len(cave_strings[0])):
            row.append(Chiton(r, c, cave_strings[r][c]))
        chitons.append(row)

    chitons[0][0].distance = 0

    return chitons


def is_on_map(chiton_map, row, col):
    """
    Takes a two-dimensional list and two integers. Determines if the the row or column values fall outside the index
    range of the map; if so, returns False. Otherwise (if [row][column] is within the bounds of the map), returns True.
    """

    row_max = len(chiton_map) - 1
    col_max = len(chiton_map[0]) - 1
    rules = [row < 0, row > row_max, col < 0, col > col_max]
    if any(rules):
        return False
    return True


def find_smallest_distance(chiton_map):
    """
    Takes a two-dimensional list. Returns the object with the smallest distance attribute.
    """

    current_node = None
    distance = np.inf
    for r in range(len(chiton_map)):
        for c in range(len(chiton_map[0])):
            if chiton_map[r][c].distance < distance and not chiton_map[r][c].visited:
                distance = chiton_map[r][c].distance
                current_node = chiton_map[r][c]
    return current_node
