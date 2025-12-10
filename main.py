import random

def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

# Ask for number of players
while True:
    players = input("Enter the number of players you want (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Please enter a number between 2 and 4.")
    else:
        print("Please enter a valid number.")

target_score = 50
players_score = [0 for _ in range(players)]

# Main game loop
while max(players_score) < target_score:
    for i in range(players):
        print("\nPlayer", i + 1, "turn has just started.")
        print("Your total score is:", players_score[i])
        current_score = 0

        while True:
            should_roll = input("Do you want to roll? (y/n): ")
            if should_roll.lower() != "y":
                break

            value = roll()
            print("You rolled:", value)

            if value == 1:
                print("You rolled a 1. Your turn is over and you gain 0 points this turn.")
                current_score = 0
                break
            else:
                current_score += value
                print("Your current turn score is:", current_score)

        players_score[i] += current_score
        print("Player", i + 1, "total score is now:", players_score[i])

        # If this player has reached or passed the target, end the game
        if players_score[i] >= target_score:
            break

# Determine winner
winning_score = max(players_score)
winning_idx = players_score.index(winning_score)
print("\nPlayer number", winning_idx + 1, "is the winner with a score of:", winning_score)
