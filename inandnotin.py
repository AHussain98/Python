#we can use in and not is to check if something is or isnt in a sequence

parrot = "Norwegian blue"
letter = input("Enter a character: ")

if letter in parrot:
    print("{0} is in {1}".format(letter,parrot))
else:
    print("I don't need that letter")

activity = input("what would you like to do today? ") #what is the answer is uppercase?
if "cinema" not in activity.casefold(): #casefold is better than lowercase, casefold converts to lowercase
    print("I want to go to the cinema")
else:
    print("Great!")

#for going on an 18-31 holiday:

age = int(input("How old are you? "))
if 18 <= age <= 31:
    print("Welcome aboard!")
else:
    print("Sorry, not this time!")