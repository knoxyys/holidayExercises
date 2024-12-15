while True:
    try:
        x = int(input("How many loops? "))
        break
    except ValueError:
        print("invalid")

total = 0

for i in range(x):
    try:
        number = int(input("Enter a number: "))
        total = total + number
    except ValueError:
        continue
print(f"The total is {total}.")

# create a flowchart before writing the program ?!?!?! ok man