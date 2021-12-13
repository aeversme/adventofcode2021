def print_grid(grid):
    for row in grid:
        print(' '.join(row))
    print("\n")


def fold_up(grid, fold):
    top_part = grid[:fold]
    bottom_part = grid[fold + 1:]
    top_row_count = len(top_part)
    bottom_row_count = len(bottom_part)

    if bottom_row_count > top_row_count:
        print("Bottom row count is greater.")
        quit()

    # print_grid(top_part)
    bottom_reversed = [row for row in reversed(bottom_part)]
    # print_grid(bottom_reversed)
    combined_grid = top_part.copy()

    row_offset = top_row_count - bottom_row_count
    for row_num in range(row_offset, len(top_part)):
        for col_num in range(len(top_part[0])):
            if bottom_reversed[row_num - row_offset][col_num] == '#':
                combined_grid[row_num][col_num] = bottom_reversed[row_num - row_offset][col_num]

    # print_grid(combined_grid)

    return combined_grid


def fold_left(grid, fold):
    left_part = [row[:fold] for row in grid]
    right_part = [row[fold + 1:] for row in grid]
    left_col_count = len(left_part[0])
    right_col_count = len(right_part[0])

    if right_col_count > left_col_count:
        print("Right column count is greater.")
        quit()

    # print_grid(left_part)
    right_reversed = [[element for element in reversed(row)] for row in right_part]
    # print_grid(right_reversed)
    combined_grid = left_part.copy()

    col_offset = left_col_count - right_col_count
    for row_num in range(len(left_part)):
        for col_num in range(col_offset, len(left_part[0])):
            if right_reversed[row_num][col_num - col_offset] == '#':
                combined_grid[row_num][col_num] = right_reversed[row_num][col_num - col_offset]

    # print_grid(combined_grid)

    return combined_grid


def fold_paper(grid, fold):
    if fold[0] == 'y':
        print(f"Folding up on row {fold[1] + 1}...")
        folded_paper = fold_up(grid, fold[1])
    else:
        print(f"Folding left on column {fold[1] + 1}...")
        folded_paper = fold_left(grid, fold[1])
    return folded_paper
