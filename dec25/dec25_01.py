from input_handler import convert_input
from movement_handler import movement_step

with open('slugs.txt') as s:
    slugs_raw = s.readlines()

slug_map = convert_input(slugs_raw)
print("Original slug_map:")
for line in slug_map:
    print(line)

moves = -1
steps = 0

while moves != 0:
    slug_map, moves = movement_step(slug_map)
    steps += 1

print("\nNew slug_map:")
for line in slug_map:
    print(line)

print(f"\nSteps: {steps}")
