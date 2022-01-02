from ..pixel_handler import count_lit_pixels
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
