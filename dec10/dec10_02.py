from input_handler import convert_input
from string_handler import check_syntax_string
from score_handler import score_completion
from statistics import median

with open('navsyntax.txt') as n:
    nav_raw = n.readlines()

nav_syntax = convert_input(nav_raw)
# print(nav_syntax)


def completion_score(syntax_file):
    # print(f"Number of syntax lines: {len(syntax_file)}")
    completion_list = []
    for syntax in syntax_file:
        check_result = check_syntax_string(syntax)
        if isinstance(check_result, list):
            completion_list.append(check_result)
    # print(f"Number of incomplete syntax lines: {len(completion_list)}")
    scores_list = score_completion(completion_list)
    return scores_list


scores = completion_score(nav_syntax)
print(f"The middle score is: {median(scores)}")
