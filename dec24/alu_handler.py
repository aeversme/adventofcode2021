def process_operation(opcode, var1, var2):
    if opcode == 1:
        return var1 + var2
    elif opcode == 2:
        return var1 * var2
    elif opcode == 3:
        if var2 == 0:
            return 'Error: cannot divide by 0.'
        return var1 // var2
    elif opcode == 4:
        if var1 < 0 or var2 <= 0:
            return 'Error: invalid modulus operand(s).'
        return var1 % var2
    elif opcode == 5:
        if var1 == var2:
            return 1
        else:
            return 0
    else:
        return 'Invalid opcode, check the input.'
