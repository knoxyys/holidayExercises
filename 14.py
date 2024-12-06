amount = int(input("What is the order amount? "))
state = input("What is the state? ")
tax = 0

if state == 'WI':
    tax = amount * 0.055
    print(f"The subtotal is ${amount:.2f}.")
    print(f"The tax is ${tax:.2f}.")
    
print(f"The total is ${amount + tax:.2f}.")