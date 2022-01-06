from input_handler import convert_input
from player_handler import Player

with open('test-dirac.txt') as d:
    start_raw = d.readlines()


def move_and_score(player, roll):
    player.space = (player.space + roll) % 10

    if player.space == 0:
        score = 10
    else:
        score = player.space

    player.score += score

    return score


def is_game_over(players):
    game_over = False
    for i in range(2):
        if players[i].score >= 21:
            print(f"+++ {players[i].name} wins in this universe.")
            players[i].victories += 1
            game_over = True
    return game_over


# TODO: need to have scores roll back as recursion moves back down the stack
def game_turn(player, players):
    print(f"New turn, current player: {player.name}")
    print(f"    {players[0]}")
    print(f"    {players[1]}")
    for num in range(1, 4):
        print(f"Roll: {num}")
        score = move_and_score(player, num)
        print(f"Result: {player}")
        if is_game_over(players):
            return
        else:
            if player == players[0]:
                next_player = players[1]
            else:
                next_player = players[0]
        game_turn(next_player, players)
        player.score -= score
    return


def dirac_game(data):
    player_list = convert_input(data)
    players = [Player(player[0], player[1]) for player in player_list]

    game_turn(players[0], players)

    print(f"{players[0].name} has victories in {players[0].victories} universes.")
    print(f"{players[1].name} has victories in {players[1].victories} universes.")

    winning_player = None
    victories = 0
    for player in players:
        if player.victories > victories:
            winning_player = player
            victories = player.victories

    return winning_player, victories


winner, wins = dirac_game(start_raw)
print(f"{winner.name} wins with victories in {wins} universes.")
