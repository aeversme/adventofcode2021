from input_handler import convert_input
from probe_handler import check_probe_trajectory
from range_handler import determine_xv_range

with open('target.txt') as t:
    target_raw = t.read()


def find_possible_velocities(data):
    target_area = convert_input(data)

    starting_xv_values = determine_xv_range(target_area)
    # print(f"Starting xv values: {starting_xv_values}")

    velocity_count = 0
    for xv in range(min(starting_xv_values), max(target_area[0]) + 1):
        for yv in range(min(target_area[1]), abs(min(target_area[1])) + 1):
            height = check_probe_trajectory(target_area, xv, yv)
            if height:
                velocity_count += 1
    return velocity_count


count = find_possible_velocities(target_raw)
print(f"Possible valid starting velocities: {count}")
