def sum_of_ints(integer, counter = 0, sum_of_int = 0):
    try:
        digit = int(str(integer)[counter])
    except:
        return sum_of_int
    return sum_of_ints(integer, counter + 1, sum_of_int + digit)

print(sum_of_ints(212))