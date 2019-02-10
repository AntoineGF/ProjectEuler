# Project Euler: Problem 6

#-------------------------
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.
#-------------------------

# First, sum of squares
sum_squares = []
for natural in range(1,100+1):
    sum_squares.append(natural**2)

sum_squares = sum(sum_squares)
print('The sum of the squares is ' + str(sum_squares))

# Second, square of the sum
square_sum = sum(list(range(0,100+1)))**2
print('The square of the sum is ' + str(square_sum))

# Difference
print('Hence the difference is: ' + str(square_sum - sum_squares))
