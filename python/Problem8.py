# Project Euler: Problem 8

#-------------------------
# The four adjacent digits in the 1000-digit number that have the greatest
# product are 9 × 9 × 8 × 9 = 5832.

# Find the thirteen adjacent digits in the 1000-digit number that have the
# greatest product. What is the value of this product?
#-------------------------

# Import the product to have the product of a list (np.prod())
import numpy as np

# To have a clean way to import the 1'000 digits number
file = open('Problem8_input.txt', 'r')
input = ''
for l in file.readlines():
    input += l.strip('\n')

# Replicate Example
maximum = 0
consecutives = 13

for idx in range(0+consecutives, len(input)):
    # Get the idx to make the product
    indices = [idx - i for i in range(0,consecutives)]
    temp = [int(input[i]) for i in indices]
    product = np.prod(temp)

    # If product is greater than the previous maximum, then it is the new max
    if product > maximum:
        productOf = temp
        maximum = product

print('The maximum is: ' + str(maximum))
print('Obtained with the product of: ')
print(productOf)
