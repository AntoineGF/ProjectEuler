# Project Euler: Problem 2

def Fibo(n):
    fibo = [0]*(n+1)
    if n == 1:
        fibo = 1
        return fibo
    else:
        fibo[0] = 1
        for j in range(1, n+1):
            fibo[j] = fibo[j - 1] + fibo[j - 2]

        return fibo[1:]

# Exercise: with terms in Fibo < 4 mio, what is sum of even-valued terms ?
n = 10
fibo = Fibo(n)
while fibo[-1] < 4*(10**6):
    n += 1
    fibo = Fibo(n)
    print('At n = ' + str(n) + ', largest term is ' + str(fibo[-1]))

n = 32
fibo = Fibo(n)

for i in range(0, len(fibo)):
    if fibo[i]%2 != 0:
        fibo[i] = 0

print(fibo)
print(sum(fibo))
