def add_one(grid):
    """
    Takes a grid (list of lists) of integers. Adds 1 to every integer in the grid. Returns the grid.
    """

    for row in grid:
        for i in range(len(row)):
            row[i] += 1
    return grid


def is_on_map(grid, row, col):
    """
    Takes a grid and two integer values. Determines if the the row or column values fall outside the index range of
    the grid; if so, returns False. Otherwise (if [row][column] is within the bounds of the grid), returns True.
    """

    rules = [row < 0, row > (len(grid) - 1), col < 0, col > (len(grid[0]) - 1)]
    if any(rules):
        return False
    return True


def flash_octopus(grid, row, col):
    """
    Takes a grid and two integers. Checks all adjacent grid locations, including diagonally. If the location is on
    the map, increments the value at that location by 1. Returns the grid.
    """

    for row_increment in range(-1, 2):
        for col_increment in range(-1, 2):
            if is_on_map(grid, row + row_increment, col + col_increment) and [row_increment, col_increment] != [0, 0]:
                grid[row + row_increment][col + col_increment] += 1
    return grid


def step(grid):
    grid_plus_energy = add_one(grid)
    flashed_grid = grid_plus_energy
    flashed_octopuses = []
    loop_counter = -1
    total_flashes = 0
    while loop_counter != 0:
        loop_counter = 0
        for row in range(len(grid_plus_energy)):
            for col in range(len(grid_plus_energy[0])):
                if grid_plus_energy[row][col] > 9 and [row, col] not in flashed_octopuses:
                    flashed_grid = flash_octopus(grid_plus_energy, row, col)
                    loop_counter += 1
                    total_flashes += 1
                    flashed_octopuses.append([row, col])
    for octopus in flashed_octopuses:
        flashed_grid[octopus[0]][octopus[1]] = 0
    return flashed_grid, total_flashes
