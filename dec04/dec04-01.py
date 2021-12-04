with open('bingo.txt') as b:
    bingo = b.readlines()


def convert_bingo_input():
    bingo_strip = [i.strip('\n') for i in bingo]
    draw = bingo_strip.pop(0).split(',')
    draw = [int(i) for i in draw]
    bingo_strip = bingo_strip[1:]
    bingo_drop = [i for i in bingo_strip if i != '']
    return draw, bingo_drop


def make_bingo_cards(bingo_input):
    card_list = []
    index = 0
    for i in range(int(len(bingo_input) / 5)):
        card = []
        for j in range(5):
            row = bingo_input[index + j].lstrip().replace('  ', ' ').split(' ')
            card.append([int(k) for k in row])
        card_list.append(card)
        index += 5
    return card_list


def squid_bingo():
    draw, card_strings = convert_bingo_input()
    cards = make_bingo_cards(card_strings)
    print(draw)
    print(cards[0])


squid_bingo()
