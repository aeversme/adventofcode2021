from input_handler import convert_input
from player_handler import Player

with open('dirac.txt') as d:
    start_raw = d.readlines()


def deterministic_die_roll(last_roll):
    if last_roll == 0 or last_roll == 100:
        roll = 1
    else:
        roll = last_roll + 1
    return roll


def game_turn(player, players, last_roll, roll_count):
    roll = [deterministic_die_roll(last_roll + i) for i in range(3)]
    roll_count += 3
    roll_sum = sum(roll)
    player.space = (player.space + roll_sum) % 10

    if player.space == 0:
        player.score += 10
    else:
        player.score += player.space

    if player == players[0]:
        next_player = players[1]
    else:
        next_player = players[0]
    return roll[2], next_player, roll_count


def dirac_game(data):
    player_list = convert_input(data)
    players = [Player(player[0], player[1]) for player in player_list]

    next_player = players[0]
    last_roll = 0
    roll_count = 0

    while players[0].score < 1000 and players[1].score < 1000:
        last_roll, next_player, roll_count = game_turn(next_player, players, last_roll, roll_count)

    losing_score = min([player.score for player in players])
    return losing_score, roll_count


score, count = dirac_game(start_raw)
print(f"Losing score times roll count: {score * count}")
