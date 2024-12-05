prin = int(input("What is the principal amount? ")) # this isnt even for time saving purposes its bc i kept misspelling principal :
rate = float(input("What is the rate as a percentage? ")) / 100
years = float(input("What is the number of years? "))
compound = float(input("What is the number of times the interest is compounded per year? "))

total = prin * (1 + (rate / compound)) ** (years * compound)

print(f"{total:.2f}")