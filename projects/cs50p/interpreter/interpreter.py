som = input()

x, y, z = som.split(" ")

x = float(x)
z = float(z)

tempInt = 0

if y == "/":
    print(x / y)
elif y == "*":
    print(x * y)
elif y == "+":
    print(x + y)
elif y == "-":
    print(x - y)
else:
    print("Please enter a valid input.")