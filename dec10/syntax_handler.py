def check_syntax(syntax_string):
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
                print(f"Expected '{expected_close[-1]}', but found '{incorrect_close}' instead.")
                return incorrect_close
            else:
                expected_close.pop(-1)
    return None


def score_error(symbol):
    symbol_scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    return symbol_scores[symbol]
