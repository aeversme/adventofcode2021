def find_next_index(index, row_length, col_count, direction):
    next_index = index
    if direction == 'east':
        if index[1] == row_length - 1:
            next_index[1] = 0
        else:
            next_index[1] = index[1] + 1
    else:
        if index[0] == col_count - 1:
            next_index[0] = 0
        else:
            next_index[0] = index[0] + 1
    return next_index


def movement_step(slug_map):
    movement_count = 0

    east_copy = []

    for row in slug_map:
        row_length = len(row)
        updated_row = ''
        to_beginning = False
        if row[0] == '.' and row[row_length - 1] == '>':
            updated_row += '>'
            to_beginning = True
            movement_count += 1
        for c in range(len(row)):
            ur_length = len(updated_row)
            if c < ur_length:
                continue
            elif c == row_length - 1 and to_beginning:
                updated_row += '.'
            elif row[c] == '>':
                current_index = [slug_map.index(row), c]
                next_index = find_next_index(current_index, row_length, len(slug_map), 'east')
                if row[next_index[1]] == '.':
                    updated_row += '.>'
                    movement_count += 1
                else:
                    updated_row += '>'
            else:
                updated_row += row[c]
        east_copy.append(updated_row)

    south_copy = east_copy.copy()

    for row in east_copy:
        col_height = len(east_copy)
        row_index = east_copy.index(row)
        for c in range(len(row)):
            if row[c] == 'v':
                current_index = [row_index, c]
                next_index = find_next_index(current_index, len(row), col_height, 'south')
                if east_copy[next_index[0]][c] == '.':
                    south_copy[next_index[0]] = south_copy[next_index[0]][:c] + 'v' + south_copy[next_index[0]][c + 1:]
                    south_copy[row_index] = south_copy[row_index][:c] + '.' + south_copy[row_index][c + 1:]
                    movement_count += 1

    return south_copy, movement_count
