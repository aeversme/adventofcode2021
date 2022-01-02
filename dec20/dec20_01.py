from input_handler import convert_input
from map_handler import expand_trenchmap
from pixel_handler import count_lit_pixels, convert_image

with open('test-trenchmap.txt') as t:
    trenchmap_raw = t.readlines()


def map_trench_floor(data):
    image_algorithm, trenchmap = convert_input(data)
    print(image_algorithm)
    print(f"The image enhancement algorithm is {len(image_algorithm)} characters long.\n")

    expanded_trenchmap = expand_trenchmap(trenchmap)
    for line in expanded_trenchmap:
        print(line)

    iteration_count = 0
    new_trenchmap = convert_image(image_algorithm, expanded_trenchmap)
    iteration_count += 1
    print("\nEnhancing image...\n")
    for line in new_trenchmap:
        print(line)

    new_trenchmap = convert_image(image_algorithm, new_trenchmap)
    iteration_count += 1
    print("\nEnhancing image...\n")
    for line in new_trenchmap:
        print(line)

    lit_pixels = count_lit_pixels(new_trenchmap)
    return lit_pixels, iteration_count


lit_pixel_count, iterations = map_trench_floor(trenchmap_raw)
print(f"\nThere are {lit_pixel_count} pixels lit after {iterations} iterations.")
