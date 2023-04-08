def statement(mainCommand, subCommand, loginKey, loacation):
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
            inputRegister = loginKey