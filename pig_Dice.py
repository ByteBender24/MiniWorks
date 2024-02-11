import random

'''
Pig Dice Game Documentation

Overview
Pig is a classic dice game where players take turns rolling a single die to accumulate points. The game continues until one player reaches a predetermined score threshold, typically 100 points.

Rules
Objective: Be the first player to reach or exceed the target score (e.g., 100 points).

Gameplay:
Players take turns rolling a single six-sided die.
On each turn, a player can roll the die multiple times to accumulate points.
If a player rolls a 1, their turn ends, and they lose all points accumulated during that turn.
If a player chooses to end their turn voluntarily (without rolling a 1), they keep all points accumulated during that turn and add them to their total score.

Scoring:
Each roll of the die adds points to the player's current turn score, based on the value rolled (2 to 6).
Rolling a 1 resets the current turn score to zero, and the player's turn ends.

Winning:
The game continues until one player reaches or exceeds the target score.
The first player to reach or exceed the target score wins the game.

Implementation Details
The provided Python script implements the Pig dice game:

It allows 2 to 4 players to participate.
Each player's turn is managed sequentially, with options to roll the die or end their turn.
The game ends when one player reaches the specified maximum score.

Usage
To play the Pig dice game:

Run the Python script.
Enter the number of players (2 to 4).
Follow the on-screen prompts to roll the die or end your turn.
Continue playing until one player wins by reaching the target score.

Note
You can customize the target score, number of players, and other parameters by modifying the script variables accordingly.

'''

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)

            print("Your score is:", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1,
      "is the winner with a score of:", max_score)