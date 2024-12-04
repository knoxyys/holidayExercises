euros = int(input("How many euros are you exchanging? "))
rate = float(input("What are 100 euros currently worth in USD? "))

usd = euros * (rate / 100)

print(f"{euros} euros at an exchange rate of 100 to {rate} is {usd:.2f} U.S. dollars.") # it does say rounded up but the example output doesnt sooo