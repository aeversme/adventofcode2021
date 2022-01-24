def perform_initialization_step(cube_dict, step):
    dict_copy = cube_dict.copy()
    for i in range(step[1][0][0], step[1][0][1] + 1):
        for j in range(step[1][1][0], step[1][1][1] + 1):
            for k in range(step[1][2][0], step[1][2][1] + 1):
                dict_copy[i, j, k] = step[0]
    return dict_copy
