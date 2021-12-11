"""
TODO:
in each step:

[done] increment each octopus by 1

any octopus with energy > 9 'flashes.' all adjacent octopuses get +1 energy, including diagonal. checks needed: out
of bounds, and keep track of flashing octopus coordinates. no octopus can flash more than once per step. use a while
loop and a flash counter so that while number of flashes != 0, loop through and check for energy > 9

loop through list of coordinates of octopuses that flashed during that step, and reset energy at those coordinates to
zero
"""


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


# TODO: bug in this function, not looking at all adjacent locations
def flash_octopus(grid, row, col):
    flashing_octopus = grid[row][col]
    print(f"Flash octopus with energy {flashing_octopus} at [{row}, {col}]")
    for row_incr in range(-1, 2):
        for col_incr in range(-1, 2):
            adjacent_octopus = grid[row + row_incr][col + col_incr]
            if is_on_map(grid, row + row_incr, col + col_incr) and adjacent_octopus != flashing_octopus:
                print(f"Adding one to {adjacent_octopus} at [{[row + row_incr]}, {[col + col_incr]}]")
                adjacent_octopus += 1
    return


def step(grid):
    grid_plus_energy = add_one(grid)
    print(grid_plus_energy)
    for row in range(len(grid_plus_energy)):
        for col in range(len(grid_plus_energy[0])):
            if grid_plus_energy[row][col] > 9:
                flash_octopus(grid_plus_energy, row, col)
    return grid
