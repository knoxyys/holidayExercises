amount = int(input("What is the order amount? "))
state = input("What state do you live in? ")
if state == 'Illinois':
    tax = 0.08
elif state == 'Wisconsin':
    county = input("What county do you live in? ")
    if county == 'Eau Claire':
        tax = 0.005
    elif county == 'Dunn': # i think this is right? it looks weird but the question didnt specify any overarching winconsin tax
        tax = 0.004

if tax != 0:
    print(f"The tax is ${amount * tax:.2f}.\nThe total is ${amount * (tax + 1):.2f}.")
else:
    print(f"The total is ${amount * (tax + 1):.2f}.") # i think this is what it meant by use only one print statement to print the output? couldnt think of a better way to do it