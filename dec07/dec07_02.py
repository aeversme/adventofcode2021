from input_handler import convert_input

with open('crabs.txt') as c:
    crabs_input = c.read()

crabs = convert_input(crabs_input)

test_crabs = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def triangular_sum(step):
    return ((step ** 2) + step) // 2


def fuel_consumption(input_list):
    fuel_by_position = []
    for location in range(min(input_list), max(input_list) + 1):
        fuel = 0
        for crab_position in input_list:
            step = abs(crab_position - location)
            fuel += triangular_sum(step)
        fuel_by_position.append(fuel)
    return fuel_by_position


fuel_use = fuel_consumption(crabs)
least_fuel = min(fuel_use)
least_fuel_position = fuel_use.index(min(fuel_use))
print(f"Position with least fuel use: {least_fuel_position}, using {least_fuel} fuel.")
