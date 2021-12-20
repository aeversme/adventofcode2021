from ..procedure_handler import check_for_reduction, addition_with_checks


def test_check_for_reduction():
    num1 = [[[[[9, 8], 1], 2], 3], 4]
    num2 = [[6, [5, [4, [3, 2]]]], 1]
    num3 = [[1, 9], [12, 5]]
    num4 = [[[5, 4], [15, [0, 13]]], [1, 1]]
    num5 = [[[[0, 7], 4], [15, [0, [1, 3]]]], [1, 1]]
    num6 = [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], 9]

    assert check_for_reduction(num1) == ('explode', '[9, 8]', 4)
    assert check_for_reduction(num2) == ('explode', '[3, 2]', 13)
    assert check_for_reduction(num3) == ('split', '12', 10)
    assert check_for_reduction(num4) == ('split', '15', 11)
    assert check_for_reduction(num5) == ('explode', '[1, 3]', 24)
    assert check_for_reduction(num6) == (None, None, None)


def test_addition_with_checks():
    num1 = [[[[4, 3], 4], 4], [7, [[8, 4], 9]]]
    num2 = [1, 1]

    assert addition_with_checks(num1, num2) == [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]
