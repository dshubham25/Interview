# Given an array of sorted numbers and a target sum,
# find a pair in the array whose sum is equal to the given target.


def target_sum(arr, target):
    left = 0
    right = len(arr) - 1
    while (left < right):
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            return [left, right]
        if target > curr_sum:
            left += 1
        else:
            right -= 1
    return [-1, -1]


print(target_sum([1, 2, 3, 4, 6], 6))
