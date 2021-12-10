from input_handler import convert_input
from string_handler import check_syntax_string
from score_handler import score_error

with open('navsyntax.txt') as n:
    nav_raw = n.readlines()

nav_syntax = convert_input(nav_raw)
# print(nav_syntax)


def error_score(syntax_file):
    total_error_score = 0
    for syntax in syntax_file:
        check_result = check_syntax_string(syntax)
        if isinstance(check_result, str):
            score = score_error(check_result)
            total_error_score += score
            # print(f"Error on line {syntax_file.index(syntax)}.")
            # print(f"Added {score} to total.")
        else:
            # print(f"No errors on line {syntax_file.index(syntax)}.")
            continue
    return total_error_score


total_score = error_score(nav_syntax)
print(f"The total error score is: {total_score}")
