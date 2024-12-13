F = float(input("Please type in a temperature : "))
C = (5 / 9) * (F - 32)
print(f"{F} degrees Fahrenheit equals {C} degrees Celsius")
if C < 0:
    print("Brr! It's cold in here!")
