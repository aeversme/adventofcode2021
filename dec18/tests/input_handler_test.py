from ..input_handler import convert_input


def test_convert_input():
    input_string = '[[1,9],[8,5]]'
    output_list = convert_input(input_string)

    assert type(output_list) == list
