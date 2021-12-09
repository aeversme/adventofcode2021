def is_on_map(heightmap, row, col):
    rules = [row < 0, row > (len(heightmap) - 1), col < 0, col > (len(heightmap[0]) - 1)]
    if any(rules):
        return False
    return True


def is_previous_coord(previous_list, row, col):
    for i in previous_list:
        if i[0] == row and i[1] == col:
            return True
    return False


def discover_basin():
    return
