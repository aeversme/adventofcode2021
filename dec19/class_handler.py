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
        """
        Returns a list of three signed integers, representing the scanner's x, y, and z coordinates relative to its
        immediate parent scanner.
        """
        return [self.rel_x, self.rel_y, self.rel_z]

    def abs_xyz(self):
        """
        Returns a list of three signed integers, representing the scanner's x, y, and z coordinates relative to the
        origin scanner [0, 0, 0].
        """
        return [self.abs_x, self.abs_y, self.abs_z]

    def calc_scanner_absolute_coordinates(self, scanner_xyz):
        """
        Takes a list of three signed integers, representing relative x, y, and z coordinates. Returns a new list of
        integers, sometimes recursively, representing absolute x, y, and z coordinates.
        """
        # scanner_xyz = self.rel_xyz()
        new_xyz = [0, 0, 0]
        if self.parent_scanner and self.parent_scanner.name != 'Scanner 0':
            parent_xyz = self.parent_scanner.rel_xyz()
            parent_transform = self.parent_scanner.transform_matrix
            for n in range(3):
                index = parent_transform[n][0]
                transform_factor = parent_transform[n][1]
                new_xyz[index] = (scanner_xyz[n] * transform_factor) + parent_xyz[index]
            new_xyz = self.parent_scanner.calc_scanner_absolute_coordinates(new_xyz)
        else:
            for n in range(3):
                new_xyz[n] = scanner_xyz[n]
        self.abs_x = new_xyz[0]
        self.abs_y = new_xyz[1]
        self.abs_z = new_xyz[2]
        return new_xyz

    def transform_beacon_coordinates(self):
        """
        Compiles a list of beacon coordinates (lists of three signed integers) by recursively adding a child
        scanner's beacons and transforming those beacons to the parent scanner's coordinate system and orientation
        before passing the list back through the stack. Returns a list of beacons whose coordinates are all in the
        same system and orientation to one another.
        """
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
            # print(f"child {child.name} passing back {len(child_coordinates)} coordinates...")
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
        """
        Takes a list of Scanner objects. Compares all scanners in the list. If two scanners share enough beacons,
        adds the second scanner to the first scanner's child scanners list. Recursively discovers relationships for
        all scanners, such that each scanner only has one parent. As scanners are passed into the function,
        removes the scanner from the list. If the list is empty, returns 0.
        """
        if self in scanners:
            scanners.remove(self)
        for scanner in scanners:
            diff_dict_filter, sum_dict_filter = find_shared_beacons(self, scanner)
            if (diff_dict_filter or sum_dict_filter) and scanner.parent_scanner == self:
                self.child_scanners.append(scanner)
        # print(f"{self.name} child scanners: {self.child_scanners}")
        for child in self.child_scanners:
            child.discover_scanner_relationships(scanners)
        if len(scanners) == 0:
            return 0


class Beacon:
    def __init__(self, x, y, z, scanner):
        self.x = x
        self.y = y
        self.z = z
        self.scanned_by = scanner

    def __repr__(self):
        return f"Beacon: {self.x}, {self.y}, {self.z}"

    def xyz(self):
        """
        Returns a list of three signed integers, representing the beacon's x, y, and z coordinates relative to its
        parent scanner.
        """
        return [self.x, self.y, self.z]
