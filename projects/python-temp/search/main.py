import webbrowser
import urllib.parse

userInput = input("Search: ")
userInput_encoded = urllib.parse.quote_plus(userInput)

url = "https://www.google.com/search?q={}".format(userInput_encoded)

webbrowser.open(url)