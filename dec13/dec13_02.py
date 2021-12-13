from input_handler import convert_input
from grid_handler import create_paper
from fold_handler import fold_paper, print_grid

with open('origami.txt') as o:
    origami_raw = o.readlines()

folds, coordinates = convert_input(origami_raw)
paper = create_paper(coordinates)

print(f"Columns: {len(paper[0])}, rows: {len(paper)}")

folded_paper = paper.copy()
for fold in folds:
    folded_paper = fold_paper(folded_paper, fold)

print_grid(folded_paper)
