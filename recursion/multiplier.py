def multiplication(a, b, c = 0):
    if b == 0:
        return c
    if b > 0:
        return multiplication(a, b - 1, c + a)
    else:
        return multiplication(a, b + 1, c - a)

print(multiplication(100, -2))