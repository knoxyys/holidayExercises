import random

name = input("Enter a name: ")
names = []

while name != '':
    names.append(name)
    name = input("Enter a name: ")

winner = random.choice(names)

print(f"The winner is... {winner}.")