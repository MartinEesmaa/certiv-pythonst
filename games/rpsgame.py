# Rock Paper Scissors (2 players)
# Programmed by Martin Eesmaa (2025)
# License: MIT
# Source code: https://github.com/MartinEesmaa/certiv-pythonst
# Script language version: Python 3
# Filename: rpsgame.py
# Date: 14.10.2025
# Updated: 15.10.2025

"""
This activity requires an algorithmic solution and corresponding script 
implementation for a two-player version of the Rock Paper Scissors game. 

HINT: The game has nine different (9) possibilities.

The solution must:
- Include a welcome message to the game
- Read players names
- Account for all possibilities
- Accept input choices from both players
- Output score (depending on choices)
- Display "Thank you for playing" message
"""

import getpass

def rpsgame():
    print("\nWelcome to Rock, Paper, Scissors game!\n")
    print("Two players mode only.")
    print("Programmed by Martin Eesmaa (2025)\n")
    while True:
        player1 = input("Enter Player 1 name: ").strip()
        if player1:
            break
        print("Player 1 name cannot be empty including spaces. Please enter a valid name.\n")
    while True:
        player2 = input("\nEnter Player 2 name: ").strip()
        if player2:
            break
        print("Player 2 name cannot be empty including spaces. Please enter a valid name.")
    print(f"Hello, {player1} and {player2}! Let's start the game.")
    choices = ['rock', 'paper', 'scissors']
    shorthand = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    score1, score2, tie = 0, 0, 0
    while True:
        try:
            rounds = int(input("Enter number of rounds to play: "))
            if rounds >= 1:
                break
            else:
                print("Number of rounds must be 1 or greater. Please try again.")
        except ValueError:
            print("Invalid input! Please enter only a number of rounds.")
    for round in range(1, rounds + 1):
        print(f"\nRound {round}")
        while True:
            choice1 = getpass.getpass(f"{player1}, enter your choice (rock/paper/scissors or r/p/s): ").lower()
            choice1 = shorthand.get(choice1, choice1)
            if choice1 not in choices:
                print("Invalid choice for Player 1! Please choose rock, paper, or scissors (or r/p/s).")
            else:
                break
        while True:
            choice2 = getpass.getpass(f"{player2}, enter your choice (rock/paper/scissors or r/p/s): ").lower()
            choice2 = shorthand.get(choice2, choice2)
            if choice2 not in choices:
                print("Invalid choice for Player 2! Please choose rock, paper, or scissors (or r/p/s).")
            else:
                break
        if choice1 == choice2:
            print("It's a tie!")
            tie += 1
        elif (choice1 == 'rock' and choice2 == 'scissors') or \
             (choice1 == 'paper' and choice2 == 'rock') or \
             (choice1 == 'scissors' and choice2 == 'paper'):
            print(f"\n{player1} wins this round!")
            score1 += 1
        else:
            print(f"\n{player2} wins this round!")
            score2 += 1
    print(f"\nFinal Score: {player1} {score1} - {player2} {score2}")
    if score1 > score2:
        print(f"Congratulations {player1}, you are the winner!")
    elif score2 > score1:
        print(f"Congratulations {player2}, you are the winner!")
    else:
        print("Well, that is a tie!")
    print(f"Ties count: {tie}")
    print("That is the end of the game.")

while True:
    rpsgame()
    while True:
        play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()
        if play_again == 'yes':
            break
        elif play_again == 'no':
            print("\nThank you for playing!")
            exit()
        else:
            print("Invalid input. Please type 'yes' or 'no'.")