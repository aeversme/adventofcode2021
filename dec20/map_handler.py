def expand_trenchmap(trenchmap):
    """
    Takes a list of strings. Adds lines of 'dark pixels' ('.') before and after the input list data, and for each
    string in the data, adds dark pixels to the beginning and end. For part 1, these values were 1/10th of current
    values. Returns a new, 'expanded' list.
    """
    expanded_trenchmap = []
    mapline_length = len(trenchmap[0])
    for _ in range(50):
        expanded_trenchmap.append('.' * mapline_length + '.' * 100)
    for line in trenchmap:
        expanded_trenchmap.append('.' * 50 + line + '.' * 50)
    for _ in range(50):
        expanded_trenchmap.append('.' * mapline_length + '.' * 100)
    return expanded_trenchmap
