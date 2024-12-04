price1 = int(input("Enter the price of item 1: "))
quantity1 = int(input("Enter the quantity of item 1: "))
price2 = int(input("Enter the price of item 2: "))
quantity2 = int(input("Enter the quantity of item 2: "))
price3 = int(input("Enter the price of item 3: "))
quantity3 = int(input("Enter the quantity of item 3: "))

total1 = price1 * quantity1
total2 = price2 * quantity2
total3 = price3 * quantity3   
total = total1 + total2 + total3
tax = total * 0.055

print(f"Subtotal: ${total:.2f}") # :.2f is very handy for forcing 2dp
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total + tax:.2f}")