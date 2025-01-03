numbers = input("Enter a list of numbers, separated by spaces: ")
numlist = numbers.split(" ")
evenlist = []

for i in numlist:
    if int(i) % 2 == 0:
        evenlist.append(i) # it does say to use a function but this seems way easier
        
print("The even numbers are:", *evenlist, sep = ' ')