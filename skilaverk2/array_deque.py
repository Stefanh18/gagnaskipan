class ArrayDeque:
    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.arr = [0] * self.capacity
        self.first = 0

    def push_back(self, param):
        if(self.size == self.capacity):
            self.resize(2 * self.size)
        self.arr[self.size] = param
        self.size += 1

    def push_front(self, param):
        """add item to beginning of deque"""
        if self.size == self.capacity:
            self.resize(2 * self.size)
        for _ in range(self.arr):
            pass
            
    
    def resize(self, new_cap):
        new_arr = [0] * new_cap
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.capacity = new_cap
        self.arr = new_arr

    def print(self):
        for i in range(0, self.size):
            if i != self.size - 1:
                print(str(self.arr[i]), end = " ")
            else:
                print(str(self.arr[i]))

    # def delete_first(self):
    #     if(not self.is_empty()):
    #         ret = self._data[self._first]
    #         self._data[self._first] = None
    #         self._first = (self._first + 1)%(len(self._data))
    #         self._n -= 1

    #         # If we're down to smaller than a quarter occupied,
    #         # cut array size in half.
    #         if(self._n < len(self._data)//4):
    #             self._resize(len(self._data)//2)

    #     else:
    #         raise Empty("oops, empty deque")s

    # def delete_last(self):
    #     if(not self.is_empty()):
    #         getix = (self._first + self._n - 1)%(len(self._data))
    #         ret = self._data[getix]
    #         self._data[getix] = None
    #         self._n -= 1

    #         # If we're down to smaller than a quarter occupied,
    #         # cut array size in half.
    #         if(self._n < len(self._data)//4):
    #             self._resize(len(self._data)//2)

    #     else:
    #         raise Empty("oops, empty deque")


arr = ArrayDeque()
arr.push_front(2)
arr.push_front(3)
arr.push_front(4)
arr.push_front(5)
arr.print()

