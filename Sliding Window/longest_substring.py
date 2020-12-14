# Given a string, find the length of the longest substring
# in it with no more than K distinct characters.

def longest_substring_with_k_distinct(string, k):
    start = 0
    max_len = 0
    freq = {}
    for end in range(len(string)):
        right_char = string[end]
        if right_char not in freq:
            freq[right_char] = 0
        freq[right_char] += 1
        while len(freq) > k:
            left_char = string[start]
            freq[left_char] -= 1
            if freq[left_char] == 0:
                del freq[left_char]
            start += 1
        max_len = max(max_len, end - start + 1)
    return max_len


print(longest_substring_with_k_distinct("araaci", 2))
print(longest_substring_with_k_distinct("cbbebi", 3))
