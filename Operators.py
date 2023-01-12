a = 12
b = 3
#so now whenever we use a and b, python knows we're referring to these two values
#in python, anything that can be calculated to return a value is an expression, see below
#so the expression a and b are evaluated to return 12 and 3, as a and b have been bound to these values
print(a+b)
print(a-b)
print(a*b)
print(a/b) #returns 4.0
print(a // b) #integer division (floor division), rounded down, so returns 4, important operator when int must be used
print(a%b) #modulo: the remainder after integer division

print()#empty line

for i in range(1,4): #this is a for loop for i from 1 to 3, range gives you a range of numbers from 1 to 3
    print(i) #so if we used a/b instead of 4 in the above loop, this wouldnt work, however it will work if we use the integer division
#python has mathematical operator precedence, BIDMAS, just use brackets in practice

