def process_operation(opcode, var1, var2):
    if opcode == 'add':
        return var1 + var2
    elif opcode == 'mul':
        return var1 * var2
    elif opcode == 'div':
        if var2 == 0:
            return 'Error: cannot divide by 0.'
        return var1 // var2
    elif opcode == 'mod':
        if var1 < 0 or var2 <= 0:
            return 'Error: invalid modulus operand(s).'
        return var1 % var2
    elif opcode == 'eql':
        if var1 == var2:
            return 1
        else:
            return 0
    else:
        return 'Invalid opcode, check the input.'
