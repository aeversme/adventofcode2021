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
