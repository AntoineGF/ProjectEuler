## Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
# The number is in the file Problem13_input.txt

# Save the input
with open('python/Problem13_input.txt') as f:
    input = []
    for line in f.readlines():
        input.append(int(line))

print(input)
print('Result')
print(str(sum(input))[0:10])
