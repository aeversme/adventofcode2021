def count_lit_pixels(image):
    lit_pixel_count = 0
    for line in image:
        lit_pixel_count += line.count('#')
    return lit_pixel_count


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
    blank_top_lines = [x for x in range(5) if image[x].count('#') == 0]
    blank_bottom_lines = [x for x in range(len(image) - 1, len(image) - 6, -1) if image[x].count('#') == 0]
    return len(blank_top_lines), len(blank_bottom_lines)


# TODO: create function to count dark pixels at front and end of a given row


def convert_image(image_algorithm, image):
    top_line_count, bottom_line_count = count_top_bottom_dark_lines(image)
    converted_image = image[:(top_line_count - 1)]
    for row in range(top_line_count - 1, len(image) - bottom_line_count + 1):
        new_row = '.'
        # TODO: col range should be first and last lit pixel index
        for col in range(1, len(image[1]) - 1):
            pixel_binary = construct_pixel_binary(row, col, image)
            algorithm_index = int(pixel_binary, 2)
            new_row += image_algorithm[algorithm_index]
        new_row += '.'
        converted_image.append(new_row)
    row_count = len(converted_image)
    for i in range(len(image) - 1, row_count - 1, -1):
        converted_image.append(image[i])
    return converted_image
