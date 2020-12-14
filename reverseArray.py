def reverse_array(arr):
    arr = arr[::-1]
    print(arr)

A = [1, 2, 3, 4, 5, 6]
#print(A)
#reverse_array(A)

def find_max_min(arr):
    arr.sort()
    return min(arr), max(arr)

A = [1, 2, 3, 4, 5, 6]
find_max_min(A)
