while True:
    try:
        rate = int(input("What's the rate of return? "))
        if rate == 0:
            print("this is a different error message. thank you challenge")
        else: break
    except ValueError:
        print("Sorry, that's not a valid input.")

print(f"It will take {72 / rate:.2f} years to double your initial investment.")