path = "o/,project/,"
def main():
    while True:
        command = input(f"{path}$ ")
        if command == "sudo":
            inputSudoPass = input("sudo: ")