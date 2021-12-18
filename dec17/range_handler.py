from probe_handler import change_x_velocity


def determine_xv_range(target):
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
