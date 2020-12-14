# Given an array of positive numbers and a positive number ‘k’,
# find the maximum sum of any contiguous subarray of size ‘k’.

def max_sum_subarray(arr, K):
    windowSum, max_sum = 0, 0
    windowStart = 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= K-1:
            max_sum = max(max_sum, windowSum)
            windowSum -= arr[windowStart]
            windowStart += 1
    return max_sum


print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))
print(max_sum_subarray([2, 3, 4, 1, 5], 2))
