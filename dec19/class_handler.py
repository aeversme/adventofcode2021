# scanner & beacon handler

class Scanner:
    def __init__(self, name):
        self.name = name.capitalize()
        self.beacons = []
        self.x = 0
        self.y = 0
        self.z = 0

    def __repr__(self):
        return f"{self.name}: position {self.x}, {self.y}, {self.z}"


class Beacon:
    def __init__(self, x, y, z, scanner):
        self.x = x
        self.y = y
        self.z = z
        self.abs_x = None
        self.abs_y = None
        self.abs_z = None
        self.scanned_by = scanner
        self.shared_with = None
        self.on_beacon_list = False

    def __repr__(self):
        if self.abs_x:
            return f"Beacon: {self.abs_x}, {self.abs_y}, {self.abs_z}"
        else:
            return f"Beacon: {self.x}, {self.y}, {self.z}"
