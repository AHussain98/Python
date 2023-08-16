numbers = [1,2,3,4,5]
squares = []
for number in numbers:
    squares.append(number ** 2)
print(squares)

squares_comp = [num ** 2 for num in numbers]  # this is a list comprehension
# does the same thing as the above but is more concise
print(squares_comp)
