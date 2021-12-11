from input_handler import convert_input

with open('test-octopus.txt') as o:
    octo_raw = o.readlines()

octopus = convert_input(octo_raw)
print(octopus)
