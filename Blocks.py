# there are no {} in python, indentation is used instead
# blocks of code can exist within other blocks
# whenever a line ends with a colon, the new line underneath must be indented
# once you're finished with that block of code, you can move onto a new line without an indentation

for i in range(1, 13):
    print("No. {} squared is {} and cubed is {}".format(i, i ** 2, i ** 3))
    print("*" * 80)
# from here, out of the loop
print("*" * 80)  # printing * 80 times

name = input("Please enter your name: ")
age = int(input("How old are you, " + name + "? "))  # input function returns a string by default
# to get the number from the user, convert input to int with int()

print(age)

if age >= 18:  # as soon as one logical condition in the block is met, the rest are skipped
    print("You can vote!")
elif age < 1:
    print("Impossible!")  # python uses elif, unlike c++ which uses else if
else:  # else block must have the same indentation as if
    print("You have to wait " + str(18 - age) + " years")  # we can only concatenate strings, not ints, so convert the sum to string

#create a guessing game
print()

print("Please give your guess: ")
guess = int(input()) # change the string input into a int and store in the guess variable

if guess == 3:
    print("Well done! first time!")
else:
    if guess < 3:
         print("please guess higher")
    else:
         print("please guess lower")
    guess = int(input("Have another go: ")) #this line will run because its on the same level of indentation as the if and else blocks
    if guess == 3:
         print("Well done, you guessed correctly second time around!")
    else:
         print("Wrong again!")

#other smart way
# if guess != 3: #smarter and cleaner code this way
#     if guess < 3:
#         print("please guess higher")
#     else:
#         print("please guess lower")
#     guess = int(input("Have another go: ")) #this line will run because its on the same level of indentation as the if and else blocks
#     if guess == 3:
#         print("Well done, you guessed correctly second time around!")
#     else:
#         print("Wrong again!")
# else:
#     print("Well done! First time!")

# if guess > 3:
#     print("Too high!")
#     guess2 = int(input("have another go: ")) #give them another go, its important this is on the same level of indentation
#     if guess2 == 3: # remember = is assignment operator, == is equality operator
#         print("you got it!")
#     else: #include another else statement for the second guess
#         print("aw too high again")
# elif guess < 3: #python uses elif
#     print("Too low!")
#     guess2 = int(input("have another go: "))  # give them another go, its important this is on the same level of indentation
#     if guess2 == 3:
#         print("you got it!")
#     else: #remember if, else and elif keywords have to be indented to the same level
#         print("aw too low again")
# else: #only kicks in if the first two conditions are false, there can be many elifs but only one else
#     print("you got it first time!!")

#lets try doing the above in a smarter way, see above
