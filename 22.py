first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
third = int(input("Enter the third number: "))

if first != second != third: # checks to see if all are different
    if first > second and first > third:
        print(f"The largest number is {first}.")
    elif second > first and second > third:
        print(f"The largest number is {second}.")
    elif third > first and third > second:
        print(f"The largest number is {third}.")