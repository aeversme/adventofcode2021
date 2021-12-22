from sb_handler import Scanner, Beacon


def convert_input(data):
    data_strip = [i.strip() for i in data]
    data_filter = list(filter(None, data_strip))
    data_filter.append('--- scanner ---')
    # print(data_filter)

    scanner_indexes = [data_filter.index(i) for i in data_filter if 'scanner' in i]
    # print(scanner_indexes)

    scanners = []
    for i in range(len(scanner_indexes) - 1):
        new_scanner = Scanner(data_filter[scanner_indexes[i]].strip(' -'))
        scanners.append(new_scanner)

        for j in range(scanner_indexes[i] + 1, scanner_indexes[i + 1]):
            beacon_coords = data_filter[j].split(',')
            beacon_coords = [int(i) for i in beacon_coords]
            new_beacon = Beacon(beacon_coords[0], beacon_coords[1], beacon_coords[2], new_scanner)
            new_scanner.beacons.append(new_beacon)

    return data_filter, scanners
