import numpy as np


class Chiton:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = int(value)
        self.distance = np.inf
        self.visited = False
        self.parent = []

    def __repr__(self):
        return f"[{self.row}, {self.col}]: val = {self.value}, dist = {self.distance}, vis = {self.visited}, " \
               f"par = {self.parent}"
