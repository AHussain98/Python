#boolean: means can only be True or False, capitals matter
#in python, we can use the not keyword instead of !=

day = "Saturday"
temperature = 30
raining = True #the boolean must have a capital first letter

if (day == "Saturday" and temperature > 27) or not raining: #and not means the raining variable must evaluate to be false if the condition is to be met
    print("Go swimming")
else:
    print("Learn python instead")

#None, False, 0, and any empty sequence is considered false

if 0:
    print("True") #unreachable, 0 is evaluated to false automatically
else:
    print("False")

name = input("Please enter your name: ") #entering nothing results in the below evaluating as false, as empty strings evaluate as false
#if name: #this just means if name evaluates as true
if name != "": #so if name is not an empty sting, this is another way of writing the above
    print("Valid name!")
else:
    print("Invalid name!")



