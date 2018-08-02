# https://practice.geeksforgeeks.org/problems/find-all-pairs-whose-sum-is-x/0
# Find all pairs with given sum
# Coded by Jing Kun Ting
# Coded for Interview Practice

TC = int(input())

while TC != 0:
    
    n, m, x = input().split(' ')
    n = int(n)
    m = int(m)
    x = int(x)
    
    array_n = input().split(' ')
    array_m = input().split(' ')
    
    array_n = [int(x) for x in array_n[:-1]]
    array_m = [int(x) for x in array_m[:-1]]
    
    exists = False
    array_dict = {}
    answer = []

    for number in array_m:
        
        array_dict[number] = number

    for number in sorted(array_n):

        key = x - number
        
        if key in array_dict.keys():
            exists = True
            answer.append("%d %d" % (number, key))

    if not exists:
        print("-1")
    
    elif len(answer) == 1:
        print(answer[0])
    
    else:
        
        final_answer = ""
        for x in range(len(answer)-1):
            final_answer += answer[x] + ", "
            
        final_answer += answer[-1]
        print(final_answer)
        
    TC -= 1
