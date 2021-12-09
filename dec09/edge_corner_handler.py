def check_corner(heightmap, row, col):
    """
    Takes a heightmap (a list of strings of numbers, each with the same length), a row number, and a column number.
    Checks whether the number at [row[column] is a corner of the heightmap. If so, returns the number at the
    [row][column] coordinate if it is lower than the two adjacent numbers (diagonals excluded).
    """

    row_max = len(heightmap) - 1
    col_max = len(heightmap[0]) - 1
    row_factor = 0
    col_factor = 0

    if row == 0 and col == 0:
        row_factor = row + 1
        col_factor = col + 1
    elif row == 0 and col == col_max:
        row_factor = row + 1
        col_factor = col - 1
    elif row == row_max and col == 0:
        row_factor = row - 1
        col_factor = col + 1
    elif row == row_max and col == col_max:
        row_factor = row - 1
        col_factor = col - 1
    if row_factor != 0 and col_factor != 0:
        if heightmap[row][col] < heightmap[row_factor][col] and heightmap[row][col] < heightmap[row][col_factor]:
            # print(f"corner at [{row}][{col}]: {heightmap[row][col]} is smaller than {heightmap[row_factor][col]} and "
            #       f"{heightmap[row][col_factor]}")
            return heightmap[row][col]
    return None


def check_edge(heightmap, row, col):
    """
    Takes a heightmap (a list of strings of numbers, each with the same length), a row number, and a column number.
    Checks whether the number at [r][column] is on an edge of the heightmap. If so, returns the number at the
    [row][column] coordinate if it is lower than the three adjacent numbers (diagonals excluded).
    """

    row_max = len(heightmap) - 1
    col_max = len(heightmap[0]) - 1
    col_check = 0
    row_check = 0
    row_factor = 0
    col_factor = 0

    # top edge except corners
    if row == 0 and col != 0 and col != col_max:
        col_check = 2
        row_factor = row + 1
    # bottom edge except corners
    elif row == row_max and col != 0 and col != col_max:
        col_check = 2
        row_factor = row - 1
    # left edge except corners
    elif col == 0 and row != 0 and row != row_max:
        row_check = 2
        col_factor = col + 1
    # right edge except corners
    elif col == col_max and row != 0 and row != row_max:
        row_check = 2
        col_factor = col - 1
    if col_check == 2:
        if heightmap[row][col] < heightmap[row][col - 1] and heightmap[row][col] < heightmap[row][col + 1] and \
                heightmap[row][col] < heightmap[row_factor][col]:
            # print(f"t/b edge at [{row}][{col}]: {heightmap[row][col]} is smaller than {heightmap[row][col - 1]}, "
            #       f"{heightmap[row][col + 1]}, and {heightmap[row_factor][col]}")
            return heightmap[row][col]
    if row_check == 2:
        if heightmap[row][col] < heightmap[row - 1][col] and heightmap[row][col] < heightmap[row + 1][col] and \
                heightmap[row][col] < heightmap[row][col_factor]:
            # print(f"l/r edge at [{row}][{col}]: {heightmap[row][col]} is smaller than {heightmap[row - 1][col]}, "
            #       f"{heightmap[row + 1][col]}, and {heightmap[row][col_factor]}")
            return heightmap[row][col]
    return None
