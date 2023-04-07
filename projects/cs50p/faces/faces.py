def convert(randomInput):
    randomInput.replace(":)", "🙂")
    randomInput.replace(":(", "🙁")
    print(randomInput)

def main():
    tempInput = input()
    convert(tempInput)

main()