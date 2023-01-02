"""
Advent of Code Day 2
Puzzle 1: Score of Rock-Paper-Scissors strategy:
    Given a strategy guide of the opponents choice and your choice, find your
    score based on what you chose and whether you won, drew, or tied each game.
Puzzle 2: Score with different rules
    Given a strategy guide of the opponents choice and the outcome of a game,
    find your score based on what you chose and whether you won, drew, or tied
    each game.
"""


def calc_score(strategy: list[list[str]]) -> int:
    """
    a,x = rock
    b,y = paper
    c,z = scissors
    :param strategy: A list of matches (tuples) where the first item is the opponents choice
    and the second item is your choice
    :return: the combined score of all matches, where a win awards 6 points, a draw awards 3, a loss awards 0, and rock, paper, and scissors award
    1,2, and 3 points respectively
    """
    score = 0
    win_match = [["A", "Y"], ["B", "Z"], ["C", "X"]]
    lose_match = [["A", "Z"], ["B", "X"], ["C", "Y"]]
    draw_match = [["A", "X"], ["B", "Y"], ["C", "Z"]]
    for game in strategy:
        if game in win_match:
            score += 6
        elif game in draw_match:
            score += 3
        if game[1] == "X":
            score += 1
        elif game[1] == "Y":
            score += 2
        else:
            score += 3

    return score

def calc_score2(outcome: list[list[str]]) -> int:
    """
    a = rocks
    b = paper
    c = scissors

    x = lose
    y = draw
    z = win

    :param outcome: A list of matches (tuples) where the first item is the opponents choice
    and the second item is the outcome of the match, ie win, lose, or draw
    :return: the combined score of all matches, where a win awards 6 points, a draw awards 3, a loss awards 0, and rock, paper, and scissors award
    1,2, and 3 points respectively
    """
    score = 0
    winning_choice  = {"A":2,"B":3,"C":1}
    losing_choice = {"A":3,"B":1,"C":2}
    draw_choice = {"A":1,"B":2,"C":3}

    for game in outcome:
        if game[1] == "X":
            score += losing_choice[game[0]]
        elif game[1] == "Y":
            score += 3 + draw_choice[game[0]]
        else:
            score += 6 + winning_choice[game[0]]

    return score


if __name__ == "__main__":
    mode = input("Press 1 for Puzzle 1 solver, press 2 for Puzzle 2 solver:\n")
    if mode == "1":
        match = []
        match_list = []
        with open(input("List of matches:")) as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        match.append(char)
                match_list.append(match)
                match = []
        print(match_list)
        print("Your total score for this set of games is {}.".format(
            calc_score(match_list)))

    elif mode == "2":
        match = []
        match_list = []
        with open(input("List of matches:")) as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        match.append(char)
                match_list.append(match)
                match = []
        print(match_list)
        print("Your total score for this set of games is {}.".format(
            calc_score2(match_list)))
