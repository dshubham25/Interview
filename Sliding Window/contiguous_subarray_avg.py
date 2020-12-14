# Given an array, find the average of all contiguous subarrays of size ‘K’ in it.


def continguous_subarray(arr, K):
    res = []
    windowSum, windowStart = 0.0, 0  # sum in float cause of avg
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]  # add next element
        if windowEnd >= K-1:
            res.append(windowSum / K)
            windowSum -= arr[windowStart]  # subtract the element going out
            windowStart += 1
    return res


res = continguous_subarray([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)
print(res)
