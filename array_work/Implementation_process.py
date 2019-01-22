class ArryList:
    def __init__(self):
        self.size = 0
        self.capacity = 4
        self.arr = [0] * self.capacity

    def print_array_list(self):
        for index in range(self.size):
            if index == self.size - 1:
                print(self.arr[index])
            else:
                print(self.arr[index], end= ", ")
    
    def append(self, value):
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = value
        self.size += 1

    def resize(self):
        self.capacity *= 2
        new_list = [0] * self.capacity
        for index in range(self.size):
            new_list[index] = self.arr[index]
        self.arr = new_list
    
    def get_first(self):
        return self.arr[0]

    def get_at(self, index):
        return self.arr[index]
    
    def get_last(self):
        return self.arr[self.size - 1]
    
    def prepend(self, value):
        if self.size == self.capacity:
            self.resize()
        new_list = [0] * self.capacity
        new_list[0] = value
        for index in range(self.size):
            new_list[index + 1] = self.arr[index]
        self.size += 1
        self.arr = new_list
    
    def insert(self, value, index):
        if self.size == 0:
            raise IndexError
        if self.size == self.capacity:
            self.resize()
        new_list = [0] * self.capacity
        for list_index in range(index):
            new_list[list_index] = self.arr[list_index]
        new_list[index] = value
        for list_index in range(index, self.size):
            new_list[list_index + 1] = self.arr[list_index]
        self.size += 1
        self.arr = new_list
    
    def remove(self, index):
        if self.size == 0:
            raise IndexError
        new_list = [0] * self.capacity
        for list_index in range(index):
            new_list[list_index] = self.arr[list_index]
        for list_index in range(index, self.size):
            new_list[list_index - 1] = self.arr[list_index]
        self.size -= 1
        self.arr = new_list        

listi = ArryList()
listi.append(1)
listi.append(2)
listi.append(3)
listi.append(4)
listi.print_array_list()
print(listi.get_first())
print(listi.get_at(2))
print(listi.get_last())
listi.prepend(5)
listi.print_array_list()
listi.insert(7,3)
listi.print_array_list()
listi.remove(2)
listi.print_array_list()