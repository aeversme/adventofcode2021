def count_lit_pixels(trenchmap):
    lit_pixel_count = 0
    for line in trenchmap:
        lit_pixel_count += line.count('#')
    return lit_pixel_count
