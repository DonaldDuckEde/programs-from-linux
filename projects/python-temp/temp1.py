import copy

print("This is a terminal")

i = 8

while i == 8:
    location = "8/ "
    inputCommand = input(f"{location.strip(' ')}:~$ ")
    
    tempCommand = copy.deepcopy(inputCommand)
    string_copy = string_copy.strip()
    
    if inputCommand.split():
        