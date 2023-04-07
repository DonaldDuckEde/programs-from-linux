tempString = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

tempString = tempString.lower()

if tempString == "42" or "forty-two" or "forty two":
    print("Yes")
else:
    print("No")