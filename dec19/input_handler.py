from sb_handler import Scanner


def convert_input(data):
    data_strip = [i.strip() for i in data]
    data_filter = list(filter(None, data_strip))
    print(data_filter)

    scanner_indexes = [data_filter.index(i) for i in data_filter if 's' in i]
    print(scanner_indexes)

    scanners = []
    # TODO: fix TypeError when trying to print each new scanner - something not getting created properly?
    for n in scanner_indexes:
        print(data_filter[n])
        new_scanner = Scanner(data_filter[n].strip(' -'))
        print(new_scanner)
        scanners.append(new_scanner)
        print(f"scanners list contains {len(scanners)} object(s)")

    return data_filter, scanners
