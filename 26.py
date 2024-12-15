import math

def monthsCalc(i, b, p):
    value = -(1/30) * (math.log(1 + b / p * (1 - (1 + i) ** 30 )) / (math.log(1 + i)))
    return value


bal = int(input("What is your balance? "))
apr = int(input("What is the APR on the card (as a percent)? "))
month = int(input("What are the monthly payments you can make? "))

daily = apr / (365 * 100)

print(f"It will take you {monthsCalc(daily, bal, month) + 1:.0f} months to pay off this card.") # +1 to always round up