
class LinkedList():
    def __init__(self):
            self.head = None
            self.tail = None

    class Node:
        def __init__(self, data = None, next = None):
            self.data = data
            self.next = next

    

    def __str__(self):
        returning_str = ""
        node = self.head
        while node:
            returning_str += str(node.data) + " "
            node = node.next
        return returning_str


    def get_size(self):
        node = self.head
        size = 0
        while node:
            size +=1
            node = node.next
        return size

    def push_back(self, data):
        new_node = self.Node(data)
        if self.head == None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def push_front(self, data):
        new_node = self.Node(data, self.head)
        self.head = new_node

    def pop_front(self):
        node = self.head
        self.head = self.head.next
        return node.data
        