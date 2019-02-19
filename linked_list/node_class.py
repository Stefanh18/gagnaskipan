class Node:

    def __init__(self, data = None, Next = None):
        self.data = data
        self.next = Next


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

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

    def pop_back(self):
    
        x = self.head
        y = x.next
        if y == None:
            self.head, self.tail = None, None
            return None
        
        while y.next != None:
            x = x.next
            y = x.next

        self.tail = x
        self.tail.next = None

    def __str__(self):
        ret_str = ""
        node = self.head
        while node != None:
            ret_str += str(node.data) + "-->"
            node = node.next
        return ret_str


class Stacks(LinkedList):
    
    def __init__(self):
        super(Stacks, self).__init__()
        self.size = 0

    







lis = LinkedList()

for i in range(1, 6):
    lis.push_back("(string " + str(i) + ")")

lis.push_front("(string 0)")

lis.pop_back()

print(lis)