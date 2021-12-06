def count_overlaps(plot):
    overlap_count = 0
    for row in plot:
        for element in row:
            if element >= 2:
                overlap_count += 1
    return overlap_count
