from my_array_deque import ArrayDeque
from my_linked_list import LinkedList

class Queue(LinkedList, ArrayDeque):
    
    def __init__(self, the_type):
        if the_type == "array":
            ArrayDeque.__init__(self)
        elif the_type == "linked":
            LinkedList.__init__(self)
           
        
    def add(self, value):
        
        return self.push_back(value)
    def remove(self):

        returning_data = self.pop_front()
        return returning_data

    


que = Queue("array")

for i in range(5):
    que.add(i)

print(que.remove())
print(que.get_size())
print(que)

