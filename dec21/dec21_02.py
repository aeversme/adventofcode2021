from input_handler import convert_input
from player_handler import Player

with open('test-dirac.txt') as d:
    start_raw = d.readlines()


def game_turn(player_index, players, score_p1, score_p2, space_p1, space_p2, stack_level):
    player = players[player_index]
    scores = [score_p1, score_p2]
    spaces = [space_p1, space_p2]
    print(" . " * stack_level + f"Turn: {player_index}; 0 has {scores[0]} points on {spaces[0]}; 1 has {scores[1]} "
                                f"points on {spaces[1]}")
    for roll in range(1, 4):
        print(" . " * stack_level + f"{player_index} rolls {roll}...")
        spaces[player_index] = (spaces[player_index] + roll) % 10
        score = spaces[player_index] + 1
        scores[player_index] += score
        print(" . " * stack_level + f"{player_index} moves to {spaces[player_index]}; new score: "
                                    f"{scores[player_index]}")

        if max(scores) < 21:
            player_index = (player_index + 1) % 2
            game_turn(player_index, players, scores[0], scores[1], spaces[0], spaces[1], stack_level + 1)
        else:
            print(" . " * stack_level + f"*** Winner index {player_index} with {scores[player_index]} on "
                                        f"{spaces[player_index]}")
            player.victories += 1
            scores = [score_p1, score_p2]
            spaces = [space_p1, space_p2]
    return


def dirac_game(data):
    player_list = convert_input(data)
    players = [Player(player[0], player[1]) for player in player_list]

    game_turn(0, players, 0, 0, 3, 7, 0)

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
