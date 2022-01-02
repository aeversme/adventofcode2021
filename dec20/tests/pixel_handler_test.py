from ..pixel_handler import count_lit_pixels, convert_image, construct_pixel_binary, count_top_bottom_dark_lines
from ..map_handler import expand_trenchmap
from ..input_handler import convert_input


def setup():
    with open('test-trenchmap.txt') as t:
        trenchmap_raw = t.readlines()
    image_algorithm, trenchmap = convert_input(trenchmap_raw)
    return image_algorithm, trenchmap


def test_count_lit_pixels():
    _, trenchmap = setup()
    lit_pixels = count_lit_pixels(trenchmap)

    assert lit_pixels == 10


def test_construct_pixel_binary():
    _, trenchmap = setup()
    pixel_binary = construct_pixel_binary(2, 1, trenchmap)

    assert len(pixel_binary) == 9
    assert pixel_binary == '100110001'


def test_count_dark_lines():
    _, trenchmap = setup()
    expanded_trenchmap = expand_trenchmap(trenchmap)
    top_line_count, bottom_line_count = count_top_bottom_dark_lines(expanded_trenchmap)

    assert top_line_count == 5
    assert bottom_line_count == 5


def test_convert_image():
    image_algorithm, trenchmap = setup()
    expanded_trenchmap = expand_trenchmap(trenchmap)
    new_trenchmap = convert_image(image_algorithm, expanded_trenchmap)

    assert count_lit_pixels(new_trenchmap) == 24
    assert new_trenchmap[7] == '....####..#....'
