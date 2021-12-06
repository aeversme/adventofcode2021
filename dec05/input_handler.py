def convert_input(vent_data):
    vents_strip = [i.strip('\n') for i in vent_data]
    vents_replace = [i.replace(' -> ', ',') for i in vents_strip]
    vents_split = [i.split(',') for i in vents_replace]
    for i in vents_split:
        for j in range(4):
            i[j] = int(i[j])
    return vents_split


def find_max_value(vent_list):
    max_value = 0
    for row in vent_list:
        highest_row_value = max(row)
        if highest_row_value > max_value:
            max_value = highest_row_value
    return max_value
