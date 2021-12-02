# forward
# down increases depth
# up decreases depth

with open('movements.txt') as move:
    movements = move.readlines()

move_split = [i.split() for i in movements]


def final_position():
    horizontal_position = 0
    depth = 0
    for i in range(len(move_split)):
        if move_split[i][0] == "forward":
            horizontal_position += int(move_split[i][1])
        elif move_split[i][0] == "down":
            depth += int(move_split[i][1])
        elif move_split[i][0] == "up":
            depth -= int(move_split[i][1])
        else:
            continue
    return horizontal_position, depth


horizontal, vertical = final_position()
print(f"Part 1: horizontal times vertical = {horizontal * vertical}")
