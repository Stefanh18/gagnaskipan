from time import time

# Time complex = O(n)
def multiplication(integer, integer2):
    end_value = 0
    for _ in range(integer2):
        end_value += integer
    return end_value

start_time = time()
print(multiplication(4,2))
end_time = time()
print(end_time - start_time)