import random

print("Let's play guess the number.")

def playGame():
    diff = input('Pick a difficulty level: (1, 2, or 3): ')
    while diff not in ['1', '2', '3']:
        diff = input('Choice needs to be in: (1, 2, or 3): ')
        
    number = random.randint(1, 10 ** int(diff))
    
    count = 1
    
    guess = int(input("I have my number. What's your guess? "))
    while guess != number:
        if guess < number:
            guess = int(input("Too low! Try again: "))
            count = count + 1
        else:
            guess = int(input("Too high! Try again: "))
            count = count + 1

    print(f"You got it in {count} guesses!")
    
    play = ''
    while play not in ['y', 'n']:
        play = input("Play again? ")
        if play == 'y':
            playGame()
        else: break

playGame()