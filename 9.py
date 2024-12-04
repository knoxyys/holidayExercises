length = int(input("What is the length of the ceiling in feet? "))
width = int(input("What is the width of the ceiling in feet? "))
# if roof is length * width
print(f"You will need to purchase {int(length * width / 350) + 1} gallons of paint to cover {length * width} square feet.")