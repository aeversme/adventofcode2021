# Advent of Code 2021
# December 04, part 1

with open('bingo.txt') as b:
    bingo = b.readlines()


def convert_bingo_input():
    """
    Transforms input text. Returns an array of draw numbers and an array of string arrays.
    """
    bingo_strip = [i.strip('\n') for i in bingo]
    draw = bingo_strip.pop(0).split(',')
    draw = [int(i) for i in draw]
    bingo_strip = bingo_strip[1:]
    bingo_drop = [i for i in bingo_strip if i != '']
    return draw, bingo_drop


def make_bingo_cards(bingo_input):
    """
    Takes an array of string arrays. Returns an array of bingo cards. Each card is an array of five integer arrays,
    each containing 5 integers.
    """
    card_list = []
    index = 0
    for i in range(int(len(bingo_input) // 5)):
        card = []
        for j in range(5):
            row = bingo_input[index + j].lstrip().replace('  ', ' ').split(' ')
            card.append([int(k) for k in row])
        card_list.append(card)
        index += 5
    return card_list


def look_for_number(draw, cards):
    """
    Takes a draw number and an array of cards. Loops through every element of every card and replaces any instance of
    the draw number with -1.
    """
    for card in range(len(cards)):
        for row in range(len(cards[0])):
            for element in range(len(cards[0][0])):
                if cards[card][row][element] == draw:
                    cards[card][row][element] = -1


def look_for_bingo(cards):
    """
    Takes an array of cards. Loops through each card. If all elements of one row or one column are -1, returns that
    card.
    """
    for card in range(len(cards)):
        for row in range(5):
            is_bingo = True
            for element in range(5):
                if cards[card][row][element] != -1:
                    is_bingo = False
            if is_bingo:
                return cards[card]
        for column in range(5):
            is_bingo = True
            for element in range(5):
                if cards[card][element][column] != -1:
                    is_bingo = False
            if is_bingo:
                return cards[card]
    return None


def score_winning_card(card, winning_number):
    """
    Takes a card and a winning number. Returns the score of the card.
    """
    unmarked_sum = 0
    for row in range(5):
        for element in range(5):
            if card[row][element] != -1:
                unmarked_sum += card[row][element]
    return unmarked_sum * winning_number


def squid_bingo():
    draw, card_strings = convert_bingo_input()
    cards = make_bingo_cards(card_strings)
    print(draw)
    print(cards[0])

    winner = False
    number_of_draws = 1
    while not winner:
        draw_number = draw[number_of_draws - 1]
        print(f"draw_number: {number_of_draws}, number: {draw_number}")
        look_for_number(draw_number, cards)
        number_of_draws += 1
        if 5 < number_of_draws <= len(draw):
            result = look_for_bingo(cards)
            if result is not None:
                winner = True
                print("Game over, there's a winning card!")
                print(f"Winning number: {draw_number}")
                print(f"Winning card:\n{result}")
                score = score_winning_card(result, draw_number)
                print(f"The winning card's score is: {score}")
            else:
                print("No winner yet.")
                continue
        elif number_of_draws > len(draw):
            print("All numbers called, no winner.")
            break
        else:
            print("Not enough draws to have a bingo yet.")
            continue


squid_bingo()
