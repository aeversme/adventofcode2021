from input_handler import convert_input
from grid_handler import create_paper
from fold_handler import fold_paper

with open('origami.txt') as o:
    origami_raw = o.readlines()

folds, coordinates = convert_input(origami_raw)
paper = create_paper(coordinates)

print(f"Columns: {len(paper[0])}, rows: {len(paper)}")

first_fold = fold_paper(paper, folds[0])

dot_count = 0
for row in first_fold:
    for element in row:
        if element == '#':
            dot_count += 1

print(f"Dot count: {dot_count}")
