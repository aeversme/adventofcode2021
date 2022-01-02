from ..input_handler import convert_input
from ..map_handler import expand_trenchmap
from ..pixel_handler import *


def setup():
    with open('test-trenchmap.txt') as t:
        trenchmap_raw = t.readlines()
    image_algorithm, trenchmap = convert_input(trenchmap_raw)
    return image_algorithm, trenchmap


algorithm, image = setup()
expanded_image = expand_trenchmap(image)


def test_count_lit_pixels():
    global image
    lit_pixels = count_lit_pixels(image)

    assert lit_pixels == 10


def test_construct_pixel_binary():
    global image
    pixel_binary = construct_pixel_binary(2, 1, image)

    assert len(pixel_binary) == 9
    assert pixel_binary == '100110001'


def test_count_dark_lines():
    global expanded_image
    top_line_count, bottom_line_count = count_top_bottom_dark_lines(expanded_image)

    assert top_line_count == 5
    assert bottom_line_count == 5


def test_count_dark_pixels():
    row = '...#...#.#.###..#.##..'
    leading_dark_pixels, trailing_dark_pixels = count_start_end_dark_pixels(row)

    assert leading_dark_pixels == 3
    assert trailing_dark_pixels == 2


def test_convert_image():
    global algorithm, expanded_image
    new_trenchmap = convert_image(algorithm, expanded_image)

    assert count_lit_pixels(new_trenchmap) == 24
    assert new_trenchmap[7] == '....####..#....'
