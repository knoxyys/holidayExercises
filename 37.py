import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
special = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
password = []

length = int(input("What's the minimum length? "))
spec = int(input("How many special characters? "))
numbers = int(input("How many numbers? "))

for i in range(length - spec - numbers):
    password.append(random.choice(letters))
for i in range(spec):
    password.append(random.choice(special))
for i in range(numbers):
    password.append(random.randint(0, 9))

random.shuffle(password)
print("Your password is: ", *password, sep = '')