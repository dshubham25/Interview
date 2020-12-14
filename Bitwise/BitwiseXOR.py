# Given an array of n-1n−1 integers in the range from 11 to nn, find the one number that is missing from the array.

def missing_num(arr):
    n = len(arr) + 1
    x = 1
    for i in range(2, n+1):
        x = x ^ i
    x2 = arr[0]
    for i in range(1, n-1):
        x2 = x2 ^ arr[i]
    return x ^ x2


print(missing_num([1, 5, 2, 6, 4]))
