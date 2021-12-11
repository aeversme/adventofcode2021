from input_handler import convert_input
import step_handler as sh

with open('octopus.txt') as o:
    octo_raw = o.readlines()


def dumbo_octopuses(grid):
    octopus = convert_input(grid)

    step_counter = 0
    flashes = 0
    while flashes != 100:
        octoflash, step_flashes = sh.step(octopus)
        flashes = step_flashes
        step_counter += 1
    return step_counter


steps = dumbo_octopuses(octo_raw)
print(f"It took {steps} steps for the flashes to synchronize the first time.")
