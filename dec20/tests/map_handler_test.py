from ..map_handler import expand_trenchmap
from ..input_handler import convert_input


def setup():
    with open('test-trenchmap.txt') as t:
        trenchmap_raw = t.readlines()
    image_algorithm, trenchmap = convert_input(trenchmap_raw)
    return image_algorithm, trenchmap


def test_expand_trenchmap():
    _, trenchmap = setup()
    expanded_trenchmap = expand_trenchmap(trenchmap)

    assert len(expanded_trenchmap) == len(trenchmap) + 10
    assert len(expanded_trenchmap[2]) == len(trenchmap[2]) + 10
    assert expanded_trenchmap[9] == '.......###.....'
