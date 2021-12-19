from ..procedure_handler import check_for_reduction, addition_with_checks


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


def test_addition_with_checks():
    num1 = [[[[4, 3], 4], 4], [7, [[8, 4], 9]]]
    num2 = [1, 1]

    assert addition_with_checks(num1, num2) == [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]
