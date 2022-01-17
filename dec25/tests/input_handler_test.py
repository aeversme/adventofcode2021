from ..input_handler import convert_input


def setup():
    with open('test_slugs.txt') as s:
        slugs_raw = s.readlines()
    return slugs_raw


def test_convert_input():
    slugs_raw = setup()
    slug_map = convert_input(slugs_raw)

    newline_count = 0
    for line in slug_map:
        if line.count('\n') > 0:
            newline_count += 1

    assert len(slug_map) == 9
    assert slug_map[5] == '>.>>..v...'
    assert newline_count == 0
