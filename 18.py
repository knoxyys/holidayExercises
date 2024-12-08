letter = input("Press C to convert from Fahrenheit to Celcius. \nPress F to convert from Celcius to Fahrenheit. ")

if letter.upper() == 'C':
    print("Your Choice: C")
    temp = int(input("Please enter the temperature in Fahrenheit: "))
    print(f"The temperature in Celcius is {(temp - 32) * 5/9:.2f}.")
elif letter.upper() == 'F':
    print("your Choice: F")
    temp = int(input("Please enter the temperature in Fahrenheit: "))
    print(f"The temperature in Celcius is {(temp * 9/5) + 32:.2f}.")
else:
    print("huh?")