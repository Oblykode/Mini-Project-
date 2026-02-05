# Pig – The Dice Game

A simple console-based version of the classic dice game **Pig** written in Python.

Players take turns rolling a six-sided die. The goal is to be the first to reach **50 points**.

## Rules (as implemented)

- Each turn, a player can roll the die as many times as they want.
- Each roll adds the rolled number to the **turn score**.
- If the player rolls a **1**, they lose all points gained this turn and their turn ends.
- If the player chooses to stop (by entering 'n'), their turn score is added to their **total score**.
- The first player to reach or exceed **50 points** wins.

## Features

- Supports **2 to 4 players**
- Clear turn-by-turn feedback
- Input validation for number of players
- Simple human vs human gameplay

## How to Play

1. Run the script:

```bash
python pig_game.py

Enter the number of players (2–4)
On your turn:
Type y to roll
Type n to hold (bank your points)

First to 50+ points wins!

Example Gameplay
textEnter the number of players you want (2 - 4): 2

Player 1 turn has just started.
Your total score is: 0
Do you want to roll? (y/n): y
You rolled: 4
Your current turn score is: 4
Do you want to roll? (y/n): y
You rolled: 6
Your current turn score is: 10
Do you want to roll? (y/n): n

Player 1 total score is now: 10

Player 2 turn has just started.
...
Code Overview

roll() → returns a random number 1–6
Input validation for number of players
Main loop continues until someone reaches 50
Each turn allows multiple rolls until 1 is rolled or player holds

How to Customize
You can easily change these:
Pythontarget_score = 100          # instead of 50
min_value = 1
max_value = 6
Requirements
Just Python 3 (uses only random module — no external libraries needed)
Have fun playing!
