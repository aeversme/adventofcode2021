from input_handler import convert_input
import step_handler as sh

with open('octopus.txt') as o:
    octo_raw = o.readlines()


def dumbo_octopuses(grid):
    octopus = convert_input(grid)

    total_flashes = 0
    for step in range(100):
        octoflash, step_flashes = sh.step(octopus)
        total_flashes += step_flashes
    return total_flashes


flashes = dumbo_octopuses(octo_raw)
print(f"There have been {flashes} octopus flashes.")