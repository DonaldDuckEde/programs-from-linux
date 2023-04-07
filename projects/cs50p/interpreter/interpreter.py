som = input()

x, y, z = som.split(" ")

x = float(x)
z = float(z)

if y == "/":
    x / z = tempInt
    print(f"{x} {y} {z} = {tempInt}")
elif y == "*":
    x * z = tempInt
    print(f"{x} {y} {z} = {tempInt}")
elif y == "+":
    x + z = tempInt
    print(f"{x} {y} {z} = {tempInt}")
elif y == "-":
    x - z = tempInt
    print(f"{x} {y} {z} = {tempInt}")
else:
    print("Please enter a valid input.")