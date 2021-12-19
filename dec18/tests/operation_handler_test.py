from ..operation_handler import add_numbers, check_for_reduction, split_number, explode_pair


def test_add_numbers():
    num1 = [1, 2]
    num2 = [[3, 4], 5]
    result = add_numbers(num1, num2)

    assert result == [[1, 2], [[3, 4], 5]]
    assert type(result) == list
    assert len(result) == 2


def test_check_for_reduction():
    num1 = [[[[[9, 8], 1], 2], 3], 4]
    num2 = [[6, [5, [4, [3, 2]]]], 1]
    num3 = [[1, 9], [12, 5]]
    num4 = [[[[0, 7], 4], [15, [0, [1, 3]]]], [1, 1]]
    num5 = [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], 9]

    assert check_for_reduction(num1) == ('explode', [9, 8], -1)
    assert check_for_reduction(num2) == ('explode', [3, 2], -1)
    assert check_for_reduction(num3) == ('split', 12, -1)
    assert check_for_reduction(num4) == ('split', 15, -1)
    assert check_for_reduction(num5) == (None, None, -1)


def test_split_number():
    num1 = [1, 13]
    num2 = [[1, 9], [12, 5]]

    assert split_number(num1, 13) == [1, [6, 7]]
    assert split_number(num2, 12) == [[1, 9], [[6, 6], 5]]


def test_explode_pair():
    num1 = [[6, [5, [4, [3, 2]]]], 1]
    num2 = [7, [6, [5, [4, [3, 2]]]]]
    num3 = [[[[[9, 8], 1], 2], 3], 4]

    assert explode_pair(num1, [3, 2]) == [[6, [5, [7, 0]]], 3]
    assert explode_pair(num2, [3, 2]) == [7, [6, [5, [7, 0]]]]
    assert explode_pair(num3, [9, 8]) == [[[[0, 9], 2], 3], 4]
