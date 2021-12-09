from input_handler import convert_input
from edge_corner_handler import check_corner, check_edge

with open('heightmap.txt') as h:
    heightmap_raw = h.readlines()

heightmap = convert_input(heightmap_raw)
# print(heightmap)
