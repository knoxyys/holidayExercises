with open('45input.txt', mode='r') as hi:
    for line in hi:
        x = line.replace("utilize", "use")

name = input("What should the name of the file be? ")

with open(f'{name}.txt', mode='w') as hello:
    print(x,file=hello)