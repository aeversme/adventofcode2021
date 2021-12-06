from input_handler import convert_input

with open('lanternfish.txt') as file:
    fish = file.read()

fish_dict = convert_input(fish)


def fish_growth(dict_input):
    day = 0
    while day < 256:
        for i in range(8):
            dict_input[i].append(dict_input[i + 1][-1])
        dict_input[8].append(dict_input[0][-2])
        dict_input[6][-1] += dict_input[0][-2]
        day += 1
    fish_population = 0
    for key, value in fish_dict.items():
        print(key, value[-1])
        fish_population += value[-1]
    return day, fish_population


days, population = fish_growth(fish_dict)
print(f"Number of fish after {days} days: {population}")
