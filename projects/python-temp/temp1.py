import copy

i = 8
location = "8/ "

while i == 8:
    inputCommand = input(f"{location.strip(' ')}:~$ ")
    
    # copies the input command so it can be used in the rest of the program
    tempCommand = copy.deepcopy(inputCommand)
    tempCommand1 = copy.deepcopy(inputCommand)
    tempCommand = tempCommand.strip()
    
    # splits the input command into the main command and the sub command, so it can be read with the simple if else statement
    mainCommand = tempCommand.split()[0]
    subCommand = tempCommand1.split()[1]
    
    if mainCommand == "cd":
        print(f"{location.strip(' ')}:~$ cd {subCommand}")
    elif mainCommand == "exit":
        break