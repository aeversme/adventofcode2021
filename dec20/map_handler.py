def expand_trenchmap(trenchmap):
    expanded_trenchmap = []
    mapline_length = len(trenchmap[0])
    for _ in range(5):
        expanded_trenchmap.append('.' * mapline_length + '.' * 10)
    for line in trenchmap:
        expanded_trenchmap.append('.' * 5 + line + '.' * 5)
    for _ in range(5):
        expanded_trenchmap.append('.' * mapline_length + '.' * 10)
    return expanded_trenchmap
