# ProjectEuler: Problem 5

# -----------------------
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# -----------------------

from math import gcd

def largest_common_multiple(a,b):
    # Returns the largest common multiple
    # gcd returns greatest common DIVISOR, hence the formula
    return a*b//gcd(a,b)


# Using reduce to apply the function to every element of the range
from functools import reduce

result = reduce(largest_common_multiple, range(1,20+1))

print("Largest common multiple is: " + str(result))
