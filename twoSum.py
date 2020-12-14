# Given an array of integers, return the two numbers such that they add up to
# a specific target. You may assume that each input would have exactly one
# solution, and you may not use the same element twice.

# Use Hash Table to solve this type of questions.
# T.C. - O(N)
# S.C. - O(N)
def two_sum(arr, num):
    ht = {}
    for i in arr:
        if arr[i] in ht:
            print(ht[arr[i]], arr[i])
            return True
        else:
            ht[num - arr[i]] = arr[i]
    return False

