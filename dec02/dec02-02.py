# aim
# down x increases aim by x
# up x decreases aim by x
# forward x increases horizontal & increases depth by aim * x

with open('movements.txt') as move:
    movements = move.readlines()

move_split = [i.split() for i in movements]


def final_position():
    horizontal_position = 0
    depth = 0
    aim = 0
    for i in range(len(move_split)):
        movement = int(move_split[i][1])
        if move_split[i][0] == "forward":
            horizontal_position += movement
            depth += movement * aim
        elif move_split[i][0] == "down":
            aim += movement
        elif move_split[i][0] == "up":
            aim -= movement
        else:
            continue
    return horizontal_position, depth


horizontal, vertical = final_position()
print(f"Part 2: horizontal times vertical = {horizontal * vertical}")
