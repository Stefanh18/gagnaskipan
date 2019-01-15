from random import randint
from time import time


# Time complex = O(n)
def build_list(size):
    returning_list = []
    for _ in range(size):
        returning_list.append(randint(1,6))
    return returning_list

def print_list(list_of_int):
    for index, num in enumerate(list_of_int):
        if index == len(list_of_int) - 1:
            print(num)
        else:
            print(num, end = ", ")

start_time = time()
list_of_int = build_list(3)    
print_list(list_of_int)
end_time = time()
print(end_time - start_time)