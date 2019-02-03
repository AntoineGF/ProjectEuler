# ProjectEuler: Problem 4 

# -----------------------
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.
# -----------------------


# Exercise

# Store all the products 
results = []
for i in range(1,999+1):
    for j in range(1,999+1):
        results.append(str(i*j))
        
# Keep only numbers whose length is equal to 6
results = [ele for ele in results if len(ele) == 6]

# Find the candidates
candidates = []
for ele in results: 
    temp = ele[-1:-4:-1]
    if ele[0:3] == temp: 
        candidates.append(int(ele))

# Solution
print('Largest palyindrom is: ' + str(max(candidates)))