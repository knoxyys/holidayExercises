import time
import random

def validIntInput(x): # stealing same function from before bc its useful
    while True:
        try:
            return int(input(x))
        except ValueError:
            continue

def game():
    diff = validIntInput("Let's play guess the number.\nPick a difficulty level (1, 2 or 3): ")
    if diff > 3:
        time.sleep(99999999) # lol

    number = random.randint(0, 10 ** diff)

    counter = 1
    guess = int(input("I have your number. What's your guess? "))
    while guess != number:
        if guess > number:
            guess = int(input("Too high. Guess again: "))
            counter = counter + 1
        else:
            guess = int(input("Too low. Guess again: "))
            counter = counter + 1

    print(f"The number was {number}. You got it in {counter} guesses!")

while True:
    game()
    while True:
        play = input("Play again? ")
        if play == 'y':
            break
        elif play == 'n':
            print("Goodbye! ")
            quit()