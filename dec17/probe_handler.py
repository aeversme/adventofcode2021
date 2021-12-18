def change_x_velocity(xv):
    """
    Takes an integer. Modifies the integer based on its starting value, and returns the new integer.
    """

    if xv > 0:
        new_xv = xv - 1
    elif xv < 0:
        new_xv = xv + 1
    else:
        new_xv = 0
    return new_xv


def probe_single_step(xp, yp, xv, yv):
    """
    Takes four integer values. Modifies position values by adding respective velocity values. Modifies x velocity by
    passing the xv value into change_x_velocity(). Subtracts 1 from yv value. Returns new position and velocity values.
    """

    new_xp = xp + xv
    new_yp = yp + yv
    new_xv = change_x_velocity(xv)
    new_yv = yv - 1
    return new_xp, new_yp, new_xv, new_yv


def is_probe_in_target(target, xp, yp):
    """
    Takes a list of lists (x and y ranges) and two integers. If the xv value is within the x range and the yv value
    is within the y range, returns True. Otherwise, returns False.
    """

    if target[0][0] <= xp <= target[0][1] and target[1][0] <= yp <= target[1][1]:
        return True
    return False


def check_probe_trajectory(target, xv, yv):
    """
    Takes a list of lists (x and y ranges) and two integers.

    While both position values xp and yp have not gone past the target range, performs probe movement steps and
    checks whether the probe position after each step is within the target area. Adds the y position of each step to
    a list of heights. If the probe never ends a step within the target area, resets the heights list to an empty list.

    Returns the height list.
    """

    height_list = []
    xp = 0
    yp = 0
    hits_target = False

    while xp < max(target[0]) and yp > min(target[1]):
        xp, yp, xv, yv = probe_single_step(xp, yp, xv, yv)
        # print(f"Position: [{xp}, {yp}]")
        height_list.append(yp)
        if is_probe_in_target(target, xp, yp):
            hits_target = True
            break

    if not hits_target:
        height_list = []

    return height_list
