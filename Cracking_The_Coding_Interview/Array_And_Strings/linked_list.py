class Node(object):

    def __init__(self, d, n = None):
        self.data = d
        self.next = n


class LinkedList(object):

    def __init__(self, r = None):
        self.root = r
        self.size = 0

print("Linked list demo")
print("Enter a number for the root 1 of the linked list")

root_number1 = int(input())
root_node1 = Node(int(root_number1))
temporary_root = root_node1

testing_node = Node(123)

data = input()
index = 0

while data != "end":

    if(index == 2):
        temporary_root.next = testing_node
        temporary_root = temporary_root.next

    new_node = Node(int(data))
    temporary_root.next = new_node
    temporary_root = temporary_root.next
    index += 1
    data = input()

print("Enter a number for the root 2 of the linked list")
root_number2 = int(input())

root_node2 = Node(int(root_number2))
temporary_root = root_node2

data = input()
index = 0

checked1 = []
checked2 = []

while data != "end":

    if(index == 3):
        temporary_root.next = testing_node
        temporary_root = temporary_root.next

    new_node = Node(int(data))
    temporary_root.next = new_node
    temporary_root = temporary_root.next

    index += 1
    data = input()

while root_node1 != None:
    print(root_node1.data)
    checked1.append(root_node1)
    root_node1 = root_node1.next
    
while root_node2 != None:
    print(root_node2.data)
    checked2.append(root_node2)
    root_node2 = root_node2.next

duplicated = 0

print(checked1)
print(checked2)
for node in checked1:
    if node in checked2:
        print("Duplicate")
        duplicated = 1
        break

if not duplicated:
    print("Not duplicated")



