from input_handler import convert_input
from error_handler import check_for_errors, score_error

with open('navsyntax.txt') as n:
    nav_raw = n.readlines()

nav_syntax = convert_input(nav_raw)
# print(nav_syntax)


def syntax_score(syntax_file):
    total_error_score = 0
    for syntax in syntax_file:
        incorrect_symbol = check_for_errors(syntax)
        if incorrect_symbol is not None:
            error_score = score_error(incorrect_symbol)
            total_error_score += error_score
            # print(f"Error on line {syntax_file.index(syntax)}.")
            # print(f"Added {error_score} to total.")
        else:
            # print(f"No errors on line {syntax_file.index(syntax)}.")
            continue
    return total_error_score


score = syntax_score(nav_syntax)
print(f"The total error score is: {score}")
