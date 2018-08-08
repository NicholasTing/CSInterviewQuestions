

num_cases = int(input())

while num_cases != 0:
    a,b,c = map(int, input().split())

    if a + b == c:
        print("Possible")
    
    elif a - b == c or b - a == c:
        print("Possible")
    
    elif a * b == c:
        print("Possible")
    
    elif a / b == c or b / a == c:
        print("Possible")
    
    else:
        print("Impossible")

    num_cases -= 1
    
    