import math

times = []
response = ''

while response != 'done':
    response = input("Enter a number: ")
    try:
        times.append(int(response))
    except ValueError:
        continue

print(f"Numbers: {times}")

total = 0
lower = times[0]
upper = times[0]

for i in times:
    total += i
    if i < lower:
        lower = i
    if i > upper:
        upper = i

mean = total / len(times)

staTotal = 0
staCount = 0
for i in times: # has to be in different loop as it uses total which is only calculated once the other loop ends
    diff = (i - mean) ** 2
    staTotal = staTotal + diff
deviation = math.sqrt(staTotal / len(times)) # square root of the mean


print(f"The average is = {mean}.")
print(f"The minimum is {lower}.")
print(f"The maximum is {upper}.")
print(f"The standard deviation is {deviation}.") # when trying the example i got a different result for the deviation but i couldnt figure out what i did wrong and chatgpt said i was right so idk