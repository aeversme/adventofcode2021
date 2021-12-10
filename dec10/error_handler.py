def check_for_errors(syntax_string):
    """
    Takes a string of characters. For each symbol, if it is an opening symbol, adds the associated closing symbol to a
    list of expected symbols. If it is a closing symbol, checks to see if it matches the last symbol in the expected
    symbols list. If so, removes the symbol from the end of the list. If not, returns the incorrect symbol.
    """

    syntax_dict = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    expected_close = []
    for symbol in syntax_string:
        if symbol in syntax_dict.keys():
            expected_close.append(syntax_dict[symbol])
        else:
            if symbol != expected_close[-1]:
                incorrect_close = symbol
                # print(f"Expected '{expected_close[-1]}', but found '{incorrect_close}' instead.")
                return incorrect_close
            else:
                expected_close.pop(-1)
    return None


def score_error(symbol):
    """
    Takes a single character. Returns the integer score associated with that character.
    """

    symbol_scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    return symbol_scores[symbol]
