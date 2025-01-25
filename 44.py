import json

with open('44input.json', mode ='r') as hi:
    data = json.load(hi)
    
while True:
    request = input("What is the product name? ")
    for item in data['products']:
        if item['name'] == request:
            print(f"Name: {item['name']}")
            print(f"Price: ${item['price']:.2f}")
            print(f"Quantity on hand: {item['quantity']}")
            exit()
    else:
        print("Sorry, that product was not found in our inventory.")