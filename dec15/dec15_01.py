from map_handler import create_chiton_map, is_on_map, find_smallest_distance

with open('chiton.txt') as ch:
    chiton_raw = ch.readlines()

chiton_map = create_chiton_map(chiton_raw)


def dijkstra_step(chitons, node):
    """
    Takes a list of lists of Chiton objects, and a Chiton object. Implements one step of the Dijkstra shortest path
    algorithm:
    - Evaluates all neighbors of the node (Chiton object). If a neighbor is within the map boundary, has not been
    marked as visited, and the sum of the current node distance (from the starting node) and the neighbor's value is
    less than the neighbor's distance, sets the neighbor's distance to that sum.
    - Sets the current node's visited attribute to True.
    """

    row = node.row
    col = node.col
    directions = [[row - 1, col], [row + 1, col], [row, col - 1], [row, col + 1]]
    for direction in directions:
        r = direction[0]
        c = direction[1]
        if is_on_map(chitons, r, c) and not chitons[r][c].visited and node.distance + chitons[r][c].value\
                < chitons[r][c].distance:
            chitons[r][c].distance = node.distance + chitons[r][c].value
            chitons[r][c].parent = [node.row, node.col]
    node.visited = True


def find_lowest_value_path():
    """
    Determines which Chiton object is in the bottom right corner of the map. While that object's visited attribute is
    False:
    - Sets the current node to the Chiton object on the map with the smallest distance attribute.
    - Performs one step of the Dijkstra algorithm using the current node.
    Once the bottom right object's visited attribute is set to True, returns that object's distance attribute.
    """

    bottom_right = chiton_map[len(chiton_map) - 1][len(chiton_map[0]) - 1]
    while not bottom_right.visited:
        current_node = find_smallest_distance(chiton_map)
        dijkstra_step(chiton_map, current_node)
    return bottom_right.distance


print(f"Lowest total risk: {find_lowest_value_path()}")
