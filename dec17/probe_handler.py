def change_x_velocity(xv):
    if xv > 0:
        new_xv = xv - 1
    elif xv < 0:
        new_xv = xv + 1
    else:
        new_xv = 0
    return new_xv


def probe_single_step(xp, yp, xv, yv):
    new_xp = xp + xv
    new_yp = yp + yv
    new_xv = change_x_velocity(xv)
    new_yv = yv - 1
    return new_xp, new_yp, new_xv, new_yv


def is_probe_in_target(target, xp, yp):
    if target[0][0] <= xp <= target[0][1] and target[1][0] <= yp <= target[1][1]:
        return True
    return False


def check_probe_trajectory(target, x_velocity, y_velocity):
    height_list = []
    xp = 0
    yp = 0
    hits_target = False

    while xp < target[0][1] and yp > target[1][0]:
        xp, yp, x_velocity, y_velocity = probe_single_step(xp, yp, x_velocity, y_velocity)
        # print(f"Position: [{xp}, {yp}]")
        height_list.append(yp)
        if is_probe_in_target(target, xp, yp):
            hits_target = True
            break

    if not hits_target:
        height_list = []

    return height_list
