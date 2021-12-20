from ..operation_handler import add_numbers, split_number, explode_pair, calculate_magnitude


def test_add_numbers():
    num1 = [1, 2]
    num2 = [[3, 4], 5]
    result = add_numbers(num1, num2)

    assert result == [[1, 2], [[3, 4], 5]]
    assert type(result) == list
    assert len(result) == 2


def test_split_number():
    num1 = [1, 13]
    num2 = [[1, 9], [12, 5]]
    num3 = [[[[4, 0], [5, 4]], [[7, 7], [6, 0]]], [[8, 9], [[11, 9], [11, 0]]]]

    assert split_number(num1, '13') == [1, [6, 7]]
    assert split_number(num2, '12') == [[1, 9], [[6, 6], 5]]
    assert split_number(num3, '11') == [[[[4, 0], [5, 4]], [[7, 7], [6, 0]]], [[8, 9], [[[5, 6], 9], [11, 0]]]]


def test_explode_pair():
    num1 = [[6, [5, [4, [3, 2]]]], 1]
    num2 = [7, [6, [5, [4, [3, 2]]]]]
    num3 = [[[[[9, 8], 1], 2], 3], 4]
    num4 = [[[[4, 0], [5, 4]], [[7, 7], [0, [6, 7]]]], [10, [[11, 9], [11, 0]]]]
    num5 = [[[0, [6, 6]], [0, [6, 7]]], [[[7, [6, 7]], [0, 6]], [[7, 8], [16, 0]]]]
    num6 = [[[[12, 12], [6, 14]], [[15, 0], [17, [8, 1]]]], [2, 9]]

    assert explode_pair(num1, '[3, 2]', 13) == [[6, [5, [7, 0]]], 3]
    assert explode_pair(num2, '[3, 2]', 16) == [7, [6, [5, [7, 0]]]]
    assert explode_pair(num3, '[9, 8]', 4) == [[[[0, 9], 2], 3], 4]
    assert explode_pair(num4, '[6, 7]', 33) == [[[[4, 0], [5, 4]], [[7, 7], [6, 0]]], [17, [[11, 9], [11, 0]]]]
    assert explode_pair(num5, '[6, 7]', 35) == [[[0, [6, 6]], [0, [6, 7]]], [[[13, 0], [7, 6]], [[7, 8], [16, 0]]]]
    assert explode_pair(num6, '[8, 1]', 38) == [[[[12, 12], [6, 14]], [[15, 0], [25, 0]]], [3, 9]]


def test_calculate_magnitude():
    num1 = [9, 1]
    num2 = [1, 9]
    num3 = [[9, 1], [1, 9]]
    num4 = [[1, 2], [[3, 4], 5]]
    num5 = [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]
    num6 = [[[[1, 1], [2, 2]], [3, 3]], [4, 4]]
    num7 = [[[[3, 0], [5, 3]], [4, 4]], [5, 5]]
    num8 = [[[[5, 0], [7, 4]], [5, 5]], [6, 6]]
    num9 = [[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]]

    assert calculate_magnitude(num1) == 29
    assert calculate_magnitude(num2) == 21
    assert calculate_magnitude(num3) == 129
    assert calculate_magnitude(num4) == 143
    assert calculate_magnitude(num5) == 1384
    assert calculate_magnitude(num6) == 445
    assert calculate_magnitude(num7) == 791
    assert calculate_magnitude(num8) == 1137
    assert calculate_magnitude(num9) == 3488
