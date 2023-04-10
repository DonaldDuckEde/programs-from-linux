import copy

i = 8
location = "8/ "
loginKey = "terminal"
# Try to make a function that looks what wrong and gives the right error message
errors = {
    "value": "Value error, enter valid input",
    "internal": "Internal error, try again",
    "error": "Error",
    "not_found": "Not found",
    "invalid": "Invalid input",
    "no-acces": "No Acces granted",
}

while i == 8:
    inputCommand = input(f"{location.strip(' ')}:~$ ")
    
    # copies the input command so it can be used in the rest of the program
    tempCommand = copy.deepcopy(inputCommand)
    tempCommand1 = copy.deepcopy(inputCommand)
    tempCommand = tempCommand.strip()
    
    # splits the input command into the main command and the sub command, so it can be read with the simple if else statement
    mainCommand = tempCommand.split()[0]
    # subCommand = tempCommand1.split()[1]
    
    if mainCommand == "cd":
            print("cd")
    elif mainCommand == "exit":
            print("exit...")
    elif mainCommand == "mkdir":
            print("mkdir")
    elif mainCommand == "login":
        inputLoginKey = input("login key: ")
        if inputLoginKey == loginKey:
            print("loging in...")
            if loginKey == "terminal":
                print("Please change your login key")
        else:
            print("wrong login key")
    elif mainCommand == "register":
        inputRegister = input("register: ")
        if inputRegister != "":
            print(f"new password: {inputRegister}")
            loginKey = inputRegister
        else:
            print(errors["invalid"])