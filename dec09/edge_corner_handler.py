def check_corner(heightmap, row, col):
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
    if heightmap[row][col] < heightmap[row_factor][col] and heightmap[row][col] < heightmap[row][col_factor]:
        return heightmap[row][col]
    return None
