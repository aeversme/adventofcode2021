from input_handler import convert_input
from step_handler import perform_initialization_step

with open('reboot.txt') as r:
    reboot_raw = r.readlines()

reboot_sequence = convert_input(reboot_raw)
print(reboot_sequence[:4])


def create_cube_dict():
    cubes = {}
    for i in range(-50, 51):
        for j in range(-50, 51):
            for k in range(-50, 51):
                cubes[i, j, k] = 'off'
    return cubes


def is_initialization_step(step):
    is_step = False
    step_values_list = []
    for i in range(3):
        for j in range(2):
            step_values_list.append(step[1][i][j])
    if min(step_values_list) > -51 and max(step_values_list) < 51:
        is_step = True
    return is_step


def initialize_reactor():
    cube_dict = create_cube_dict()
    for step in reboot_sequence:
        for i in range(3):
            if is_initialization_step(step):
                cube_dict = perform_initialization_step(cube_dict, step)
    return cube_dict


def count_on_cubes(cube_dict):
    on_count = 0
    for _, value in cube_dict.items():
        if value == 'on':
            on_count += 1
    return on_count


reactor_cubes = initialize_reactor()
cubes_on = count_on_cubes(reactor_cubes)
print(f"{cubes_on} cubes are on")
