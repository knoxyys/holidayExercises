months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
number = int(input("Please enter the number of the month: "))

if number < 13:
    print(f"The name of the month is {months[number - 1]}")
else: print("Input not valid")