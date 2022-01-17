from ..movement_handler import movement_step, find_next_index
from ..input_handler import convert_input


def get_test_data():
    with open('test_slugs.txt') as s:
        slugs_raw = s.readlines()
    return convert_input(slugs_raw)


def test_find_next_index():
    index1 = [0, 4]
    index2 = [3, 7]

    assert find_next_index(index1, 8, 'east') == [0, 5]
    assert find_next_index(index2, 8, 'east') == [3, 0]


def test_movement_step():
    line1 = ['...>>>>>...']
    line2 = ['...>>>>.>..']
    slug_map = get_test_data()
    new_map = movement_step(slug_map)

    assert movement_step(line1) == line2
    assert movement_step(line2) == ['...>>>.>.>.']
    assert new_map[0] == '....>.>v.>'
    assert new_map[4] == '.>v.v...v.'
