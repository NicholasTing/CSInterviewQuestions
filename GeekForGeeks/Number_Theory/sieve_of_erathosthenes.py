# Nicholas Ting
# Code on sieve of erathosthenes.py

def sieve_of_erathosthenese(primes):

    p = 2
    prime = [True for i in range(primes+1)]

    while(p * p <= primes):
        
        if(prime[p] == True):

            for i in range(p*2, primes+1, p):
                prime[i] = False
            
        p += 1
    
    count = 0
    for p in range(2,primes):
        
        if prime[p]:
            print(p)
            count += 1

    print(count)

def isPrime(primes):

    root = primes ** (1/2)
    for i in range(2, int(root) +1):

        if primes % i == 0:
            return False
    
    return True

def notSieve(primes):

    check = []

    for i in range(2,primes):

        if isPrime(i):
            check.append(i)


    for num in check:
        print(num)

    print(len(check))


print("First, input a number and we will return a list of primes up to that number.")
primes = int(input())

print("Do you want to use the sieve method? Yes or No")
method = input()

if method == "Yes":

    sieve_of_erathosthenese(primes)

else:

    notSieve(primes)
