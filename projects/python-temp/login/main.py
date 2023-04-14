sudoPower = False
sudoPass = "terminal"
warnStrikes = 0

class VirtualPath:
    def __init__(self, path):
        self.path = path
    
    def join(self, *paths):
        return VirtualPath('/'.join([self.path] + list(paths)))
    
    def add_file(self, filename):
        return VirtualPath('.'.join([self.path, filename]))
    
    def __str__(self):
        return self.path
    
my_path = VirtualPath('root')

def split_command(command):
    command_list = command.split()
    return command_list

def strikes(strikes):
    global warnStrikes
    warnStrikes += 1
    if warnStrikes == 3:
        print("You have too many false uses, please restart the environment.")
        exit(0)

def enter():
    print()

while True:
    command = input(f"{my_path}$ ")
    if command == "sudo":
        inputSudoPass = input("sudo: ")
        if inputSudoPass == sudoPass:
            sudoPower = True
        else:
            print("Please enter a valid sudo key: ")
    elif command == "keys":
        enter()
        print("Welcome to the key environment.")
        changeKey = input("Key to change: ")
        
        if changeKey == "sudo":
            newSudoPass = input("Sudo key: ")
            if newSudoPass != sudoPass:
                sudoPass = newSudoPass
            else:
                strikes(warnStrikes)
    elif command == "mkdir":
        new_folder = input("Enter folder name: ")
        my_path = my_path.join(new_folder)
    elif command == "mkfile":
        file_name = input("Enter file name: ")
        file_ext = input("Enter file extension: ")
        my_file = my_path.add_file(f"{file_name}.{file_ext}")
        print(f"File created at {my_file}.{file_ext}")
    elif command == "quit":
        exit(0)
    elif command == "cd":
        new_path = input("Enter path: ")
        my_path = my_path.join(new_path)
    elif  command == "ls":
        enter()
        print(my_path)