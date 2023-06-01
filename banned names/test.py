fetchNames = open("bannedNames.txt", "r")

data = fetchNames.read()

fetch_data = data.split("\n")

name = input("Enter your name: ")

if name in fetch_data:
    print(f"{name} is a name banned by the us government")
else:
    print(f"{name} is vaild")
