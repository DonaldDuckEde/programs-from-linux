import copy

i = 8
location = "8/ "

while i == 8:
    inputCommand = input(f"{location.strip(' ')}:~$ ")
    
    tempCommand = copy.deepcopy(inputCommand)
    tempCommand1 = copy.deepcopy(inputCommand)
    tempCommand = tempCommand.strip()
    
    mainCommand = tempCommand.split()[0]
    subCommand = tempCommand1.split()[1]
    
    if mainCommand == "cd":
        print(f"{location.strip(' ')}:~$ cd {subCommand}")
    elif mainCommand == "exit":
        break