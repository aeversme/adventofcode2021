def count_lit_pixels(image):
    lit_pixel_count = 0
    for line in image:
        lit_pixel_count += line.count('#')
    return lit_pixel_count


# TODO: account for pixels outside scope of image, based on iteration; if even, pixels == '.'; else pixels == '#'
def construct_pixel_binary(row, col, image):
    pixel_binary = ''
    grid = [
        [row - 1, col - 1], [row - 1, col], [row - 1, col + 1],
        [row, col - 1], [row, col], [row, col + 1],
        [row + 1, col - 1], [row + 1, col], [row + 1, col + 1]
    ]
    for location in grid:
        if image[location[0]][location[1]] == '#':
            pixel_binary += '1'
        else:
            pixel_binary += '0'
    return pixel_binary


def count_top_bottom_dark_lines(image):
    blank_top_lines = [i for i in range(5) if image[i].count('#') == 0]
    blank_bottom_lines = [i for i in range(len(image) - 1, len(image) - 6, -1) if image[i].count('#') == 0]
    return len(blank_top_lines), len(blank_bottom_lines)


# TODO: this is wrong, thinking in limited scope. this function goes away, as does the one above
def count_start_end_dark_pixels(row):
    pixel_count = [[row[:5], 0], [row[:-6:-1], 0]]
    for i in range(2):
        for string in pixel_count[i][0]:
            for char in string:
                if char == '.':
                    pixel_count[i][1] += 1
                else:
                    break
    return pixel_count[0][1], pixel_count[1][1]


def convert_image(image_algorithm, image):
    top_line_count, bottom_line_count = count_top_bottom_dark_lines(image)
    # TODO: this goes away, just iterate over every pixel in the expanded image
    converted_image = image[:(top_line_count - 1)]
    for row in range(top_line_count - 1, len(image) - bottom_line_count + 1):
        new_row = '.'
        # TODO: col range should be first and last lit pixel index
        leading_dark_pixels, trailing_dark_pixels = count_start_end_dark_pixels(image[row])
        for col in range(leading_dark_pixels, len(image[1]) - trailing_dark_pixels - 1):
            pixel_binary = construct_pixel_binary(row, col, image)
            algorithm_index = int(pixel_binary, 2)
            new_row += image_algorithm[algorithm_index]
        new_row += '.'
        converted_image.append(new_row)
    row_count = len(converted_image)
    for i in range(len(image) - 1, row_count - 1, -1):
        converted_image.append(image[i])
    return converted_image
