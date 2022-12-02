from utils.read import file

player_one = {"A": 1, "B": 2, "C": 3}
player_two = {"X": 1, "Y": 2, "Z": 3}
loss = 0
win = 6
draw = 3


def rock_paper_scissors():
    string_input = file(2, "string")
    player_one_input = []
    player_two_input = []
    for line in string_input:
        line = line.split(" ")
        player_one_input.append(line[0])
        player_two_input.append(line[1])
    return player_one_input, player_two_input


def part_one():
    score_player_one = 0
    score_player_two = 0
    inputs_player_one, inputs_player_two = rock_paper_scissors()
    for x, y in zip(inputs_player_one, inputs_player_two):
        one = player_one[x]
        two = player_two[y]

        score_player_one += one
        score_player_two += two

        if one == two:
            score_player_one += draw
            score_player_two += draw
        if (one == 1 and two == 2) or (one == 2 and two == 3) or (one == 3 and two == 1):
            score_player_one += loss
            score_player_two += win
        if (two == 1 and one == 2) or (two == 2 and one == 3) or (two == 3 and one == 1):
            score_player_one += win
            score_player_two += loss

    print(f"According to the strategy guide, your score would be **{score_player_two}**.")
