def string_length_recurr(string, index = 0, c = 0):
    try:
        string[index]
        c += 1
        return string_length_recurr(string, index + 1, c)
    except:
        return c

print(string_length_recurr("what the heck"))


    
