# úr bókinni
def binary_search(data, target, low, high):

    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target <  data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1 , high)


a_list = [1, 5, 6, 7, 34, 56 ,2, 56 , 65 , 123]
a_list.sort()

print(binary_search(a_list, 300, 0 , len(a_list) -1 ))
