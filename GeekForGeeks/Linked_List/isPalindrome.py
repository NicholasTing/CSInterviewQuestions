def isPalindrome(head):
    # Code here
    answers = []
    while head != None:
        answers.append(head.data)
        head = head.next
    
    index = -1
    middle = 0
    odd = False
    if len(answers) % 2 != 0:
        middle = len(answers) / 2 + 1
        odd = True
        
    for ans in range(len(answers)):
        
        if odd and ans == middle:
            continue
        
        if answers[ans] != answers[index]:
            return 0
            
        index -= 1
        
    return 1