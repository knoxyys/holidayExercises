prin = int(input("Enter the principal: "))
rate = float(input("Enter the rate of interest as a percentage: "))
years = float(input("Enter the number of years: "))

print(f"After {years} years at {rate}%, the investment will be worth ${prin + (prin * (rate / 100 * years)):.2f}.")