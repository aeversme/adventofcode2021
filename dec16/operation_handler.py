def perform_operation(type_id, operand_list):
    value = 0
    if type_id == 0:
        assert (len(operand_list) > 0)
        value = sum(operand_list)
    elif type_id == 1:
        assert (len(operand_list) > 0)
        value = 1
        for m in operand_list:
            value *= m
    elif type_id == 2:
        assert (len(operand_list) > 0)
        value = min(operand_list)
    elif type_id == 3:
        assert (len(operand_list) > 0)
        value = max(operand_list)
    elif type_id == 5:
        assert (len(operand_list) == 2)
        value = 1 if operand_list[0] > operand_list[1] else 0
    elif type_id == 6:
        assert (len(operand_list) == 2)
        value = 1 if operand_list[0] < operand_list[1] else 0
    elif type_id == 7:
        assert (len(operand_list) == 2)
        value = 1 if operand_list[0] == operand_list[1] else 0
    return value
