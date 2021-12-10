def check_syntax_strings(syntax_string):
    """
    Takes a string of characters. For each symbol s, if s is an opening symbol, adds the associated closing symbol to a
    list of expected symbols. If s is a closing symbol, checks to see if it matches the last symbol in the expected
    symbols list. If not, returns the incorrect symbol s.

    If s matches the last symbol in the expected symbols list, removes s from the end of the list. If no symbols are
    incorrect in the entire string, reverses the list of expected symbols in place to put them in the correct order
    for 'completing' the string. Returns the reversed list of expected symbols.
    """

    syntax_dict = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    symbols_to_complete = []
    for symbol in syntax_string:
        if symbol in syntax_dict.keys():
            symbols_to_complete.append(syntax_dict[symbol])
        else:
            if symbol != symbols_to_complete[-1]:
                incorrect_close = symbol
                # print(f"Expected '{symbols_to_complete[-1]}', but found '{incorrect_close}' instead.")
                return incorrect_close
            else:
                symbols_to_complete.pop(-1)
    symbols_to_complete.reverse()
    return symbols_to_complete
