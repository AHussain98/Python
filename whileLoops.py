# #while loop runs while the condition is true
# i = 0 #with a while loop, the condition must be initialised before the while loop starts
# while i < 10:
#     print("i is now {}".format(i),end=" ") #end used to print on the same line
#     i += 1
#
# ##if the condition never becomes false, the loop will return forever
#
# available_exits = ["North", "South", "East", "West"]
# chosen_exit = 123 #has to be initalised, doesn't even matter if its a string or int
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose a direction: ")
#     if (chosen_exit.casefold() == "quit"): #casefold converts to lowercase, more aggressive than .lower()
#         print("Quitting game")
#         break #break out of the loop
# else: print("aren't you glad you got out of there")
#else code block for the loop will only execute if the loop completes successfully
#if the loop ends due to a break, or fails, the else will not run

# #to print on same line
# for i in range(6):
#     print(i,end=" ") #end is used tp print on the same line


#remember that 0 is divisible by every number, so an if statement should factor this in, eg if i%13 == 0 will evaluate as true if i is 0
#while loops best used when you dont know how many times you need to loop, such as when reading data from a file