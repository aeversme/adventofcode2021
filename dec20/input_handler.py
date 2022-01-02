def convert_input(data):
    data_strip = [i.strip('\n') for i in data]
    image_algorithm = data_strip.pop(0)
    data_filter = [i for i in data_strip if len(i) > 0]
    return image_algorithm, data_filter
