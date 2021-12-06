def count_overlaps(plot):
    """
    Takes a 2-dimensional 'plot' list. Returns the number of occurrences of an integer greater than 1 (which
    represents where at least two lines overlap).
    """
    overlap_count = 0
    for row in plot:
        for element in row:
            if element > 1:
                overlap_count += 1
    return overlap_count
