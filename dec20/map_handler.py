def expand_trenchmap(trenchmap):
    expanded_trenchmap = []
    mapline_length = len(trenchmap[0])
    for _ in range(4):
        expanded_trenchmap.append('.' * mapline_length + '.' * 8)
    for line in trenchmap:
        expanded_trenchmap.append('.' * 4 + line + '.' * 4)
    for _ in range(4):
        expanded_trenchmap.append('.' * mapline_length + '.' * 8)
    return expanded_trenchmap
