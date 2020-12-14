# Given an array of characters where each character represents a fruit tree, you are given two baskets and
# your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.
# You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree until you cannot,
# i.e., you will stop when you have to pick from a third fruit type.

# Write a function to return the maximum number of fruits in both the baskets.


def fruits_into_basket(fruits):
    window_start = 0
    max_len = 0
    freq = {}

    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]
        if right_fruit not in freq:
            freq[right_fruit] = 0
        freq[right_fruit] += 1

        while len(freq) > 2:
            left_fruit = fruits[window_start]
            freq[left_fruit] -= 1
            if freq[left_fruit] == 0:
                del freq[left_fruit]
            window_start += 1
        max_len = max(max_len, window_end - window_start + 1)
    return max_len


print(fruits_into_basket(['A', 'B', 'C', 'A', 'C']))
print(fruits_into_basket(['A', 'B', 'C', 'B', 'B', 'C']))
