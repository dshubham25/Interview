# Given an array of sorted numbers, remove all duplicates from it.
# You should not use any extra space; after removing the duplicates in-place return the new length of the array.

def remove_dup(arr):
    non_dup = 1
    i = 1
    while (i < len(arr)):
        if arr[non_dup - 1] != arr[i]:
            arr[non_dup] = arr[i]
            non_dup += 1
        i += 1
    return non_dup


print(remove_dup([2, 3, 3, 3, 4, 7, 9, 9]))


# Given an unsorted array of numbers and a target ‘key’,
# remove all instances of ‘key’ in-place and return the new length of the array.

def remove_ele(arr, key):
    next = 0
    for i in range(len(arr)):
        if arr[i] != key:
            arr[next] = arr[i]
            next += 1
    return next


print(remove_ele([3, 2, 3, 6, 3, 10, 9, 3], 3))
