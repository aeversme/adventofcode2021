basin_size = 0
tracked_coordinates = []


def is_on_map(heightmap, row, col):
    """
    Takes a heightmap and two integer values. Determines if the the row or column values fall outside the index
    range of the map; if so, returns False. Otherwise (if [row][column] is within the bounds of the map), returns True.
    """

    rules = [row < 0, row > (len(heightmap) - 1), col < 0, col > (len(heightmap[0]) - 1)]
    if any(rules):
        return False
    return True


def is_previous_coord(previous_list, row, col):
    """
    Takes a list and two integer values. Determines if [row, col] is in the list; if so, returns True. Otherwise,
    returns False.
    """

    for i in previous_list:
        if i == [row, col]:
            return True
    return False


def discover_basin(heightmap, row, col, is_low_point=False):
    """
    Takes a heightmap, two integer values, and a boolean (default = False). If the boolean argument is_low_point is
    passed in as True (an outside call of the function), sets starting values for basin size and a list of
    tracked coordinates.

    For the four cardinal directions (up, down, left, right) relative to the given input coordinates [row][column] on
    the heightmap, determines if: the index of the next coordinates in that direction is within the bounds of the
    map; if the next coordinates have not already been tracked as part of the basin; and if the value at the next
    coordinates is not equal to '9'.

    If all three conditions are met, adds one to basin size, adds the next coordinates to the list of tracked
    coordinates, and calls itself recursively with the next coordinates. If any condition is not met,
    the loop continues with the next direction. If all directions have been checked, moves back down the stack and
    continues evaluating directions for the previous coordinates.

    Returns basin size.
    """

    global basin_size, tracked_coordinates
    if is_low_point:
        basin_size = 1
        tracked_coordinates = [[row, col]]
    directions = [[row - 1, col], [row + 1, col], [row, col - 1], [row, col + 1]]
    for direction in directions:
        r = direction[0]
        c = direction[1]
        if is_on_map(heightmap, r, c) and not is_previous_coord(tracked_coordinates, r, c) and not \
                heightmap[r][c] == '9':
            basin_size += 1
            tracked_coordinates.append([r, c])
            discover_basin(heightmap, r, c)
    return basin_size
