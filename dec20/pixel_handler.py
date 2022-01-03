def count_lit_pixels(image):
    """
    Takes a list of strings. Returns a count of the number of '#' characters in the list.
    """
    lit_pixel_count = 0
    for line in image:
        lit_pixel_count += line.count('#')
    return lit_pixel_count


def is_not_on_image(row, col, image):
    """
    Takes an 'image' (a list of strings) and two integer values. Determines if the the row or column values fall
    outside the index range of the image; if so, returns True. Otherwise (if [row][column] is within the bounds of the
    image), returns False.
    """

    rules = [row < 0, row > (len(image) - 1), col < 0, col > (len(image[0]) - 1)]
    if any(rules):
        return True
    return False


def construct_pixel_binary(row, col, image, iteration):
    """
    Takes a row and column integer, a list of strings, and an iteration integer. For the given row and column
    indexes, finds the eight surrounding locations. If any location is not on the image, assumes a value based on the
    iteration number. If a location is on the image, checks the value; adds a '1' to the pixel binary string if the
    value is a '#' and adds a '0' otherwise. Returns the pixel binary string.
    """
    pixel_binary = ''
    grid = [
        [row - 1, col - 1], [row - 1, col], [row - 1, col + 1],
        [row, col - 1], [row, col], [row, col + 1],
        [row + 1, col - 1], [row + 1, col], [row + 1, col + 1]
    ]
    for location in grid:
        if is_not_on_image(location[0], location[1], image):
            if iteration % 2 == 0:
                pixel_binary += '0'
            else:
                pixel_binary += '1'
        elif image[location[0]][location[1]] == '#':
            pixel_binary += '1'
        else:
            pixel_binary += '0'
    return pixel_binary


def convert_image(image_algorithm, image, iteration):
    """
    Takes an image algorithm string, a list of strings, and an iteration integer. For each index position in each
    string (each column of each row in the image), uses the pixel binary to determine which character ('.' or '#')
    should go in that position in the new string for that row. Adds completed strings to the list of converted
    strings, and returns that list.
    """
    converted_image = []
    for row in range(len(image)):
        new_row = ''
        for col in range(len(image[0])):
            pixel_binary = construct_pixel_binary(row, col, image, iteration)
            algorithm_index = int(pixel_binary, 2)
            new_row += image_algorithm[algorithm_index]
        converted_image.append(new_row)
    return converted_image
