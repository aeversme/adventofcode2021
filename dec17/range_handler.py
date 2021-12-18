from probe_handler import change_x_velocity


def determine_xv_range(target):
    """
    Takes a list of lists (x and y ranges). For each integer up to the minimum value of the x range of the target,
    performs probe movement steps considering only x position and x velocity (the starting integer). If the x
    position is within the target x range when the x velocity reaches zero, adds the starting integer to a listm of
    possible starting x velocities.

    Returns the list of possible starting x velocities.
    """

    possible_starting_xv = []
    for i in range(min(target[0])):
        xp = i
        xv = change_x_velocity(i)
        while xv > 0:
            xp += xv
            xv = change_x_velocity(xv)
        if min(target[0]) <= xp <= max(target[0]):
            possible_starting_xv.append(i)
    return possible_starting_xv
