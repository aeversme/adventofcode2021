from error_handler import check_for_errors


def find_incomplete_syntax(syntax_file):
    """
    Takes a list of syntax strings. Checks each string for errors. If no errors, the string is considered correct but
    'incomplete' and is added to a list of 'incomplete' strings. Returns the list of 'incomplete' strings.
    """

    incomplete_syntax = []
    for syntax in syntax_file:
        if check_for_errors(syntax) is None:
            incomplete_syntax.append(syntax)
    return incomplete_syntax


def complete_syntax(incomplete_syntax_list):
    """
    Takes a list of strings. For each string, determines if each symbol is an opening symbol. If so,
    adds the associated closing symbol to a list of expected closing symbols. If not, removes the symbol from the end
    of the expected symbols list.

    Reverses the list of expected symbols to create a list of symbols needed to 'complete' the string. Adds that list
    to a container list.

    Returns the container list.
    """

    completion_list = []
    syntax_dict = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    for syntax_string in incomplete_syntax_list:
        symbols_to_complete = []
        for symbol in syntax_string:
            if symbol in syntax_dict.keys():
                symbols_to_complete.append(syntax_dict[symbol])
            else:
                if symbol == symbols_to_complete[-1]:
                    symbols_to_complete.pop(-1)
                else:
                    print("There's been an error...")
        symbols_to_complete.reverse()
        completion_list.append(symbols_to_complete)
    return completion_list


def score_completion(completion_list):
    """
    Takes a list of lists of characters. For each list of characters, manipulates a score based on each character and
    adds the total score to a list of scores. Returns the list of scores.
    """

    symbol_scores = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    completion_scores = []
    for completion in completion_list:
        score = 0
        for symbol in completion:
            score *= 5
            score += symbol_scores[symbol]
        completion_scores.append(score)
    return completion_scores
