from input_handler import convert_input

with open('dirac.txt') as d:
    start_raw = d.readlines()

starting_positions = convert_input(start_raw)
print(starting_positions)


def deterministic_die_roll(last_roll):
    roll = 0
    if last_roll is None or last_roll == 100:
        roll = 1
    else:
        roll = last_roll + 1
    return roll
