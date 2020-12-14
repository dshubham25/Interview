# Given an array of positive numbers and a positive number ‘S’,
#  find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’.
# Return 0, if no such subarray exists.


def smallest_subarray_with_given_sum(arr, s):
    windowSum = 0
    min_length = float('inf')
    windowStart = 0
    for windowEnd in range(0, len(arr)):
        windowSum += arr[windowEnd]
        while windowSum >= s:
            min_length = min(min_length, windowEnd-windowStart+1)
            windowSum -= arr[windowStart]
            windowStart += 1
    while min_length == float('inf'):
        return 0
    return min_length


print(smallest_subarray_with_given_sum([2, 1, 5, 2, 3, 2], 7))
