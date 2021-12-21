# scanner & beacon handler

class Scanner:
    def __init__(self, name):
        self.name = name
        self.beacons = []
        self.x = 0
        self.y = 0
        self.z = 0

    def __repr__(self):
        print(f"Scanner: {self.name}, position {self.x}, {self.y}, {self.z}")


class Beacon:
    def __init__(self, x, y, z, scanner):
        self.x = x
        self.y = y
        self.z = z
        self.scanned_by = scanner
        self.shared_with = None
        self.on_beacon_list = False

    def __repr__(self):
        print(f"{self.x}, {self.y}, {self.z}")
