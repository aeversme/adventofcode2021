from map_handler import create_chiton_map, create_chiton_cave, is_on_map, find_smallest_distance

with open('chiton.txt') as ch:
    chiton_raw = ch.readlines()

part_one = False

if part_one:
    chiton_map = create_chiton_map(chiton_raw)
else:
    chiton_map = create_chiton_cave(chiton_raw)


def dijkstra_step(chitons, node, active_nodes):
    """
    Takes a list of lists of Chiton objects, and a Chiton object. Implements one step of the Dijkstra shortest path
    algorithm:
    - Evaluates all neighbors of the node (Chiton object). If a neighbor is within the map boundary, has not been
    marked as visited, and the sum of the current node distance (from the starting node) and the neighbor's value is
    less than the neighbor's distance, sets the neighbor's distance to that sum. Adds the neighbor to the active nodes
    list.
    - Sets the current node's visited attribute to True.
    """

    row = node.row
    col = node.col
    directions = [[row - 1, col], [row + 1, col], [row, col - 1], [row, col + 1]]
    for direction in directions:
        r = direction[0]
        c = direction[1]
        neighbor = None
        if is_on_map(chitons, r, c):
            neighbor = chitons[r][c]
        if neighbor is not None and not neighbor.visited and node.distance + neighbor.value < neighbor.distance:
            neighbor.distance = node.distance + neighbor.value
            neighbor.parent = [node.row, node.col]
            active_nodes.append(neighbor)
    node.visited = True


def clear_node_from_active(node, active_nodes):
    """
    Takes a node and an active node list. Removes the node if it is in the active nodes list and returns the active
    node list.
    """

    if active_nodes.count(node) > 0:
        active_nodes.pop(active_nodes.index(node))
    return active_nodes


def find_lowest_value_path():
    """
    Determines which Chiton object is in the bottom right corner of the map. While that object's visited attribute is
    False:
    - Sets the current node to the Chiton object on the map with the smallest distance attribute.
    - Performs one step of the Dijkstra algorithm using the current node.
    - Removes the current node from the active nodes list.
    Once the bottom right object's visited attribute is set to True, returns that object's distance attribute.
    """

    bottom_right = chiton_map[len(chiton_map) - 1][len(chiton_map[0]) - 1]
    # step_count = 0
    active_nodes = []
    while not bottom_right.visited:
        current_node = find_smallest_distance(chiton_map, active_nodes)
        dijkstra_step(chiton_map, current_node, active_nodes)
        active_nodes = clear_node_from_active(current_node, active_nodes)
        # step_count += 1
        # print(f"{step_count}: {len(active_nodes)} active nodes")
    return bottom_right.distance


print(f"Lowest total risk: {find_lowest_value_path()}")
