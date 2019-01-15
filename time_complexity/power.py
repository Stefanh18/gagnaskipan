from time import time

# Time complex = O(n)
def power(base, exp):
    ret_val = 1
    for _ in range(exp):
        ret_val *= base
    return ret_val

def better_power(base, exp):
    return base**exp

starting_time = time()
print(power(2,2))
end_time = time()
print(end_time - starting_time)
starting_time = time()
print(better_power(2,2))
end_time = time()
print(end_time - starting_time)

# Seinna er hraðara