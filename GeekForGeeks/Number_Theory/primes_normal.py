# Nicholas Ting
# Finding primes without sieve of erathosthenes.py

def isPrime(primes):

    root = primes ** (1/2)
    for i in range(2, int(root) +1):

        if primes % i == 0:
            return False
    
    return True

print("First, input a number and we will return a list of primes up to that number.")
primes = int(input())

check = []

for i in range(2,primes):

    if isPrime(i):
        check.append(i)


for num in check:
    print(num)


print(len(check))