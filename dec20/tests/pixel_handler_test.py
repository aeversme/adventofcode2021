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
    pixel_binary = construct_pixel_binary(2, 1, image, 0)

    assert len(pixel_binary) == 9
    assert pixel_binary == '100110001'


def test_convert_image():
    global algorithm, expanded_image
    new_trenchmap = convert_image(algorithm, expanded_image, 0)

    assert count_lit_pixels(new_trenchmap) == 24
    assert new_trenchmap[7] == '....####..#....'
