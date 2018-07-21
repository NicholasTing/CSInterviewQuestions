prime_numbers = {}
        
def isPrime(number):

    for i in range(2,number):
        
        if number % i == 0:
            return False
    
    return True

number = 50

answer_found = 0
for i in range(2, number):

    first = isPrime(i) 
    second = isPrime(number - i)

    if (first and second):
        print("%d + %d = %d" % (i, number-i, number))
        answer_found = 1
        break

