from input_handler import convert_input

with open('caves.txt') as c:
    caves_raw = c.readlines()


def add_connection(caves, cave0, cave1):
    if cave0 not in caves.keys():
        caves[cave0] = []

    caves[cave0].append(cave1)


def create_map(cave_connections):
    caves = {}
    for connection in cave_connections:
        first_cave = connection[0]
        second_cave = connection[1]

        add_connection(caves, first_cave, second_cave)
        add_connection(caves, second_cave, first_cave)
    return caves


cave_map = create_map(convert_input(caves_raw))
print(cave_map)

path = []
path_count = 0


def enter_cave(cave_name, entrance):
    global cave_map, path, path_count

    path.append(cave_name)
    print(f"{len(path) * '  '}In {cave_name} from {entrance}, path: {path}")

    if len(path) < 100:
        for cave_exit in cave_map[cave_name]:
            print(f"{len(path) * '  '}Looking at exit {cave_exit}...")
            if path.count(cave_exit) > 0 and cave_exit.islower():
                print(f"{len(path) * '  '}Can't go back to {cave_exit}.")
            elif cave_exit == 'end':
                path_count += 1
                print(f"{len(path) * '  '}=== Found end. Path: {path}")
            else:
                enter_cave(cave_exit, cave_name)

    path.pop()
    return


enter_cave('start', None)
print(f"Path count: {path_count}")
