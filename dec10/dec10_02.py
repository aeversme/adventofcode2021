from input_handler import convert_input
import repair_handler as rh
from statistics import median

with open('navsyntax.txt') as n:
    nav_raw = n.readlines()

nav_syntax = convert_input(nav_raw)
# print(nav_syntax)


def completion_score(syntax_file):
    # print(f"Number of syntax lines: {len(syntax_file)}")
    incomplete_syntax = rh.find_incomplete_syntax(syntax_file)
    # print(f"Number of incomplete syntax lines: {len(incomplete_syntax)}")
    completion_list = rh.complete_syntax(incomplete_syntax)
    scores_list = rh.score_completion(completion_list)
    return scores_list


scores = completion_score(nav_syntax)
print(f"The middle score is: {median(scores)}")
