a = input("Is the car silent when you turn the key? ")
if a == 'y':
    b = input("Are the battery terminals corroded? ")
    if b == 'y': print("Clean terminals and try starting again.")
    elif b == 'n': print("Replace cables and try again.")
elif a == 'n':
    b = input("Does the car make a clicking noise? ")
    if b == 'y': print("Replace the battery.")
    elif b == 'n':
        c = input("Does the car crank up but fail to start? ")
        if c == 'y': print("Check spark plug connections.")
        elif c == 'n':
            d = input("Does the engine start and then die?")
            if d == 'y':
                e = input("Does your car have fuel injection?")
                if e == 'y': print("Get it in for service.")
                elif e == 'n': print("Check to ensure the choke is opening and closing.")