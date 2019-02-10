# Project Euler: Problem 9

# -------------------
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2

# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# -------------------

# Prod to take the product of the list [a,b,c]
from numpy import prod

# One way to do it
for a in range(1,1000-1):
    for b in range(a+1, 1000):
        c = 1000 - b - a
        if  a**2 + b**2 == c**2:
            result = [a,b,c]
            break

print('a,b,c, are respectively:')
print(result)
print('The product of abc is: ' + str(prod(result)))
