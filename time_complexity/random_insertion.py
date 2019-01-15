from random import randint
from time import time

# Time complex = O(n)
def build_list(size):
    returning_list = []
    for _ in range(size):
        returning_list.append(randint(1,6))
    return returning_list

start_time = time()
print(build_list(12))
end_time = time()
print(end_time - start_time)