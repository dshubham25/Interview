# In a non-empty array of numbers, every number appears exactly twice except two numbers that appear only once.
# Find the two numbers that appear only once.

def find_num(nums):
    n1xn2 = 0
    for num in nums:
        n1xn2 ^= num
    rightmost = 1
    while (rightmost & n1xn2) == 0:
        rightmost = rightmost << 1
    num1, num2 = 0, 0
    for num in nums:
        if (num & rightmost) != 0:
            num1 ^= num
        else:
            num2 ^= num
    return [num1, num2]


print(find_num([1, 4, 2, 1, 3, 5, 6, 2, 3, 5]))
print(find_num([2, 1, 3, 2]))
