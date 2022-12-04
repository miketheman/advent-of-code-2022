"""https://adventofcode.com/2022/day/2"""
from pathlib import Path

PLAYER_1_OPTIONS = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
}

PLAYER_2_OPTIONS = {
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}

PLAY_OUTCOMES_WIN_LOSE = {
    "Rock": "Scissors",
    "Paper": "Rock",
    "Scissors": "Paper",
}

PLAY_OPTION_SCORE = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3,
}

PLAY_OUTCOME_SCORE = {
    "Lose": 0,
    "Draw": 3,
    "Win": 6,
}

# Strategy Guide input located relative to this file using Path
strategy_guide_input = Path(__file__).parent / "input.txt"

# Read guide into a list line by line, split on whitespace into tuples
with strategy_guide_input.open() as f:
    play_rounds = [tuple(line.strip().split()) for line in f]
    # Each `play_round` is a tuple of (opponent, self) play options


def play_round(player_1: str, player_2: str) -> tuple[str, int]:
    """Play a round of Rock, Paper, Scissors, determine outcome and score"""
    player_1_option = PLAYER_1_OPTIONS[player_1]
    player_2_option = PLAYER_2_OPTIONS[player_2]

    if player_1_option == player_2_option:
        outcome = "Draw"
        score = PLAY_OUTCOME_SCORE[outcome] + PLAY_OPTION_SCORE[player_2_option]
    elif PLAY_OUTCOMES_WIN_LOSE[player_1_option] == player_2_option:
        outcome = "Lose"
        score = PLAY_OUTCOME_SCORE[outcome] + PLAY_OPTION_SCORE[player_2_option]
    else:
        outcome = "Win"
        score = PLAY_OUTCOME_SCORE[outcome] + PLAY_OPTION_SCORE[player_2_option]

    return outcome, score


# Test cases for rules and score
assert play_round("A", "Y") == ("Win", 8)
assert play_round("B", "X") == ("Lose", 1)
assert play_round("C", "Z") == ("Draw", 6)


# Play all rounds and sub up score
score = sum(play_round(*play_rounds)[1] for play_rounds in play_rounds)

print(f"Part 1 Score: {score}")

# Part 2 - the assumptions have changed!

ROUND_OUTCOME_MAP = {
    "X": "Lose",
    "Y": "Draw",
    "Z": "Win",
}


def find_player_2_option(player_1_option: str, outcome: str) -> str:
    """Find the player 2 option that would have resulted in the given outcome"""
    player_2_option = PLAY_OUTCOMES_WIN_LOSE[player_1_option]
    if outcome == "Lose":
        return player_2_option
    elif outcome == "Draw":
        return player_1_option
    elif outcome == "Win":
        return PLAY_OUTCOMES_WIN_LOSE[player_2_option]
    else:
        raise ValueError(f"Invalid outcome: {outcome}")


# Test cases for finding player 2 option
assert find_player_2_option("Rock", "Draw") == "Rock"
assert find_player_2_option("Paper", "Lose") == "Rock"
assert find_player_2_option("Scissors", "Win") == "Rock"

# We need a slightly different `play_round` for the new assumptions
def play_round_with_outcome(player_1: str, outcome: str) -> int:
    """Play a round of Rock, Paper, Scissors, with a known outcome and score"""
    player_1_option = PLAYER_1_OPTIONS[player_1]
    player_2_option = find_player_2_option(PLAYER_1_OPTIONS[player_1], outcome)

    if outcome == "Draw":
        score = PLAY_OUTCOME_SCORE[outcome] + PLAY_OPTION_SCORE[player_2_option]
    elif outcome == "Lose":
        score = PLAY_OUTCOME_SCORE[outcome] + PLAY_OPTION_SCORE[player_2_option]
    else:
        # outcome = "Win"
        score = PLAY_OUTCOME_SCORE[outcome] + PLAY_OPTION_SCORE[player_2_option]

    return score


# Play all rounds and sum up score
score = sum(
    play_round_with_outcome(
        player_1,
        ROUND_OUTCOME_MAP[outcome],
    )
    for player_1, outcome in play_rounds
)

print(f"Part 2 Score: {score}")
