def convert_input(data):
    data_strip = [i.strip('\n') for i in data]
    player_list = []
    for item in data_strip:
        player_list.append([item[:8], int(item[-1])])
    return player_list
