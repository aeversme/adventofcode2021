def find_next_index(index, row_length, direction):
    next_index = index
    if direction == 'east':
        if index[1] == row_length - 1:
            next_index[1] = 0
        else:
            next_index[1] = index[1] + 1
    return next_index


def movement_step(slug_map):
    east_copy = []

    for row in slug_map:
        row_length = len(row)
        updated_row = ''
        if row[0] == '.' and row[row_length - 1] == '>':
            updated_row += '>'
        for c in range(len(row)):
            ur_length = len(updated_row)
            if c < ur_length:
                continue
            elif row[c] == '>':
                current_index = [slug_map.index(row), c]
                next_index = find_next_index(current_index, row_length, 'east')
                if row[next_index[1]] == '.':
                    updated_row += '.>'
                else:
                    updated_row += '>'
            else:
                updated_row += row[c]
        east_copy.append(updated_row)

    south_copy = []

    # south-facing herd:
    # loop through each index in each string of east_copy
    # if 'v', look at next_index (wrapping to first string same column) to determine if slug can move
    # if slug can move, change south_copy current_index to '.' and next_index to 'v'

    return east_copy
