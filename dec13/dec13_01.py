from input_handler import convert_input
from grid_handler import create_grid

with open('test-origami.txt') as o:
    origami_raw = o.readlines()

folds, coordinates = convert_input(origami_raw)

print(folds)
print(coordinates)

paper = create_grid(coordinates)
print(paper)
print(f"Columns: {len(paper[0])}, rows: {len(paper)}")
