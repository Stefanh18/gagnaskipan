from random import randint
from time import time


# time complex = O(1)
my_list = [1,3,4,5,6]

def increase_number(my_list):
    size = len(my_list)
    number = randint(0,size - 1)
    my_list[number] += 1
    return my_list

start_time = time()
print(increase_number(my_list))
end_time = time()
print(end_time - start_time)





