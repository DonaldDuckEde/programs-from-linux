import copy

i = 8
location = "8/ "

while i == 8:
    inputCommand = input(f"{location.strip(' ')}:~$ ")
    
    tempCommand = copy.deepcopy(inputCommand)
    tempCommand = tempCommand.strip()
    
    mainCommand = tempCommand.split()[0]
    subCommand = tempCommand.split()[1]
    
    if mainCommand == "cd":
        
    elif mainCommand == "exit":
        break