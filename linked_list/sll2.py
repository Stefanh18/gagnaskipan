class Node:
    def __init__(self, nextt, data):
        self.nextt = nextt
        self.data = data

def push_front(head, val):
    return Node(head, val)

def push_back(head, val):
    if head == None:
        return Node(head, val)
    return Node(push_back(head.nextt, val), head.data)

def print_list(head):
    if head == None:
        print()
    else:
        print(head.data, end = ' ')
        print_list(head.nextt)

def count_list(head):
    node = head
    if node == None:
        return 0
    else:
        return 1 + count_list(node.nextt)

def insert_between(head, val):
    if head == None:
        return Node(head,val)
    if head.data >= val:
        return Node(head, val)
    return Node(insert_between(head.nextt, val), head.data)

def reverse (head, tail = None):
    nextt = head.nextt
    head.nextt = tail
    if nextt == None:
        return head
    else:
        return reverse(nextt, head)

head = None

for x in range(10):
    head = push_back(head, x)

print_list(head)

print(count_list(head))
listi = insert_between(head, 4)
print_list(listi)
listi1 = reverse(head)
print_list(listi1)
