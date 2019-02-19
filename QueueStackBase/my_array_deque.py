
class ArrayDeque():

    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.arr = [0] * self.capacity
        self.first = 0

    def __str__(self):
        returning_str = ""
        for i in range(0, self.size):
                returning_str += str(self.arr[i]) + " "
        return returning_str

    def get_size(self):
        return self.size

    def push_back(self, value):
        if self.size == self.capacity:
            self.resize(self.capacity * 2)
        self.arr[self.size] = value  
        self.size += 1      

    def pop_back(self):
        if self.size == 0:
            return None
        returning_data = self.arr[self.size -1]
        self.arr[self.size - 1] = 0
        self.size -= 1
        return returning_data

    def pop_front(self):
        if self.size == 0:
            return None
        returning_data = self.arr[0]
        for i in range(1, self.size + 1):
            self.arr[i-1] = self.arr[i]
        self.size -= 1
        return returning_data
 
    def push_front(self, value):       #spurja kennara lis + lis
        if self.size == len(self.arr):
            self.resize(self.size * 2)
        new_arr = [0] * self.capacity
        for i in range(self.size):
            new_arr[i+1] = self.arr[i]
        self.arr = new_arr
        self.arr[0] = value
        self.size += 1

    def resize(self, new_cap):
        new_arr = [0] * new_cap
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.capacity = new_cap
        self.arr = new_arr
    