# Advent of Code 2021
# December 05, part 2

from input_handler import convert_input, find_max_value
from line_plotter import check_line_type, plot_line
from plot_checker import count_overlaps

with open('vent_lines.txt') as v:
    vents = v.readlines()


def analyze_vents():
    vents_list = convert_input(vents)
    max_value = find_max_value(vents_list)
    plot = [[0] * (max_value + 1) for _ in range(max_value + 1)]
    for coordinates in vents_list:
        line_type = check_line_type(coordinates)
        if line_type is not None:
            plot_line(line_type, coordinates, plot)
    print(f"Number of vent overlaps: {count_overlaps(plot)}")
    return 0


analyze_vents()
