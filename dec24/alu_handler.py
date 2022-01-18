def alu(opcode, var1, var2):
    if opcode == 'add':
        return var1 + var2
    elif opcode == 'mul':
        return var1 * var2
    elif opcode == 'div':
        return var1 // var2
    elif opcode == 'mod':
        return var1 % var2
    elif opcode == 'eql':
        if var1 == var2:
            return 1
        else:
            return 0
    else:
        return "Invalid opcode, check the input."
