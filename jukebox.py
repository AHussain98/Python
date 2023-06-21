# when you import from another file, that code is executed as soon as the program runs
# like a header file, its better to import files that are used for object definitions, rather than executing any code at runtime

# the filename we import from must not have any spaces in it, else we cannot import from it
from Sequence_Operations_3 import families

while True:
    print("Please choose your family (invalid choice exits): ")
    for index, (member1,member2,member3) in enumerate(families):  # we can unpack the tuple here if we use parenthesis
    #    member1,member2,member3 = family # unpack
        print("{} : {}".format(index + 1,(member1,member2,member3)))

    choice = int(input()) # take input from the user and convert into an integer
    if 1 <= choice <= len(families):
        chosen_family = families[choice -1]
    else:
        break # put the break here as it is executed if the choice is invalid
    print(chosen_family)
    print("now pick a family member between 1 and 3 (invalid choice exits): ")
    chosen_person = int(input())
    if 1 <= chosen_person <= len(chosen_family):
        print(chosen_family[chosen_person - 1])
    else:
        break
    break

# a constant is a fixed value that doesnt change
# the interperter will not stop you from changing the value of any veriable
# type a variable in full caps to indicate it is a constant

