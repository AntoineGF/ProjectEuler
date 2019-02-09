# Project Euler: Problem 10

# -----------------
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.
# -----------------

# Implementing the Sieve of Eratosthenes
# Source: https://codereview.stackexchange.com/questions/132343/project-euler-10-find-the-sum-of-all-the-primes-below-two-million?rq=1
# About 'yield': https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do

def Eratosthenes(n):
    # Declare a set - an unordered collection of unique elements
    multiples = set()

    # Iterate through [2,n]
    for i in range(2, n+1):

        # If i has not been eliminated already
        if i not in multiples:
            # Yay prime!
            # yield is like return, except it will return a GENERATOR
            yield i

            # Add multiples of the prime in the range to the 'invalid' set
            # Example for 2, then 4,6,8,10, ... will be in multiples and de facto
            # will not be considered as being prime numbers. This increases efficiency drastically
            multiples.update(range(i*i, n+1, i))

# Example: Generator object
print(Eratosthenes(15))
for ele in Eratosthenes(15):
    print(ele)

# Now sum it up
summ = 0
prime_numbers = list(Eratosthenes(2*10**6))
for x in prime_numbers:
    summ = int(x) + summ

print(summ)
