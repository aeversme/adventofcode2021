from input_handler import convert_input
import step_handler as sh

with open('test-octopus.txt') as o:
    octo_raw = o.readlines()

octopus = convert_input(octo_raw)
# print(octopus)

octoflash = sh.step(octopus)
