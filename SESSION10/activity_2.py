# Think numbers guessing game

import random

wins = 0
losses = 0
playGame = True

while playGame:
    number = random.randint(1, 10)
    print('I am thinking of a number between 1 and 10')
    guess = int(input('Guess the number: '))

    if guess < number:
        print('Your guess is too low. It was ' + str(number))
        losses += 1
    elif guess > number:
        print('Your guess is too high. It was ' + str(number))
        losses += 1
    else:
        print('That is right! You win')
        wins += 1

    temp = input("Would you like to play again? y/n: ")
    if temp.lower() != 'y':
        playGame = False

print("You won " + str(wins) + " times and lost " + str(losses) + " times")