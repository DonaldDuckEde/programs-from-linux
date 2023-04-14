path = "o/,project/,"
sudoPower = False


while True:
    command = input(f"{path}$ ")
    if command == "sudo":
        inputSudoPass = input("sudo: ")
        if inputSudoPass == sudoPass:
            sudoPower = True
        else:
            print("Please enter a valid sudo key: ")
    elif command == "keys":
        print("welcome to the key environment.")
        changeKey = input("Key to change:")
        if changeKey == "sudo":
            newSudoPass = input("Sudo key: ")