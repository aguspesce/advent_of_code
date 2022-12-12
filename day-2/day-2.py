"""
Script to solve the 2nd Day
"""

import numpy.testing as npt

# task 1
# A - rock, B - paper, C - scissors
# X - rock, Y - paper, Z - scissors
# X - 1, Y - 2, Z - 3
score_task_1 = {"X": 1, "Y": 2, "Z": 3}
game_score_task_1 = {
    "A X": 3,
    "A Y": 6,
    "A Z": 0,
    "B X": 0,
    "B Y": 3,
    "B Z": 6,
    "C X": 6,
    "C Y": 0,
    "C Z": 3,
}


# task 2
# A - rock, B - paper, C - scissors
# X - lose, Y - draw, Z - win
# X - 0, Y - 2, Z - 3
score_task_2 = {"X": 0, "Y": 3, "Z": 6}
game_score_task_2 = {
    "A X": 3,
    "A Y": 1,
    "A Z": 2,
    "B X": 1,
    "B Y": 2,
    "B Z": 3,
    "C X": 2,
    "C Y": 3,
    "C Z": 1,
}


def game(fname, score_task, game_score):
    """
    Return a float with the total score for several rounds.
    """
    # Read the files with the different rounds
    lines = _read_input(fname)
    # Initialize a list to store the score for each round
    scores = []
    # Calculate the score for each rounds
    for line in lines:
        scores.append(_score(score_task, game_score, line))
    return sum(scores)


def _read_input(fname):
    """
    Read the file and split the lines.

    Return a list where its elements are strings.
    """
    lines = open(fname, "r").read().splitlines()
    return lines


def _score(score_task, game_score, line):
    """
    Calculate the round score.

    Return a float.
    """
    # Sum the score_task and the game_score
    return score_task[line[2]] + game_score[line]


def test_score():
    """
    Check the score function
    """
    expected_score_1 = [8]
    expected_score_2 = [4]
    game_round = ["A Y"]
    # Calculate the score for the different game strategies
    score_1 = _score(score_task_1, game_score_task_1, game_round[0])
    score_2 = _score(score_task_2, game_score_task_2, game_round[0])
    # Compare with the expected results
    npt.assert_allclose(score_1, expected_score_1)
    npt.assert_allclose(score_2, expected_score_2)


def test_game():
    """
    Check the game function
    """
    expected_score_1 = [8, 1, 6]
    expected_score_2 = [4, 1, 7]
    # Compare the score obtained for a game with the expected result
    npt.assert_allclose(
        game("test_input", score_task_1, game_score_task_1), expected_score_1
    )
    npt.assert_allclose(
        game("test_input", score_task_2, game_score_task_2), expected_score_2
    )


if __name__ == "__main__":

    # Solve first part
    your_total_score_1 = game("input", score_task_1, game_score_task_1)

    # Solve second part
    your_score_2 = game("input_2", score_task_2, game_score_task_2)

    print(
        "Answerers:",
        "\n",
        "- First part: ",
        f"{your_total_score_1}",
        "\n",
        "- Second part: ",
        f"{your_score_2}",
    )
