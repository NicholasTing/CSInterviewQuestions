class Node:

    def __init__(self, key):

        self.c = key
        self.next = None
    
print("Enter two strings: ")
string1 = input()
string2 = input()

initialized1 = False
initialized2 = False


for letter in string1:

    if not initialized1:
        head1 = Node(letter)
        temp = head1
        initialized1 = True
    
    else:
        new = Node(letter)
        temp.next = new
        temp = temp.next


for letter in string2:

    if not initialized2:
        head2 = Node(letter)
        temp = head2
        initialized2 = True
    
    else:
        new = Node(letter)
        temp.next = new
        temp = temp.next
    
answer_found = False
while head1 != None and head2 != None:
    
    if head1.c != head2.c:
        if head1.c > head2.c:
            print("1")
        
        else:
            print("-1")
        
        answer_found = True
        break
        
    head1 = head1.next
    head2 = head2.next

    if head1 and not head2:
        print("1")
        answer_found = True
        break

    if head2 and not head1:
        print("-1")
        answer_found = True
        break
    

if not answer_found:
    print("0")