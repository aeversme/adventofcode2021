# Advent of Code 2021
# December 01

with open('depth.txt', 'r') as depth:
    depths_list = depth.readlines()

depths_int = list(map(int, depths_list))


def depth_increase():
    increases = 0
    for i in range(1, len(depths_int)):
        if depths_int[i] > depths_int[i - 1]:
            increases += 1
    return increases


print(depth_increase())


def sliding_window():
    window_increases = 0
    for i in range(len(depths_int) - 3):
        first_window = depths_int[i] + depths_int[i + 1] + depths_int[i + 2]
        second_window = depths_int[i + 1] + depths_int[i + 2] + depths_int[i + 3]
        if second_window > first_window:
            window_increases += 1
    return window_increases


print(sliding_window())
