while True:
    w = input("What is your weight in pounds? ")
    try:
        w = int(w)
        break
    except ValueError:
        continue

while True:
    h = input("What is your height in inches? ")
    try:
        h = int(h)
        break
    except ValueError:
        continue

bmi = (w / h ** 2) * 703 # idk if this is actually accurate but its whatever the formula they gave us soo
print(f"Your BMI is {bmi:.2f}.")

if bmi < 18.5 and bmi > 25:
    print("You are within the ideal weight range.")
elif bmi < 18.5:
    print("You are underweight. You should see your doctor.")
else:
    print("You are overweight. You should see your doctor.")