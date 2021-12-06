from input_handler import convert_input

with open('testfish.txt') as file:
    fish = file.read()

fish_list = convert_input(fish)
day = 0


def fish_timer(input_list):
    global day
    while day < 80:
        print(f"Calculating day {day}")
        for i in range(len(input_list)):
            if input_list[i] == 0:
                input_list[i] = 6
                input_list.append(8)
            else:
                input_list[i] -= 1
        day += 1
    return input_list


final_list = fish_timer(fish_list)
print(f"After {day} days, there are {len(final_list)} lanternfish.")
