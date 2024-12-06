try:
    w = int(input("What is your weight? "))
    g = input("What is your gender? ")
    a = int(input("What is the amount of alchohol consumed in oz? "))
    h = int(input("When was the last time you drunk? "))
except ValueError or NameError:
    print("enter the correct values please :(")

g = g.lower()
if g == 'man' or 'male':
    r = 0.73
elif g == 'woman' or 'female':
    r = 0.66

bac = (a * 5.14 / w * r) - 0.015 * h

print(f"Your BAC is {bac:.3f}") # rounded to 3dp for simplicity
if bac > 0.07:
    print("It is not legal for you to drive.")
else:
    print("It is legal for you to drive.")