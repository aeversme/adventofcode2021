from ..alu_handler import process_operation


def test_process_operation():

    assert process_operation('add', 1, 2) == 3
    assert process_operation('mul', 3, 4) == 12
    assert process_operation('div', 4, 2) == 2
    assert process_operation('div', 9, 2) == 4
    assert process_operation('div', 4, 0) == 'Error: cannot divide by 0.'
    assert process_operation('mod', 3, 2) == 1
    assert process_operation('mod', 7, 4) == 3
    assert process_operation('mod', -1, 6) == 'Error: invalid modulus operand(s).'
    assert process_operation('mod', 1, -1) == 'Error: invalid modulus operand(s).'
    assert process_operation('mod', -1, 0) == 'Error: invalid modulus operand(s).'
    assert process_operation('eql', 6, 6) == 1
    assert process_operation('eql', 7, 5) == 0
    assert process_operation('sub', 5, 2) == 'Invalid opcode, check the input.'
