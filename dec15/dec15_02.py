from map_handler import create_chiton_cave, is_on_map, find_smallest_distance

with open('chiton.txt') as ch:
    chiton_raw = ch.readlines()

chiton_map = create_chiton_cave(chiton_raw)
