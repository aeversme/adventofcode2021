from ..step_handler import perform_initialization_step


def create_cube_dict():
    cube_dict = {}
    for i in range(8, 15):
        for j in range(8, 15):
            for k in range(8, 15):
                cube_dict[i, j, k] = 'off'
    return cube_dict


def test_set_cube_status():
    step = ['on', [[10, 12], [10, 12], [10, 12]]]
    cube_dict = create_cube_dict()
    result = perform_initialization_step(cube_dict, step)

    on_count = 0
    for _, value in result.items():
        if value == 'on':
            on_count += 1

    assert on_count == 27
