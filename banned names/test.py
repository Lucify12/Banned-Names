fetchNames = open("bannedNames.txt", "r")

data = fetchNames.read()

fetch_data = data.split("\n")

name = input("Enter your name: ")

if name in fetch_data:
    print(name + " is banned")
else:
    print(name + " is valid welcome")