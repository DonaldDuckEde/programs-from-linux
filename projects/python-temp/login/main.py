sudoPower = False
sudoPass = "terminal"
warnStrikes = 0

class VirtualPath:
    def __init__(self, path):
        self.path = path
    
    def join(self, *paths):
        return VirtualPath('/'.join([self.path] + list(paths)))
    
    def __str__(self):
        return self.path

my_path = VirtualPath('root')

def strikes(strikes):
    warnStrikes += 1
    if warnStrikes == 3:
        print("You have to much false uses please restart the evenirement.")
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
        print("welcome to the key environment.")
        changeKey = input("Key to change: ")
        
        if changeKey == "sudo":
            newSudoPass = input("Sudo key: ")
            if newSudoPass != sudoPass:
                newSudoPass = sudoPass
            else:
                strikes(warnStrikes)
    elif command == "mkdir":
        new_folder = input("Enter folder name: ")
        my_path = my_path.join(new_folder)