path = "o/,project/,"
sudoPower = False
sudoPass = "terminal"
warnStrikes = 0

def strikes(strikes):
    warnStrikes += 1
    if warnStrikes == 3:
        print("You have to much false uses please restart the evenirement.")
        exit(0)

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
            if newSudoPass != sudoPass:
                newSudoPass = sudoPass
            else:
                strikes(warnStrikes)