import copy

i = 8
Location = "8/ "

while i == 8:
    inputCommand = input(f"{location.strip(' ')}:~$ ")
    
    tempCommand = copy.deepcopy(inputCommand)
    tempCommand = tempCommand.strip()
    
    mainCommand = tempCommand.split()[0]
    
    if mainCommand == "cd":
        print("cd")
    elif mainCommand == "exit":
        break