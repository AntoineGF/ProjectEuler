# Project Euler: Problem 7

#-------------------------
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
# see that the 6th prime is 13.

# What is the 10 001st prime number?
#-------------------------

def IsPrime(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
        return False

    return True

# Find the nth prime number
n = 10001
i = 1
prime_numbers = []

# As long as the nth prime number is not reached, continue
while len(prime_numbers) < n:
    # If the number is prime, store it
    if IsPrime(i) == True:
        # Store all prime numbers (takes 34.7s approx.)
        prime_numbers.append(i)
    # Test the following number
    i+=1

print('The ' + str(n) + 'th prime number is: ' + str(prime_numbers[-1]))
