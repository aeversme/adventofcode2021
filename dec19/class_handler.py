from beacon_handler import find_shared_beacons


class Scanner:
    def __init__(self, name):
        self.name = name.capitalize()
        self.beacons = []
        self.rel_x = 0
        self.rel_y = 0
        self.rel_z = 0
        self.abs_x = 0
        self.abs_y = 0
        self.abs_z = 0
        self.transform_matrix = [[0, 1], [1, 1], [2, 1]]
        self.parent_scanner = None
        self.child_scanners = []

    def __repr__(self):
        if self.name == "Scanner 0":
            return f"{self.name}: position {self.rel_x}, {self.rel_y}, {self.rel_z}"
        elif self.name != "Scanner 0" and self.rel_x != 0:
            return f"{self.name}: position {self.rel_x}, {self.rel_y}, {self.rel_z} relative to parent " \
                   f"{self.parent_scanner.name}\n" \
                   f"           transform {self.transform_matrix}"
        else:
            return f"{self.name}"

    def rel_xyz(self):
        return [self.rel_x, self.rel_y, self.rel_z]

    def abs_xyz(self):
        return [self.abs_x, self.abs_y, self.abs_z]

    # def calc_scanner_absolute_coordinates(self):
    #     scanner_xyz = self.rel_xyz()
    #     new_xyz = [0, 0, 0]
    #     if self.parent_scanner:
    #         parent_xyz = self.parent_scanner.abs_xyz()
    #         parent_transform = self.parent_scanner.transform_matrix
    #         for i in range(3):
    #             for j in range(3):
    #                 new_xyz[i] += ((parent_xyz[j] * parent_transform[i][j]) + scanner_xyz[j]) * \
    #                               parent_transform[i][j]
    #
    #     self.abs_x = new_xyz[0]
    #     self.abs_y = new_xyz[1]
    #     self.abs_z = new_xyz[2]
    #     return new_xyz

    def transform_beacon_coordinates(self):
        transformed_beacons = []
        scanner_xyz = self.rel_xyz()
        beacons_xyz = []
        for beacon in self.beacons:
            beacons_xyz.append(beacon.xyz())
        # print(f"{self.name} {len(beacons_xyz)} beacons_xyz: {beacons_xyz}")
        for child in self.child_scanners:
            child_coordinates = child.transform_beacon_coordinates()
            for coordinate in child_coordinates:
                beacons_xyz.append(coordinate)
            print(f"child {child.name} passing back {len(child_coordinates)} coordinates...")
        for beacon_xyz in beacons_xyz:
            beacon_in_parent_xyz = [0, 0, 0]
            for n in range(3):
                index = self.transform_matrix[n][0]
                transform_factor = self.transform_matrix[n][1]
                beacon_in_parent_xyz[index] = (beacon_xyz[n] * transform_factor) + scanner_xyz[index]
            transformed_beacons.append(beacon_in_parent_xyz)
            # print(f"{beacon_xyz} becomes {beacon_in_parent_xyz}")
        # print(f"{self.name} transformed: {transformed_beacons}")
        return transformed_beacons

    def discover_scanner_relationships(self, scanners):
        if self in scanners:
            scanners.remove(self)
        for scanner in scanners:
            diff_dict_filter, sum_dict_filter = find_shared_beacons(self, scanner)
            if diff_dict_filter or sum_dict_filter and scanner.parent_scanner == self:
                self.child_scanners.append(scanner)
                scanners.remove(scanner)
        print(f"{self.name} child scanners: {self.child_scanners}")
        for child in self.child_scanners:
            child.discover_scanner_relationships(scanners)


class Beacon:
    def __init__(self, x, y, z, scanner):
        self.x = x
        self.y = y
        self.z = z
        self.scanned_by = scanner
        self.shared_with = None
        self.on_beacon_list = False

    def __repr__(self):
        return f"Beacon: {self.x}, {self.y}, {self.z}"

    def xyz(self):
        return [self.x, self.y, self.z]
