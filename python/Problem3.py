# ProjectEuler : Problem 3

# -----------------------
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# -----------------------

def FindFactors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)

    return factors

def IsPrime(x):
    if x >= 2:
        for y in range(2,x):
            # print('Iteration: ' + str(y))
            # print(x%y)
            # print((x%y) == 0)
            if not ( x % y ):
                return False
    else:
        return False

    return True

# Example Result
factors = FindFactors(13195)
primes = []
for ele in factors:
    if IsPrime(ele):
        primes.append(ele)

print(primes)
print('Highest prime is: ' + str(max(primes)))

# Exercise
# Way too long to compute the factors, try alternative function
# See: https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python

from functools import reduce

def FindFactors2(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
# See notes for explanations

n = 600851475143
factors = FindFactors2(n)
primes = []
for ele in factors:
    if IsPrime(ele):
        primes.append(ele)

print(primes)
print('Highest prime is: ' + str(max(primes)))


### NOTES FindFactors2()
# Only need to range until sqrt(n), since sqrt(n) * sqrt(n) = n
# which means that numbers greater than sqrt(n) are actually redundant
# Therefore: store ith number and the other one by doing n/i

# finally, reduce(list.__add__, []) puts the two elements of the list into one long list

# Exemple: factors of 100, only have to go until sqrt(100) = 10
# This returns: [1, 100], [2, 50], [4, 25], [5,20]
# (this is actually [1, 100/1], [2, 100/2] and so on)
# reduce adds every element to a long list: [1,100,2,50,4,25,5,20]
