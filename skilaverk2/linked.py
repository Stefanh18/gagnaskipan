class Node:

    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList():
    
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        node = self.head
        lis = []
        while node:
            lis.append(str(node.data))
            node = node.next
        return " ".join(lis)

    def push_back(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def push_front(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def pop_front(self):
        self.head = self.head.next