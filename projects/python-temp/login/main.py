path = "o/,project/,"

while True:
    command = input(f"{path}$ ")
    if command == "sudo":
        inputSudoPass = input("sudo: ")