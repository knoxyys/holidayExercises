people = int(input("How many people? "))
pizzas = int(input("How many pizzas do you have? "))
slices = int(input("How many slices per pizza? ")) #not shown in example output but in instructions
print(f"{people} people with {pizzas} pizzas")
print(f"Each person should get {int(pizzas * slices / people)} slices of pizza.")
print(f"There are {int(pizzas * slices % people)} leftover pieces. ")