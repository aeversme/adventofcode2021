"""
TODO:
in each step:

increment each octopus by 1

any octopus with energy > 9 'flashes.' all adjacent octopuses get +1 energy, including diagonal. checks needed: out
of bounds, and keep track of flashing octopus coordinates. no octopus can flash more than once per step. use a while
loop and a flash counter so that while number of flashes != 0, loop through and check for energy > 9

loop through list of coordinates of octopuses that flashed during that step, and reset energy at those coordinates to
zero
"""