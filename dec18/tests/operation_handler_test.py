from ..operation_handler import add_numbers, split_number, explode_pair


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

    assert split_number(num1, 13) == [1, [6, 7]]
    assert split_number(num2, 12) == [[1, 9], [[6, 6], 5]]


def test_explode_pair():
    num1 = [[6, [5, [4, [3, 2]]]], 1]
    num2 = [7, [6, [5, [4, [3, 2]]]]]
    num3 = [[[[[9, 8], 1], 2], 3], 4]

    assert explode_pair(num1, [3, 2]) == [[6, [5, [7, 0]]], 3]
    assert explode_pair(num2, [3, 2]) == [7, [6, [5, [7, 0]]]]
    assert explode_pair(num3, [9, 8]) == [[[[0, 9], 2], 3], 4]
