# import random
#
# answer = random.randint(1,10) # so dot the module youve imported with the function you want to use
# # randint function produces a random integer in the range we've defined
# # using the random module that comes with python, import to use modules from pythons standard library
#
# # print("Please give your guess: ")
# # guess = int(input()) # change the string input into a int and store in the guess variable
# # #print(answer)
# # if guess == answer:
# #     print("Well done! first time!") #TODO: WOW, these comments are tracked in the tab below, great for testing purposes and reminders
# # else:
# #     if guess < answer:
# #          print("please guess higher")
# #     else:
# #          print("please guess lower")
# #     guess = int(input("Have another go: ")) #this line will run because its on the same level of indentation as the if and else blocks
# #     if guess == answer:
# #          print("Well done, you guessed correctly second time around!")
# #     else:
# #          print("Wrong again!")
#
# # try with a while loop for infinite guesses, more suited than a for loop is
# guess = 0 # initalise so the variable exists
# count = 0
# # print(answer) #used for test
# # while guess != answer:
# #     guess = int(input("Give your guess: ")) #remember input returns string by default!!!!!!
# #     count += 1
# #     if guess == answer:
# #         print("Correct!")
# #         if guess == answer and count == 1:
# #             print("Correct first time!")
# #         break
# #     if guess == 0:
# #         print("Quitter!")
# #         break
#
#
# #we can reduce the time taken to search for a value using binary search
# # #remember pythons integer division rounds down!
# # print(int(5/3)) #rounded down, integer divison // does this by default
#
# #binary search example
#
# #create the low and high bound variables
# low = 1
# high = 1000
#
# print("Please think of a number between {} and {}".format(low,high))
# input("Press press the ENTER key to begin")
#
# guesses = 1
# while True:  # we cant do "while guess != answer because we dont know the avlue of answr
#     guess = low + (high - low) // 2  # calculates the midpoint between the low and high values to produce the next guess
#     highLow = input("My guess is {}. Should I guess higher or lower? "
#                      "Enter h or l, or c if I was correct"
#                     .format(guess)).casefold()  # inputs can be casefolded
#     # using another "" allows you to split the line
#     if highLow == "h":  # remember that input returns a string, so its h in quotes
#         low = guess + 1  # one because we've already evaluated the guess value
#     elif highLow == "l":
#         # could just write pass in here to skip this
#         high = guess - 1
#     elif highLow == "c":
#         print("I got it in {} guesses!".format(guesses))
#         break
#     else:
#         print("Please choose a valid option")
#     guesses += 1  # augmented assignment, more efficient in python
#     # because the variable is only evaluated once,
#     # guessess = guesses +1 means it gets evaluated twice in python, not in c++
# # you can use the pass keyword in python to skip a block of code, but not end the loop
#
# # else can also be used at the end of loops, causes a block of code
# # to be executed if the loop was allowed to continue to the end
# # below, the loop only terminates normally when all the values are acceptable
# # we can print something that states this to the user using an else statement
# numbers = [1, 45, 32, 12, 60]
# for number in numbers:
#     if number % 8 == 0:
#        print("The numbers are unacceptable")
#        break
# else:
#     print("All the numbers are acceptable") #the else for the whole loop must be at the same level as the for
#     #else is associated with the for loop, same level as for
#
#
# # do the binary search loop with an else:
#
# while low != high:  #if low == high, then we've found the number,
#     # assume in this scenario the number is in the range given, if not then this wouldnt work as the condition
#     guess = low + (high - low) // 2  # calculates the midpoint between the low and high values to produce the next guess
#     highLow = input("My guess is {}. Should I guess higher or lower? "
#                      "Enter h or l, or c if I was correct"
#                     .format(guess)).casefold()  # inputs can be casefolded
#     # using another "" allows you to split the line
#     if highLow == "h":  # remember that input returns a string, so its h in quotes
#         low = guess + 1  # one because we've already evaluated the guess value
#     elif highLow == "l":
#         # could just write pass in here to skip this
#         high = guess - 1
# #     elif highLow == "c":
# #         print("I got it in {} guesses!".format(guesses))
# #         break
# #     else:
# #         print("Please choose a valid option")
#     guesses += 1  # augmented assignment, more efficient in python
# else:
#     print("You thought of the number {}".format(low))
#     print("I got it in {} guesses!".format(guesses))


menu = ["Bread", "Cheese", "Chicken", "Lamb", "Roti"]
while True: #will continue to run until break occurs
 for i in range(1,6):
    print("Menu item {}: {}".format(i, menu[i-1]))
 choice = int(input("What would you like? "))
 if choice == 0:
    print("We'll get your coats")
    break
 elif choice <= 0 or choice >= 6:
    print("Sorry, that's not available, please choose from one of the below: ")
 else:
    print("Wise choice, your {} is coming right up".format(menu[choice-1]))
    break


