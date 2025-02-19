def welcome():
    print("Welcome to the Hundred Acre Wood")
    pass

welcome()

def greeting(name):
    print("Welcome to The Hundred Acre Wood, " + name)
    pass

greeting("Alexis Covington")

def print_catchphrase(character):
    if character == "Pooh":
        print("Oh bother")
    elif character == "Tigger":
        print("TTFN")

print_catchphrase("Tigger")