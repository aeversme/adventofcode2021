from ..input_handler import convert_input


def setup():
    with open('test-trenchmap.txt') as t:
        trenchmap_raw = t.readlines()
    return trenchmap_raw


def test_convert_input():
    trenchmap_raw = setup()
    image_algorithm, trenchmap = convert_input(trenchmap_raw)

    assert len(image_algorithm) == 512
    assert image_algorithm[:7] == '..#.#..'
    assert len(trenchmap) == 5
    assert trenchmap[2] == '##..#'
