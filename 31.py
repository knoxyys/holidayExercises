# would be so easy to do blah blah blah import pandas import prettytable but NO

def validInput(x): # ooo look a function for it now how fancy
    while True:
        try:
            return int(input(x))
        except ValueError:
            continue

age = validInput("Enter age: ")
rest = validInput("Enter resting heartbeat: ")

def target(x):
    x = (((220 - age) - rest) * (i / 100)) + rest
    return x

print(f"\nResting Pulse: {rest}         Age: {age}\n") # makes table stuff
print("Intensity   | Rate")
print("------------|-----------")

for i in range(55, 96, 5):
    print(f"{i}%         | {target(i):.0f} bpm")