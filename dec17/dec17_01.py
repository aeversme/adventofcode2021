from input_handler import convert_input
from probe_handler import check_probe_trajectory
from range_handler import determine_xv_range

with open('target.txt') as t:
    target_raw = t.read()


def find_highest_y(data):
    target_area = convert_input(data)

    starting_xv_values = determine_xv_range(target_area)
    # print(f"Starting xv values: {starting_xv_values}")

    heights = []
    for xv in starting_xv_values:
        for yv in range(abs(min(target_area[1])) + 1):
            height = check_probe_trajectory(target_area, xv, yv)
            if height:
                heights.append(max(height))
    return heights


heights_list = find_highest_y(target_raw)
print(f"Maximum y position: {max(heights_list)}")
