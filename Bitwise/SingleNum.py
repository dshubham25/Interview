# In a non-empty array of integers, every number appears twice except for one, find that single number

from typing import AsyncIterator


def single_num(arr):
    num = 0
    for number in arr:
        num ^= number
    return num


arr = [1, 4, 2, 1, 3, 2, 3]
print(single_num(arr))
